import asyncio, gc, sys, time, os, json
from playwright.async_api import Playwright, async_playwright
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from functools import lru_cache
from async_lru import alru_cache
from dotenv import load_dotenv


#importando Metodos principais
from Metodos import checkup_login, getBQ, fileChooser, create_bq, junctionWindow, junctionSizeWindow
from Decorators import capture_console_output_async, TimeStampedStream, lang_pack_async, PauseWrapper, with_pause_control

@alru_cache(maxsize=128)
@lang_pack_async
@with_pause_control()
@capture_console_output_async
async def run(playwright: Playwright) -> None:
    load_dotenv()
    id_repository = os.getenv('BQ_ID_REPOSITORY')
    baseURL = os.getenv('BASE_URL')
    CACHE_FILE = r'src\Metodos\BQ\__pycache__\queue_files.json'
    
    sys.stdout = TimeStampedStream(sys.stdout)
    print('\nExecution Start')
    
    browser = await playwright.chromium.launch(headless=False, args=['--start-maximized'], timeout=60*1000)
    context = await browser.new_context(base_url=baseURL, no_viewport=True)
    # page = PauseWrapper(await context.new_page())
    page = await context.new_page()
    
    
    rootBQ = f'./webapps/assessment/do/authoring/'\
    f'viewAssessmentManager?assessmentType=Pool&course_id={id_repository}'
    
    limit = 100
    offset = 0
    maxLimit = 2147483647 # 2_147_483_647
    
    bq_id = f'./learn/api/v1/courses/{id_repository}/assessments?limit={limit}&offset={offset}'
    bq_id_max = f'./learn/api/v1/courses/{id_repository}/assessments?limit={maxLimit}&offset={offset}'
    
    def API_bq_id(_offset: int):
        API = f'./learn/api/v1/courses/{id_repository}/assessments?limit={limit}&offset={_offset}'
        return API
    
    def BQTest(id_BQ: str):
        BQ = f'./webapps/assessment/do/authoring/modifyAssessment?'\
            f'method=modifyAssessment&course_id={id_repository}'\
            f'&assessmentId={id_BQ}'
        return BQ
    
    def filteredRequest_title(item_search: str, config: str):
        request = f'''() => {{
            const data = JSON.parse(document.body.innerText).results.find(item => item.title === "{item_search}");
            if (data && (data.{config}).toString) {{
                return data.{config};
            }} else {{
                throw new Error('{item_search} not found in room {id_repository}');
                }}
            }}'''
        return request
    
    async def loop_BQ_id(Offset: int):
        await page.goto(API_bq_id(_offset=Offset))
        id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
        return id_BQ
    
    async def bq_cleanup(_cache_length: int) -> None:
        """
        CleanUp BQ repository if it has more than 60 and more than 2 months

        Args:
            _cache_length (int): _description_
        """
        async def handle_dialog(dialog):
            print("Dialog appeared with message:", dialog.message)
            await dialog.accept()  # or dialog.dismiss()
        
        await page.goto(bq_id_max)
        _count = await page.evaluate('JSON.parse(document.body.innerText).paging.count')
        if (_cache_length + _count) >= 60:
            _list = await page.evaluate('JSON.parse(document.body.innerText).results.map(item => item.lastModifiedDate)')
            # parsed_list = [datetime.fromisoformat(dt.replace("Z", "+00:00")).strftime("%Y-%m") for dt in _list]
            # Reference date: two months ago, at month precision
            # limit_date = datetime.today() - relativedelta(months=2)
            limit_date = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
            limit_date -= relativedelta(months=2)
            old_indices = []
            parsed_dates = []
            delete_list = []
            for i, dt in enumerate(_list):
                dt_obj = datetime.fromisoformat(dt.replace("Z", "+00:00")).replace(day=1)
                parsed_dates.append((i, dt_obj))
                if dt_obj <= limit_date:
                    old_indices.append(i)
                    
            _title_list = await page.evaluate('JSON.parse(document.body.innerText).results.map(item => item.title)')
            
            if not old_indices:
                # Sort by datetime ascending, then pick first 10 indices
                parsed_dates.sort(key=lambda x: x[1])
                old_indices = [i for i, _ in parsed_dates[:10]]
                
                for _i in old_indices:
                    delete_list.append(_title_list[_i])
                print(f"Selected indices for cleanup: {delete_list}")
            else:
                for _i in old_indices:
                    delete_list.append(_title_list[_i])
                print(f"Selected indices for cleanup: {delete_list}")
            
            if delete_list:
                for _d in delete_list:
                    await page.goto(f'{rootBQ}&showAll=true')
                    print(f'Deleting: {_d}')
                    await page.get_by_role("button", name=_d).click()
                    page.once("dialog", handle_dialog)
                    await page.get_by_role("menuitem", name="Excluir").click()
                    print(f'{_d} Deleted!')
        return
    
    start_time0 = time.time()
    await checkup_login.checkup_login(page=page)
    end_time0 = time.time()
    execution_time = end_time0 - start_time0
    executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
    print(executionTime0)
    
    cookies = await page.context.cookies(urls=baseURL)
    print('cookies caught')
    
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding="utf-8") as f:
            cache_data = json.load(f)
        print('Json queue found')
    else:
        fileChooser.window_file()
        print('files caught')
        print('Json queue created')
        with open(CACHE_FILE, 'r', encoding="utf-8") as f:
            cache_data = json.load(f)
        print('Json queue openned')
            
    cache_length = len(cache_data['queue_files'])
    
    # loop for store queue_file.json info
    for i in range(cache_length):
        _cache = cache_data['queue_files'][i]
        _path = _cache['path']
        
        try:
            _cache['bqName']
        except KeyError:
            _cache['bqName'] = create_bq.get_bq_name(path=_path)
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(cache_data, json_file, indent=4, ensure_ascii=False)

        try:
            _cache['isJunction']
        except KeyError:
            _cache['isJunction'] = junctionWindow.window(bq_name=cache_data['queue_files'][i]['bqName'])
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
        
        if _cache['questionCount'] == 0:
            _cache['questionCount'] = getBQ.enunciado_count(path=_path)
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
        
        if _cache['isJunction'] == 'Yes':
            print('Choose other BQ for the Junction...')
            size = junctionSizeWindow.window()
            for _size in range(size):
                fileChooser.window_file(bq_name=f'{cache_data['queue_files'][i]['bqName']} Parte {_size+1}')
    
    with open(CACHE_FILE, 'r', encoding="utf-8") as f:
        cache_data = json.load(f)
    cache_length = len(cache_data['queue_files'])
    
    for i in range(cache_length):
        _cache = cache_data['queue_files'][i]
        _path = _cache['path']
        
        try:
            _cache['bqName']
        except KeyError:
            _cache['bqName'] = create_bq.get_bq_name(path=_path)
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(cache_data, json_file, indent=4, ensure_ascii=False)

        try:
            _cache['isJunction']
        except KeyError:
            _cache['isJunction'] = 'Yes'
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
        
        if _cache['questionCount'] == 0:
            _cache['questionCount'] = getBQ.enunciado_count(path=_path)
            with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
    
    # loop for create question
    start_time_queue = time.time()
    
    with open(CACHE_FILE, 'r', encoding="utf-8") as f:
        cache_data = json.load(f)
    cache_length = len(cache_data['queue_files'])
    
    await bq_cleanup(cache_length)
    
    for i in range(cache_length):
        cache = cache_data['queue_files'][i]
        if cache['processingStatus'] == "Finished":
            print(f'{cache['bqName']} is already finished!')
        else:
            path = cache['path']
            isjunction = cache['isJunction']
            questionCount = cache['questionsMade']
                    
            doc = cache['questionCount']
            print(doc)
            BQ_name = cache['bqName']
            print(BQ_name)
                    
                
            try:
                id_BQ = ''
                BQ_count = 0
                try:
                    id_BQ = cache['idBQ']
                except KeyError:
                    await page.goto(bq_id_max)
                    id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
                    cache['idBQ'] = id_BQ
                    with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                        json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
                    
                    if isjunction == 'No':
                        BQ_count = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='questionCount'))
                        cache['questionsMade'] = BQ_count
                        with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                            json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
                    
                    if BQ_count >= questionCount:
                        questionCount = BQ_count
                    else:
                        BQ_count = questionCount
                    
                print(f'ID found: {id_BQ}')
            except Exception as e:
                await page.goto(rootBQ)
                await create_bq.create_bq(page=page, BQ_name=BQ_name)
                await page.goto(bq_id)
                
                length = await page.evaluate('JSON.parse(document.body.innerText).results.length')
                count = await page.evaluate('JSON.parse(document.body.innerText).paging.count')
                # counter = count - length
                
                while not id_BQ:
                    try:
                        id_BQ = await page.evaluate(filteredRequest_title(item_search=BQ_name, config='id'))
                        print(f'ID found: {id_BQ}')
                    except Exception as e:
                        print(f'Error fetching id_BQ: {e}')
                        try:
                            if offset <= count:
                                offset+=length
                                id_BQ = await loop_BQ_id(offset)
                                print(f'ID found: {id_BQ}')
                        except Exception as e:
                            print(f'Error in loop_BQ_id: {e}')

            await page.goto(BQTest(id_BQ=id_BQ))
            
            start_time_doc = time.time()
            for index in range(doc):
                index +=1
                
                if index <= BQ_count:
                    print(f'\nQuestão : {index} - already made!')
                    pass
                else:
                    new_context = await browser.new_context(base_url=baseURL, no_viewport=True)
                    await new_context.add_cookies(cookies)
                    new_page = PauseWrapper(await new_context.new_page())
                    
                    start_time = time.time()
                    print(f'\nQuestão : {index}')
                    
                    await new_page.goto(url=BQTest(id_BQ=id_BQ), wait_until='commit')
                    # await new_page.wait_for_timeout(1000)
                    
                    await create_bq.create_question(index=index, path=path, page=new_page)
                    
                    await new_context.close()
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    executionTime = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
                    print('{:5} | {}'.format(f'Run: {index}',executionTime))
                    
                    cache['questionsMade'] = index
                    with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                        json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
                        
                    if cache['questionsMade'] < doc:
                        cache['processingStatus'] = "Running"
                        with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                            json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
                        
                    gc.collect()
                    
            end_time_doc = time.time()
            execution_time_doc = end_time_doc - start_time_doc
            executionTime_doc = f'Execution time: {'{:.2f}'.format(execution_time_doc)} seconds'
            print(executionTime_doc)
                    
            if cache['questionsMade'] == doc:
                
                cache['processingStatus'] = "Finished"
                with open(CACHE_FILE, "w", encoding="utf-8") as json_file:
                    json.dump(cache_data, json_file, indent=4, ensure_ascii=False)
    
    end_time_queue = time.time()
    execution_time_queue = end_time_queue - start_time_queue
    executionTime_queue = f'Execution time: {'{:.2f}'.format(execution_time_queue)} seconds'
    print(executionTime_queue)
    
    os.remove(CACHE_FILE)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
        
asyncio.run(main())