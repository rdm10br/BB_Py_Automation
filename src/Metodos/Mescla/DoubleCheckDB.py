from playwright.async_api import Page, expect
from Metodos import getApiContent
import regex as re
import requests, json, os, asyncio
from dotenv import load_dotenv

def folder(id_interno: str, item) -> str:
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
    data = API(url)  # A API deve retornar os dados completos
    
    try:
        # Verifica se o item contém 'contentHandler' e se ele é True
        for i in data.get('results', []):
            if i.get('title') == item:  # Verifica o item específico
                if 'contentHandler' in i:  # Verifica se a chave 'contentHandler' existe
                    # Verifica o id do contentHandler e retorna o tipo correspondente
                    print(i.get('contentHandler', {}).get('id', None))
                    return i.get('contentHandler', {}).get('id', None)  # Retorna o id do contentHandler
        return None  # Se o item não for encontrado ou não tiver contentHandler
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o item: {e}")
        return None
    
def API_ID(id_interno: str, item):
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
    data = API(url)  # A API deve retornar os dados completos
    
    try:
        # Verifique se a resposta é uma lista ou um dicionário
        if isinstance(data, dict):  # Se for um dicionário, tente acessar 'results'
            items = data.get('results', [])
        elif isinstance(data, list):  # Se for uma lista, use diretamente
            items = data
            
        # Verifique se o item existe na lista de itens
        for i in items:
            if i.get('title') == item:  # Verifica se o item tem o título correspondente
                if 'id' in i:  # Verifica se existe a chave 'id'
                    return i.get('id')  # Retorna o id ou False
        return False  # Se o item não for encontrado ou o formato estiver errado
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o item: {e}")
        return False

def API_child_id(id_interno, item, item_unidade):
    id_parent = API_ID(id_interno, item)
    url = f'/learn/api/public/v1/courses/{id_interno}/contents/{id_parent}/children'
    Item_list = api_child(id_interno, item)
    data = API(url)
    if item_unidade in Item_list:
        try:
            # Verifique se a resposta é uma lista ou um dicionário
            if isinstance(data, dict):  # Se for um dicionário, tente acessar 'results'
                items = data.get('results', [])
            elif isinstance(data, list):  # Se for uma lista, use diretamente
                items = data
                
            # Verifique se o item existe na lista de itens
            for i in items:
                if i.get('title') == item_unidade:  # Verifica se o item tem o título correspondente
                    if 'id' in i:  # Verifica se existe a chave 'id'
                        return i.get('id', False)  # Retorna o id ou False
            return False  # Se o item não for encontrado ou o formato estiver errado
        except Exception as e:
            print(f"Ocorreu um erro ao verificar o item: {e}")
            return False
    
    
def api_child(id_interno, item) -> list:
    id_parent = API_ID(id_interno, item)
    url = f'/learn/api/public/v1/courses/{id_interno}/contents/{id_parent}/children'
    data = API(url)

    item_list = [item.get('title', '') for item in data.get('results', [])]
    return item_list

