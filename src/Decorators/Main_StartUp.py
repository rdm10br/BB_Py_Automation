# Importações de bibliotecas padrão e de terceiros necessárias para automação, manipulação de arquivos, variáveis de ambiente e concorrência.
import sys, time, os, asyncio, requests
# import json
# from datetime import datetime, timedelta
from async_lru import alru_cache
from functools import wraps, lru_cache
from playwright.async_api import async_playwright, Browser, Page, BrowserContext, Playwright
from multiprocessing import cpu_count
from dotenv import load_dotenv

# Importação de módulos internos do projeto para manipulação de planilhas, login, wrappers de console, criptografia, controle de pausa e internacionalização.
from Metodos import getPlanilha, checkup_login
from Decorators.Inscryption import Auto_Sub, Auto_Unsub
from Decorators.language_pack import lang_pack, lang_pack_async
from Decorators.consoleWrapper import TimeStampedStream, capture_console_output_async
from Decorators.pause_control import PauseWrapper, with_pause_control


async def login_block(
    _playwright: Playwright,
    _baseURL: str,
    _timeout: int = 60*1000,
    _headless: bool = False,
    _arg: list[str] = ['--start-maximized']
    ) -> tuple [Browser, BrowserContext, Page, list]:
    """
    Inicializa o navegador Playwright, realiza o login na aplicação e captura os cookies de autenticação.

    Args:
        _playwright (async_playwright): Instância do Playwright para automação de navegador.
        _baseURL (str): URL base da aplicação alvo.
        _timeout (int, opcional): Tempo limite para inicialização do navegador em milissegundos. Padrão: 60*1000.
        _headless (bool, opcional): Define se o navegador será executado em modo headless (sem interface gráfica). Padrão: False.
        _arg (str, opcional): Argumentos adicionais para inicialização do navegador. Padrão: '--start-maximized'.

    Returns:
        tuple: (browser, context, page, cookies)
            browser (Browser): Instância do navegador Playwright.
            context (BrowserContext): Contexto do navegador com configurações aplicadas.
            page (Page): Página inicial aberta no contexto.
            cookies (list): Lista de cookies capturados após login.
    """
    print('\nExecution Start')
                
    browser = await _playwright.chromium.launch(headless=_headless, args=_arg, timeout=_timeout)
    context = await browser.new_context(base_url=_baseURL, no_viewport=True, color_scheme='dark')
    page = PauseWrapper(await context.new_page())
    
    start_time0 = time.time()
    await checkup_login.checkup_login(page=page)
    end_time0 = time.time()
    
    execution_time = round(end_time0 - start_time0, 2)
    print(f'Execution time: {execution_time} seconds')
    
    cookies = await page.context.cookies(urls=_baseURL)
    print('cookies caught')
    
    return browser, context, page, cookies


