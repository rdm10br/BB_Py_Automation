import gc, sys, time, os, asyncio, requests, json
from datetime import datetime, timedelta
from functools import wraps, lru_cache
from playwright.async_api import async_playwright
from multiprocessing import cpu_count
from dotenv import load_dotenv

from Metodos import getPlanilha, checkup_login
from Decorators.consoleWrapper import TimeStampedStream, capture_console_output_async
from Decorators.Inscryption import Auto_Sub, Auto_Unsub


def playwright_StartUp(timeout: int = 60*1000, headless: bool = False, arg: str = '--start-maximized'):
    def decorator(func):
        @lru_cache
        @wraps(func)
        @capture_console_output_async
        async def wrapper(*args, **kwargs):
            async with async_playwright() as playwright:
                load_dotenv()
                baseURL = os.getenv('BASE_URL')
                
                sys.stdout = TimeStampedStream(sys.stdout)
                print('\nExecution Start')
                
                browser = await playwright.chromium.launch(headless=headless, args=[arg], timeout=timeout)
                context = await browser.new_context(base_url=baseURL, no_viewport=True, color_scheme='dark')
                page = await context.new_page()
                
                start_time0 = time.time()
                await checkup_login.checkup_login(page=page)
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                print(executionTime0)
                
                cookies = await page.context.cookies(urls=baseURL)
                print('cookies caught')
                # await flush_then_wait()
                total_lines_plan1 = getPlanilha.total_lines
                
                start_time0 = time.time()
                for index in range(total_lines_plan1):
                    index+=1
                    print(f'Start loop {index}/{total_lines_plan1}')
                    cell_status = getPlanilha.getCell_status(index=index)
                    start_time = time.time()
                    id_externo = getPlanilha.getCell(index)
                    
                    if cell_status == 'nan':
                        
                        _url = f'./learn/api/public/v3/courses/courseId:{id_externo}'
                        cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}
                        
                        response = requests.get(
                            url=f'{baseURL}{_url}',
                            cookies=cookies_cache
                        )
                        # Verifica se a requisição foi bem-sucedida
                        print(f'response status for classroom: {id_externo} | {response.status_code}')
                        
                        if str(response.status_code) == '401':
                            await checkup_login.checkup_login(page=page)
                            cookies = await page.context.cookies(urls=baseURL)
                            cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}

                            response = requests.get(
                                url=f'{baseURL}{_url}',
                                cookies=cookies_cache
                            )
                            print(f'response status for classroom: {id_externo} | {response.status_code}')
                        
                        _url = f'./learn/api/public/v1/courses/{response.json().get('id')}/contents'
                        request = requests.get(
                            url=f'{baseURL}{_url}',
                            cookies=cookies_cache
                        )
                        is_empty = (lambda: len(request.json().get('results')) if request.json() and request.json().get('results') else 0)()
                        
                        if is_empty != None:
                            print(f'itens in {id_externo}: {is_empty}')
                            
                        if str(response.status_code) == '200' and is_empty > 0:
                        
                            new_context = await browser.new_context(base_url=baseURL, no_viewport=True)
                            await new_context.add_cookies(cookies)
                            new_page = await new_context.new_page()
                            
                            await Auto_Sub(page=new_page, index=index)
                            await func(new_page, index, *args, **kwargs)
                            await Auto_Unsub(page=new_page, index=index)
                            
                            await new_page.close()
                            await new_context.close()
                            
                            end_time = time.time()
                            execution_time = end_time - start_time
                            executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                            print('{:5} | {}'.format(f'Run: {index}/{total_lines_plan1}',executionTime))
                            gc.collect()
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
                
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                print(executionTime0)
                
                print('Execution End')
                await browser.close()

        return wrapper
    return decorator