def API(_url: str) -> list:
    try:
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        BASE_URL = os.getenv('BASE_URL')

        # Caminho do arquivo de cache dos dados da URL
        cache_file = r'src\Metodos\Mescla\__pycache__\api_cache.json'  # Cache específico para dados da URL
        
        cookie_file = r'src\Metodos\Login\__pycache__\login_cache.json'
        
        # Lê o arquivo de cache para obter os cookies
        with open(cookie_file, 'r') as c:
            cache_cookies = json.load(c)
        # Verifica se o arquivo de cache existe
        
        cookies = {cookie['name']: cookie['value'] for cookie in cache_cookies['cookies']}
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='UTF-8') as f:
                cache = json.load(f)

        else:
            cache = {}

        # Verifica se a URL já está no cache
        if _url in cache:
            print(f"Cache encontrado para a URL: {_url}")
            return cache[_url]  # Retorna os dados armazenados para a URL

        # Se não houver cache, faz a requisição HTTP
        print(f"Fazendo requisição para a URL: {_url}")
        
        response = requests.get(
            url=f'{BASE_URL}{_url}',
            cookies=cookies
        )
        
        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()
        
        # Converte a resposta em JSON
        data = response.json()

        # Armazena o retorno da URL no cache
        cache[_url] = data
        
        # Salva o cache atualizado no arquivo de cache
        with open(cache_file, 'w', encoding='UTF-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)

        return data
    except Exception as e:
        # Aqui você pode logar o erro ou retorná-lo de alguma forma mais informativa
        print(f"Ocorreu um erro: {e}")
        return []  # Retorna uma lista vazia em caso de erro
    
    
def Item_list(id_interno: str):
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
    data = API(url)
    # Extrai o campo 'title' do JSON. Se não existir, retorna uma lista vazia
    item_list = [item.get('title', '') for item in data.get('results', [])]
    return item_list

async def DoubleCheckDB(page: Page, id_interno: str) -> None:
    # Chama a função API de forma assíncrona usando asyncio.to_thread
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
   
    _item_list = await asyncio.to_thread(Item_list, id_interno)
    print(_item_list)
    
    item_list = _item_list  # Agora estamos usando o item_list retornado pela função API
        
    # contentHandler
    
    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    await page.get_by_role("link", name="Boletim de notas").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_label("Configurações", exact=True).click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.mouse.wheel(0, 500)  # Rola 500px para baixo
    await page.wait_for_timeout(2*1000)
    await page.get_by_role("button", name="Fechar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_role("link", name="Grupos").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_role("link", name="Conteúdo da disciplina").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(3*1000)
    await loopItemList(page, id_interno, item_list)
    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    await page.get_by_role("link", name="Banco de questões Gerenciar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(4*1000)
    await page.get_by_role("button", name="Fechar").click()
    await page.get_by_role("link", name="Imagem do curso Editar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(4*1000)
    await page.get_by_role("button", name="Fechar").click()

async def loopItemList(page: Page, id_interno, item_list):
    
    _ItemRolagem = [
        'Workshop',
        'AV1',
        'Avaliações',
        'WebAula'
        ]
    _ItemConfig = [  #todos que tem config clicar, menos fale com tutor
            'Desafio Colaborativo',
            # 'AV1'
        ]
    _ItemConfigFcT = [  #Fale com tutor config
        'Fale com o Tutor'
        ]
    _ItemDCTimeout= [
        'Meu Desempenho'
    ]
    
    _ItemSFTimeout= [
        'Organize seus estudos com a Sofia'
    ]
    
    for item in item_list:
        
        # if "Organize seus estudos com a Sofia" in item:
        #         await page.wait_for_load_state("domcontentloaded")
        #         await page.get_by_label("Mais opções para Organize").click()
        #         await page.get_by_text("Editar", exact=True).click()
        #         await page.locator('text=Detalhes do link LTI').wait_for(state="visible", timeout=1000*30)
        #         await page.get_by_placeholder("Formato: meuwebsite.com").click()
        #         await page.get_by_placeholder("Formato: meuwebsite.com").press("End")
        #         await page.wait_for_timeout(2*1000)
        #         await page.get_by_role("button", name="Fechar").click()
        
        if "Atividade de Aulas Práticas" in item:
            print("Rolando a página...")
            await page.mouse.wheel(0, 5000)  # Rola 5000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("button", name="Atividade de Aulas Práticas", exact=True).click()
            await page.get_by_role("link", name="Atividade Prática").click()
            await page.get_by_role("link", name="Configurações", exact=True).click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(3*1000)
            await page.mouse.wheel(0, 1000)  # Rola 1000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 800)  # Rola 800px para baixo
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 350)  # Rola 350px para baixo
            await page.wait_for_timeout(2*1000)
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(6*1000)
            await page.get_by_role("button", name="Fechar").click()
            await page.get_by_role("button", name="Fechar").click()
            await page.get_by_role("button", name="Atividade de Aulas Práticas", exact=True).click()
        
        if "AV1" in item:
            await AV1(page, id_interno, item)
            
        if "Unidade" in item:
            await unidade(page, id_interno, item)

        else:
            id_DB = API_ID(id_interno, item)
            if not id_DB:
                print(f"ID não encontrado para o item: {item}")
                continue  # Pula para o próximo item se o ID não for encontrado
            await page.goto(url=f"./ultra/courses/{id_interno}/outline")
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(5*1000)
            try:
                if item in _ItemDCTimeout:
                    print("executando o seguinte item: Meu Desempenho")
                    await page.get_by_role("link", name="Meu Desempenho", exact=True).click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(10*1000)
                    await page.get_by_role("button", name="Fechar").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(2*1000)
                    continue
                
                if item in _ItemSFTimeout:
                    print("executando o seguinte item: Organize seus estudos com a Sofia")
                    await page.get_by_role("link", name="Organize seus estudos com a").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(10*1000)
                    await page.get_by_role("button", name="Fechar").click()
                    await page.wait_for_load_state("domcontentloaded")
                    await page.get_by_label("Mais opções para Organize").click()
                    await page.get_by_text("Editar", exact=True).click()
                    await page.locator('text=Detalhes do link LTI').wait_for(state="visible", timeout=1000*30)
                    await page.get_by_placeholder("Formato: meuwebsite.com").click()
                    await page.get_by_placeholder("Formato: meuwebsite.com").press("End")
                    await page.wait_for_timeout(2*1000)
                    await page.get_by_role("button", name="Fechar").click()
                
                    continue
                
                elif item in _ItemRolagem:
                    print("Rolando a página...")
                    await page.mouse.wheel(0, 5000)  # Rola 5000px para baixo
                    await page.wait_for_timeout(2*1000)
                # await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
                # await page.wait_for_load_state('load')
                # await page.wait_for_timeout(3*1000)
                elif item in _ItemConfigFcT:
                    print("executando o seguinte item: Fale com o Tutor")
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(4*1000)
                    await page.get_by_role("link", name="Fale com o Tutor").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(4*1000)
                    await page.get_by_label("Editar configurações do diário").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(4*1000)
                elif item in _ItemConfig:
                    print("executando o seguinte item: Desafio Colaborativo")
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(4*1000)
                    await page.get_by_role("link", name="Desafio Colaborativo").click()
                    await page.wait_for_timeout(3*1000)
                    await page.get_by_role("link", name="Configurações", exact=True).click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(5*1000)
                
                elif "Solicite seu livro impresso" in item:
                    await page.wait_for_timeout(1*1000)
                    continue
                
                    
                # await page.get_by_role("button", name="Fechar").click()
                # await page.wait_for_load_state('load')
                # await page.wait_for_timeout(5*1000)
                else:
                    await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(3*1000)
                    await page.get_by_role("button", name="Fechar").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(5*1000)
                    
                    continue

            except Exception as e:
                # await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
                # await page.wait_for_load_state('load')
                # await page.wait_for_timeout(3*1000)
                # await page.get_by_role("button", name="Fechar").click()
                # await page.wait_for_load_state('load')
                # await page.wait_for_timeout(5*1000)
                print(f'Erro ao processar request {item} in {id_interno}:', e)

async def unidade(page: Page, id_interno, item):
    id_DB = API_ID(id_interno, item)
    if not id_DB:
        print(f"ID não encontrado para o item: {item}")
        # continue  # Pula para o próximo item se o ID não for encontrado
    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    
    try:
        await page.wait_for_load_state("domcontentloaded")
        await page.locator('text=Unidade 1').wait_for(state="visible", timeout=1000*60)

        
        if not await page.locator(f'//div[@data-content-id="{id_DB}"]').is_visible(timeout=10000):  # Espera 10 segundos para o item estar visível
            print(f"Elemento com id {id_DB} não encontrado na página.")
            # continue  # Pula para o próximo item
        item_unidade = api_child(id_interno, item)
        await page.wait_for_load_state("domcontentloaded", timeout=1000*10)
        await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
        await page.wait_for_load_state("domcontentloaded", timeout=1000*10)
        
        for i in item_unidade:
            id_i = API_child_id(id_interno, item, i)
            await page.wait_for_load_state("domcontentloaded")
            await page.wait_for_timeout(1000*4)
            await page.locator(f'//div[@data-content-id="{id_i}"]').click()
            print(f"Processando item: {i}")
            await page.wait_for_timeout(1000*6)

            if "Atividade de Autoaprendizagem" in i:
                print("Encontrou 'Atividade de Autoaprendizagem' no item")
                await page.get_by_role("link", name="Configurações", exact=True).click()
                await page.wait_for_load_state('load')
                await page.wait_for_timeout(3*1000)
                await page.mouse.wheel(0, 1000)  # Rola 1000px para baixo
                await page.wait_for_timeout(2*1000)
                await page.mouse.wheel(0, 800)  # Rola 800px para baixo
                await page.wait_for_timeout(2*1000)
                await page.mouse.wheel(0, 350)  # Rola 350px para baixo
                await page.wait_for_timeout(2*1000)
                await page.wait_for_load_state('load')
                await page.wait_for_timeout(6*1000)
                await page.get_by_role("button", name="Fechar").click()
                await page.wait_for_timeout(2*1000)
                await page.get_by_role("button", name="Fechar").click()
                
                continue
            
            if "Material complementar" in i:
                    print("Encontrou 'Material complementar', pulando item.")
                    continue
            
            await page.wait_for_timeout(3*1000)
            await page.get_by_role("button", name="Fechar").click()

    except Exception as e:
        print(f'Erro ao processar request {item} in {id_interno}:', e)
    
async def AV1(page: Page, id_interno, item):
    try:
        # Obtemos o tipo de contentHandler
        contentHandler_id = folder(id_interno, item)
        
        if contentHandler_id == "resource/x-bb-asmt-test-link":
            # Realiza as ações se contentHandler for "resource/x-bb-asmt-test-link"
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 5000)  # Rola 5000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("link", name="AV1").click()
            await page.get_by_role("link", name="Configurações", exact=True).click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(3*1000)
            await page.mouse.wheel(0, 1000)  # Rola 1000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.locator("#attempt-count").select_option("number:5")
            await page.wait_for_timeout(5*1000)
            await page.locator("#attempt-count").select_option("number:1")
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 800)  # Rola 800px para baixo
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 500)  # Rola 350px para baixo
            await page.wait_for_timeout(2*1000)
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("button", name="Fechar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("button", name="Fechar").click()
        
        elif contentHandler_id == "resource/x-bb-folder":
            # Realiza as ações se contentHandler for "resource/x-bb-folder"
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 5000)  # Rola 5000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("button", name="AV1", exact=True).click()
            await page.get_by_role("link", name="Avaliação Workshop").click()
            await page.get_by_role("link", name="Configurações", exact=True).click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(3*1000)
            await page.mouse.wheel(0, 1000)  # Rola 1000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 800)  # Rola 800px para baixo
            await page.wait_for_timeout(2*1000)
            await page.locator("#attempt-count").select_option("number:5")
            await page.get_by_role("button", name="Fechar").click()
            await page.locator("#attempt-count").select_option("number:1")
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 350)  # Rola 350px para baixo
            await page.wait_for_timeout(2*1000)
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(6*1000)
            await page.get_by_role("button", name="Fechar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("button", name="Fechar").click()
            await page.get_by_role("link", name="Atividade Contextualizada").click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("link", name="Configurações", exact=True).click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(3*1000)
            await page.mouse.wheel(0, 1000)  # Rola 1000px para baixo
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 800)  # Rola 800px para baixo
            await page.wait_for_timeout(2*1000)
            await page.mouse.wheel(0, 350)  # Rola 350px para baixo
            await page.wait_for_timeout(2*1000)
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(6*1000)
            await page.get_by_role("button", name="Fechar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(2*1000)
            await page.get_by_role("button", name="Fechar").click()
            await page.get_by_role("button", name="AV1", exact=True).click()
        
        else:
            print(f"Content handler não encontrado ou não corresponde a um tipo esperado. ID: {contentHandler_id}")
    
    except Exception as e:
        print(f"Ocorreu um erro durante a execução de AV1: {e}")