async def loop_block(
    _total_lines: int,
    _baseURL: str,
    _browser: Browser,
    _page: Page,
    _func: callable,
    _cookies: list,
    _autoSub: bool = False,
    *args,
    **kwargs
    ) -> None:
    """
    Executa um loop sobre as linhas de uma planilha, realizando ações específicas para cada linha de acordo com seu status.
    Realiza requisições à API para verificar o status do curso, executa funções customizadas e gerencia contexto/páginas do navegador.

    Args:
        _total_lines (int): Número total de linhas a serem processadas na planilha.
        _baseURL (str): URL base para requisições à API.
        _browser (Browser): Instância do navegador Playwright.
        _page (Page): Página Playwright principal para login e renovação de cookies.
        _func (callable): Função a ser executada para cada linha válida.
        _cookies (list): Lista de cookies de autenticação.
        _autoSub (bool, opcional): Se True, realiza inscrição automática antes da função e desinscrição após. Padrão: False.
        *args: Argumentos posicionais adicionais para a função customizada.
        **kwargs: Argumentos nomeados adicionais para a função customizada.

    Returns:
        None
    """
    for index in range(_total_lines):
        index+=1
        
        print(f'Start loop {index}/{_total_lines}')
        
        # Seleciona métodos e identificadores de acordo com o script principal em execução.
        if os.path.basename(sys.argv[0]) == 'Main_expurgo.py' or os.path.basename(sys.argv[0]) == 'Main_expurgo_lote.py':
            cell_status = getPlanilha.getCell_status_expurgo(index=index)
            if os.path.basename(sys.argv[0]) == 'Main_expurgo_lote.py':
                id_externo = getPlanilha.unique_expurgo[index-1]
            else:
                id_externo = getPlanilha.getCell_expurgo(index)
        else:
            cell_status = getPlanilha.getCell_status(index=index)
            id_externo = getPlanilha.getCell(index)
            
        start_time = time.time()
        
        # Processa apenas linhas ainda não tratadas (status 'nan').
        if cell_status == 'nan':
            # Monta URL da API para consulta do curso.
            _url = f'./learn/api/public/v3/courses/courseId:{id_externo}'
            cookies_cache = {cookie['name']: cookie['value'] for cookie in _cookies}
            
            response = requests.get(
                url=f'{_baseURL}{_url}',
                cookies=cookies_cache
            )
            print(f'response status for classroom: {id_externo} | {response.status_code}')
            
            # Se não autorizado, renova login e cookies.
            if str(response.status_code) == '401':
                await checkup_login.checkup_login(page=_page)
                cookies = await _page.context.cookies(urls=_baseURL)
                cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}

                response = requests.get(
                    url=f'{_baseURL}{_url}',
                    cookies=cookies_cache
                )
                print(f'response status for classroom: {id_externo} | {response.status_code}')
            
            # Consulta conteúdos do curso.
            _url = f'./learn/api/public/v1/courses/{response.json().get("id")}/contents'
            request = requests.get(
                url=f'{_baseURL}{_url}',
                cookies=cookies_cache
            )
            
            # Define se o curso está vazio ou não, de acordo com o script principal.
            if os.path.basename(sys.argv[0]) == 'Main_Open_Mescla.py':
                is_empty = 1
            elif os.path.basename(sys.argv[0]) == 'Main_Close_Mescla.py':
                is_empty = 1
            elif os.path.basename(sys.argv[0]) == 'Main_Orfão.py':
                is_empty = 1
                response.status_code = 200
            elif os.path.basename(sys.argv[0]) == 'Main_expurgo.py':
                is_empty = 1
                response.status_code = 200
            elif os.path.basename(sys.argv[0]) == 'Main_expurgo_lote.py':
                is_empty = 1
                response.status_code = 200
            else:
                is_empty = (lambda: len(request.json().get('results')) if request.json() and request.json().get('results') else 0)()

            if is_empty != None:
                print(f'itens in {id_externo}: {is_empty}')
                
            # Se curso encontrado e não vazio, executa função customizada em novo contexto/página.
            if str(response.status_code) == '200' and is_empty > 0:
                new_context = await _browser.new_context(base_url=_baseURL, no_viewport=True)
                await new_context.add_cookies(_cookies)
                new_page = PauseWrapper(await new_context.new_page())
                
                if _autoSub:
                    await Auto_Sub(page=new_page, index=index)
                
                await _func(new_page, index, *args, **kwargs)
                
                if _autoSub:
                    await Auto_Unsub(page=new_page, index=index)
                
                await new_page.close()
                await new_context.close()
                
                end_time = time.time()
                execution_time = round(end_time - start_time, 2)
                print(f'Run: {index}/{_total_lines} | Execution time: {execution_time} seconds')
            elif str(response.status_code) == '404':
                print(f'Index: {index} | sala: {id_externo} not found!')
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='not found!')
            elif str(response.status_code) == '401':
                print(f'Index: {index} | sala: {id_externo} not authorized!')
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='not authorized!')
            elif is_empty == 0:
                print(f'Index: {index} | sala: {id_externo} is empty!')
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='empty')
        else :
            print(f'Index: {index} in plan is alredy writen')