def playwright_StartUp_nosub(timeout: int = 60*1000, headless: bool = False, arg: str = '--start-maximized'):
    def decorator(func):
        @lru_cache
        @wraps(func)
        @capture_console_output_async
        async def wrapper(*args, **kwargs):
            async with async_playwright() as playwright:
                load_dotenv()
                baseURL = os.getenv('BASE_URL')
                
                sys.stdout = TimeStampedStream(sys.stdout)
                print('\nExecution Start')
                
                browser = await playwright.chromium.launch(headless=headless, args=[arg], timeout=timeout)
                context = await browser.new_context(base_url=baseURL, no_viewport=True, color_scheme='dark')
                page = await context.new_page()
                
                start_time0 = time.time()
                await checkup_login.checkup_login(page=page)
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                print(executionTime0)
                
                cookies = await page.context.cookies(urls=baseURL)
                print('cookies caught')
                total_lines_plan1 = getPlanilha.total_lines
                
                start_time0 = time.time()
                for index in range(total_lines_plan1):
                    index+=1
                    
                    print(f'Start loop {index}/{total_lines_plan1}')
                    cell_status = getPlanilha.getCell_status(index=index)
                    start_time = time.time()
                    id_externo = getPlanilha.getCell(index)
                    
                    
                    if cell_status == 'nan':
                        
                        _url = f'./learn/api/public/v3/courses/courseId:{id_externo}'
                        cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}
                        
                        response = requests.get(
                            url=f'{baseURL}{_url}',
                            cookies=cookies_cache
                        )
                        # Verifica se a requisição foi bem-sucedida
                        print(f'response status for classroom: {id_externo} | {response.status_code}')
                        
                        if str(response.status_code) == '401':
                            await checkup_login.checkup_login(page=page)
                            cookies = await page.context.cookies(urls=baseURL)
                            cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}

                            response = requests.get(
                                url=f'{baseURL}{_url}',
                                cookies=cookies_cache
                            )
                            print(f'response status for classroom: {id_externo} | {response.status_code}')
                        
                        _url = f'./learn/api/public/v1/courses/{response.json().get('id')}/contents'
                        request = requests.get(
                            url=f'{baseURL}{_url}',
                            cookies=cookies_cache
                        )
                        
                        if os.path.basename(sys.argv[0]) == 'Main_Open_Mescla.py':
                            is_empty = 1
                        elif os.path.basename(sys.argv[0]) == 'Main_Orfão.py':
                            is_empty = 1
                            response.status_code = 200
                        else:
                            is_empty = (lambda: len(request.json().get('results')) if request.json() and request.json().get('results') else 0)()

                        
                        if is_empty != None:
                            print(f'itens in {id_externo}: {is_empty}')
                            
                            
                        if str(response.status_code) == '200' and is_empty > 0:
                            new_context = await browser.new_context(base_url=baseURL, no_viewport=True)
                            await new_context.add_cookies(cookies)
                            new_page = await new_context.new_page()
                            
                            await func(new_page, index, *args, **kwargs)
                            
                            await new_page.close()
                            await new_context.close()
                            
                            end_time = time.time()
                            execution_time = end_time - start_time
                            executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                            print('{:5} | {}'.format(f'Run: {index}/{total_lines_plan1}',executionTime))
                            gc.collect()
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
                        
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                print(executionTime0)
                
                print('Execution End')
                await browser.close()

        return wrapper
    return decorator


