import asyncio, json
from playwright.async_api import async_playwright, expect


# input_string = "Atividade de Autoaprendizagem 1 2"
# digits = ''.join([ch for ch in input_string if ch.isdigit()])
# print(digits[1])

async def run() -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        
        CACHE_FILE = r'src\Metodos\Login\__pycache__\login_cache.json'
        with open(CACHE_FILE, 'r') as f:
            cache_data = json.load(f)
            await page.context.add_cookies(cache_data['cookies'])

        baseURL = 'https://sereduc.blackboard.com/'
        id_interno = '_200072_1'
        URL_API = fr'{baseURL}learn/api/v1/courses/{id_interno}/contents/'
        request = 'JSON.parse(document.body.innerText).results[0].contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.feedbackSettings.as.options'
        config = 'contentDetail["resource/x-bb-asmt-test-link"].test.deploymentSettings.feedbackSettings.as.options'
        
        await page.goto(url=URL_API, wait_until='commit')
        
        result_options = await page.evaluate(request)
        
        # print(f'{options}\n')
        # for each in options: print(each)
        
        options_correct = [
        "SCORE",
        "USER_ANSWERS",
        "CORRECT_ANSWERS",
        "INSTRUCTOR_FEEDBACK",
        "ALL_ANSWERS"]

        if result_options == options_correct:
            print('This config is correct')
        else:
            print('This config is wrong')
        
if __name__ == "__main__":
    asyncio.run(run())