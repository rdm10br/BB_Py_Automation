import gc, sys, time
from functools import wraps
from playwright.async_api import async_playwright
# from PySide6.QtCore import Signal, QObject, QThread

from Metodos import getPlanilha, checkup_login
from Decorators.consoleWrapper import TimeStampedStream, capture_console_output_async

# class Worker_startup (QObject):
#     worker_signal = Signal(str)

#     def do_work(self):
#         # Simulate some work being done in a separate thread
#         self.thread = QThread()
#         self.moveToThread(self.thread)
#         self.thread.started.connect(playwright_StartUp)

def playwright_StartUp(func):
    @wraps(func)
    @capture_console_output_async
    async def wrapper(*args, **kwargs):
        async with async_playwright() as playwright:
            
            sys.stdout = TimeStampedStream(sys.stdout)
            print('\nExecution Start')
            
            browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'])
            context = await browser.new_context(no_viewport=True)
            page = await context.new_page()
            
            start_time0 = time.time()
            await checkup_login.checkup_login(page=page)
            end_time0 = time.time()
            execution_time = end_time0 - start_time0
            executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
            print(executionTime0)
            
            cookies = await page.context.cookies(urls="https://sereduc.blackboard.com/")
            print('cookies caught')
            
            total_lines_plan1 = getPlanilha.total_lines
            
            for index in range(total_lines_plan1):
                index+=1
                # progress_updated = Signal(int)
                # progress_updated.emit(f'{index}')
                print(f'Start loop {index}')
                
                cell_status = getPlanilha.getCell_status(index=index)
                start_time = time.time()
                
                if cell_status == 'nan':
                    
                    new_context = await browser.new_context(no_viewport=True)
                    await new_context.add_cookies(cookies)
                    new_page = await new_context.new_page()
                    
                    await func(new_page, index, *args, **kwargs)
                    
                    await new_page.close()
                    await new_context.close()
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                    print('{:5} | {}'.format(f'Run: {index}',executionTime))
                    
                    gc.collect()
                else :
                    print(f'Index: {index} in plan is alredy writen')
                    index+=1

            print('Execution End')
                    
            await browser.close()

    return wrapper