def playwright_StartUp_nosub_expurgo(timeout: int = 60*1000, headless: bool = False, arg: str = '--start-maximized'):
    def decorator(func):
        @lru_cache
        @wraps(func)
        @capture_console_output_async
        async def wrapper(*args, **kwargs):
            async with async_playwright() as playwright:
                load_dotenv()
                baseURL = os.getenv('BASE_URL')
                
                sys.stdout = TimeStampedStream(sys.stdout)
                print('\nExecution Start')
                
                browser = await playwright.chromium.launch(headless=headless, args=[arg], timeout=timeout)
                context = await browser.new_context(base_url=baseURL, no_viewport=True, color_scheme='dark')
                page = await context.new_page()
                
                start_time0 = time.time()
                await checkup_login.checkup_login(page=page)
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                print(executionTime0)
                
                cookies = await page.context.cookies(urls=baseURL)
                print('cookies caught')
                total_lines_plan1 = getPlanilha.total_lines_expurgo
                
                start_time0 = time.time()
                for index in range(total_lines_plan1):
                    index+=1
                    
                    print(f'Start loop {index}/{total_lines_plan1}')
                    cell_status = getPlanilha.getCell_status(index=index)
                    start_time = time.time()
                    id_externo = getPlanilha.getCell(index)
                    
                    
                    if cell_status == 'nan':
                        
                        _url = f'./learn/api/public/v3/courses/courseId:{id_externo}'
                        cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}
                        
                        response = requests.get(
                            url=f'{baseURL}{_url}',
                            cookies=cookies_cache
                        )
                        # Verifica se a requisição foi bem-sucedida
                        print(f'response status for classroom: {id_externo} | {response.status_code}')
                        
                        if str(response.status_code) == '401':
                            await checkup_login.checkup_login(page=page)
                            cookies = await page.context.cookies(urls=baseURL)
                            cookies_cache = {cookie['name']: cookie['value'] for cookie in cookies}

                            response = requests.get(
                                url=f'{baseURL}{_url}',
                                cookies=cookies_cache
                            )
                            print(f'response status for classroom: {id_externo} | {response.status_code}')
                        
                        _url = f'./learn/api/public/v1/courses/{response.json().get('id')}/contents'
                        request = requests.get(
                            url=f'{baseURL}{_url}',
                            cookies=cookies_cache
                        )
                        
                        if os.path.basename(sys.argv[0]) == 'Main_Open_Mescla.py':
                            is_empty = 1
                        elif os.path.basename(sys.argv[0]) == 'Main_Orfão.py':
                            is_empty = 1
                            response.status_code = 200
                        elif os.path.basename(sys.argv[0]) == 'Main_expurgo.py':
                            is_empty = 1
                            response.status_code = 200
                        else:
                            is_empty = (lambda: len(request.json().get('results')) if request.json() and request.json().get('results') else 0)()

                        
                        if is_empty != None:
                            print(f'itens in {id_externo}: {is_empty}')
                            
                            
                        if str(response.status_code) == '200' and is_empty > 0:
                            new_context = await browser.new_context(base_url=baseURL, no_viewport=True)
                            await new_context.add_cookies(cookies)
                            new_page = await new_context.new_page()
                            
                            await func(new_page, index, *args, **kwargs)
                            
                            await new_page.close()
                            await new_context.close()
                            
                            end_time = time.time()
                            execution_time = end_time - start_time
                            executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                            print('{:5} | {}'.format(f'Run: {index}/{total_lines_plan1}',executionTime))
                            gc.collect()
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
                        
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                print(executionTime0)
                
                print('Execution End')
                await browser.close()

        return wrapper
    return decorator


def playwright_StartUp_nosub_test(timeout: int = 60*1000, headless: bool = False, arg: str = '--start-maximized'):
    def decorator(func):
        @lru_cache
        @wraps(func)
        @capture_console_output_async
        async def wrapper(*args, **kwargs):
            async with async_playwright() as playwright:
                load_dotenv()
                baseURL = os.getenv('BASE_URL')

                sys.stdout = TimeStampedStream(sys.stdout)
                print('\nExecution Start')

                browser = await playwright.chromium.launch(headless=headless, args=[arg], timeout=timeout)
                context = await browser.new_context(base_url=baseURL, no_viewport=True, color_scheme='dark')
                page = await context.new_page()

                # Login check
                start_time0 = time.time()
                await checkup_login.checkup_login(page=page)
                end_time0 = time.time()
                execution_time = end_time0 - start_time0
                print(f'Execution time: {execution_time:.2f} seconds')

                cookies = await page.context.cookies(urls=baseURL)
                print('cookies caught')

                total_lines_plan1 = getPlanilha.total_lines

                async def process_line(index):
                    cell_status = getPlanilha.getCell_status(index=index)
                    if cell_status == 'nan':
                        start_time = time.time()

                        # Create a new context and process the page
                        new_context = await browser.new_context(base_url=baseURL, no_viewport=True)
                        await new_context.add_cookies(cookies)
                        new_page = await new_context.new_page()

                        await func(new_page, index, *args, **kwargs)

                        await new_page.close()
                        await new_context.close()

                        end_time = time.time()
                        execution_time = end_time - start_time
                        print(f'Run: {index}/{total_lines_plan1} | Execution time: {execution_time:.2f} seconds')
                    else:
                        print(f'Index: {index} in plan is already written')

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
                execution_time = end_time0 - start_time0
                print(f'Execution time: {execution_time:.2f} seconds')

                print('Execution End')
                await browser.close()

        return wrapper
    return decorator