def playwright_StartUp(timeout: int = 60*1000, headless: bool = False, arg: list[str] = ['--start-maximized'], autoSub: bool = False):
    """
    Decorador para inicializar o ambiente Playwright, realizar login, configurar contexto e executar função customizada sobre todas as linhas da planilha.
    Gerencia o ciclo de vida do navegador e imprime o tempo total de execução.

    Args:
        timeout (int, opcional): Tempo limite para inicialização do navegador em milissegundos. Padrão: 60*1000.
        headless (bool, opcional): Define se o navegador será executado em modo headless. Padrão: False.
        arg (str, opcional): Argumentos adicionais para inicialização do navegador. Padrão: '--start-maximized'.
        autoSub (bool, opcional): Se True, realiza inscrição automática antes da função e desinscrição após. Padrão: False.

    Returns:
        function: Função decorada pronta para execução assíncrona.
    """
    def decorator(func):
        @alru_cache(maxsize=128)
        @wraps(func)
        @lang_pack_async
        @with_pause_control()
        @capture_console_output_async
        async def wrapper(*args, **kwargs):
            async with async_playwright() as playwright:
                load_dotenv()
                baseURL = os.getenv('BASE_URL')
                
                sys.stdout = TimeStampedStream(sys.stdout)
                
                browser, context, page, cookies = await login_block(
                    _playwright=playwright,
                    _baseURL=baseURL,
                    _timeout=timeout,
                    _headless=headless,
                    _arg=arg
                )
                
                # Seleciona o total de linhas de acordo com o script principal.
                if os.path.basename(sys.argv[0]) == 'Main_expurgo.py':
                    total_lines = getPlanilha.total_lines_expurgo
                elif os.path.basename(sys.argv[0]) == 'Main_expurgo_lote.py':
                    total_lines = getPlanilha.total_unique_expurgo
                else:
                    total_lines = getPlanilha.total_lines
                
                start_time0 = time.time()
                
                await loop_block(
                    _total_lines=total_lines,
                    _baseURL=baseURL,
                    _browser=browser,
                    _page=page,
                    _func=func,
                    _cookies=cookies,
                    _autoSub=autoSub,
                    *args,
                    **kwargs
                )
                
                end_time0 = time.time()
                execution_time = round(end_time0 - start_time0, 2)
                print(f'Execution time: {execution_time} seconds')
                
                print('Execution End')
                await browser.close()

        return wrapper
    return decorator


def playwright_StartUp_nosub_test(timeout: int = 60*1000, headless: bool = False, arg: str = '--start-maximized'):
    """
    Decorador para inicializar o ambiente Playwright e executar função customizada sobre todas as linhas da planilha,
    sem realizar inscrição/desinscrição automática. Utiliza processamento assíncrono em lotes para otimizar a execução.

    Args:
        timeout (int, opcional): Tempo limite para inicialização do navegador em milissegundos. Padrão: 60*1000.
        headless (bool, opcional): Define se o navegador será executado em modo headless. Padrão: False.
        arg (str, opcional): Argumentos adicionais para inicialização do navegador. Padrão: '--start-maximized'.

    Returns:
        function: Função decorada pronta para execução assíncrona.
    """
    def decorator(func):
        @alru_cache(maxsize=128)
        @wraps(func)
        @lang_pack_async
        @with_pause_control()
        @capture_console_output_async
        async def wrapper(*args, **kwargs):
            async with async_playwright() as playwright:
                load_dotenv()
                baseURL = os.getenv('BASE_URL')

                sys.stdout = TimeStampedStream(sys.stdout)
                
                browser, context, page, cookies = await login_block(
                    _playwright=playwright,
                    _baseURL=baseURL,
                    _timeout=timeout,
                    _headless=headless,
                    _arg=arg
                )

                total_lines_plan1 = getPlanilha.total_lines

                async def process_line(index):
                    cell_status = getPlanilha.getCell_status(index=index)
                    if cell_status == 'nan':
                        start_time = time.time()

                        # Create a new context and process the page
                        new_context = await browser.new_context(base_url=baseURL, no_viewport=True)
                        await new_context.add_cookies(cookies)
                        new_page = PauseWrapper(await new_context.new_page())

                        await func(new_page, index, *args, **kwargs)

                        await new_page.close()
                        await new_context.close()

                        end_time = time.time()
                        execution_time = round(end_time - start_time, 2)
                        print(f'Run: {index}/{total_lines_plan1} | Execution time: {execution_time} seconds')
                    else:
                        print(f'Index: {index} in plan is already written')
                start_time0 = time.time()
                # Determine the number of threads (logical processors) and use half
                num_threads = max(1, cpu_count() // 2)
                print(f'Using {num_threads} threads')

                # Create and manage tasks in batches to limit concurrent execution
                async def run_in_batches(indices, batch_size):
                    for i in range(0, len(indices), batch_size):
                        batch = indices[i:i + batch_size]
                        await asyncio.gather(*[process_line(index) for index in batch])

                # Prepare the list of indices and process them
                indices = list(range(1, total_lines_plan1 + 1))
                await run_in_batches(indices, num_threads)

                end_time0 = time.time()
                execution_time = round(end_time0 - start_time0, 2)
                print(f'Execution time: {execution_time} seconds')

                print('Execution End')
                await browser.close()

        return wrapper
    return decorator