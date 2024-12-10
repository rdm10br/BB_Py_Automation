import gc, sys, time, os, asyncio
from functools import wraps, lru_cache
from playwright.async_api import async_playwright
from multiprocessing import cpu_count
from dotenv import load_dotenv

from Metodos import getPlanilha, checkup_login
from Decorators.consoleWrapper import TimeStampedStream, capture_console_output_async
from Decorators.Inscryption import Auto_Sub, Auto_Unsub

def playwright_StartUp(func):
    @lru_cache
    @wraps(func)
    @capture_console_output_async
    async def wrapper(*args, **kwargs):
        async with async_playwright() as playwright:
            load_dotenv()
            baseURL = os.getenv('BASE_URL')
            
            sys.stdout = TimeStampedStream(sys.stdout)
            print('\nExecution Start')
            
            browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'], timeout=60*1000)
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
                # progress_updated = Signal(int)
                # progress_updated.emit(f'{index}')
                print(f'Start loop {index}/{total_lines_plan1}')
                # await flush_then_wait()
                cell_status = getPlanilha.getCell_status(index=index)
                start_time = time.time()
                
                if cell_status == 'nan':
                    
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
                    # await flush_then_wait()
                    gc.collect()
                else :
                    print(f'Index: {index} in plan is alredy writen')
                    # await flush_then_wait()
                    index+=1
            
            end_time0 = time.time()
            execution_time = end_time0 - start_time0
            executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
            print(executionTime0)
            
            print('Execution End')
            # await flush_then_wait()
            await browser.close()

    return wrapper

def playwright_StartUp_nosub(func):
    @lru_cache
    @wraps(func)
    @capture_console_output_async
    async def wrapper(*args, **kwargs):
        async with async_playwright() as playwright:
            load_dotenv()
            baseURL = os.getenv('BASE_URL')
            
            sys.stdout = TimeStampedStream(sys.stdout)
            print('\nExecution Start')
            
            browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'], timeout=60*1000)
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
                # progress_updated = Signal(int)
                # progress_updated.emit(f'{index}')
                print(f'Start loop {index}/{total_lines_plan1}')
                # await flush_then_wait()
                cell_status = getPlanilha.getCell_status(index=index)
                start_time = time.time()
                
                if cell_status == 'nan':
                    
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
                    # await flush_then_wait()
                    gc.collect()
                else :
                    print(f'Index: {index} in plan is alredy writen')
                    # await flush_then_wait()
                    index+=1
                    
            end_time0 = time.time()
            execution_time = end_time0 - start_time0
            executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
            print(executionTime0)
            
            print('Execution End')
            # await flush_then_wait()
            await browser.close()

    return wrapper

def playwright_StartUp_nosub_test(func):
    @lru_cache
    @wraps(func)
    @capture_console_output_async
    async def wrapper(*args, **kwargs):
        async with async_playwright() as playwright:
            load_dotenv()
            baseURL = os.getenv('BASE_URL')

            sys.stdout = TimeStampedStream(sys.stdout)
            print('\\nExecution Start')

            browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'], timeout=60 * 1000)
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