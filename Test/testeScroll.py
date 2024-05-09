import asyncio, sys
from playwright.async_api import Playwright, async_playwright, expect


from Metodos import getApiContent, capture_console_output_async, TimeStampedStream


@capture_console_output_async
async def run(playwright: Playwright) -> None:
    sys.stdout = TimeStampedStream(sys.stdout)
    print('teste')
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    username = ''
    password = ''
    await page.goto("https://sereduc.blackboard.com/")
    await page.get_by_label("Privacidade, cookies e termos").locator("div").nth(1).click()
    await page.get_by_role("button", name="OK").click()
    await page.get_by_label("Nome de usuário").click()
    await page.get_by_label("Nome de usuário").fill(username)
    await page.get_by_label("Nome de usuário").press("Tab")
    await page.get_by_label("Senha").fill(password)
    await page.get_by_label("Senha").press("Enter")
    await page.wait_for_load_state('domcontentloaded')
    await page.goto(url='https://sereduc.blackboard.com/ultra/courses/_139625_1/outline',
                    wait_until='domcontentloaded')
    await page.wait_for_timeout(4*1000)
    Classurl = page.url
    id_interno = '_139625_1'
    itemSearch = 'Avaliações'
    id_avaliacao = await getApiContent.API_Req_Content(page=page,
                            id_interno=id_interno, item_Search=itemSearch)
    # await page.wait_for_selector(selector='Avaliações', state='attached')
    await page.goto(f'{Classurl}?search=Avaliações')
    await page.locator(f'#folder-title-{id_avaliacao}').click()
    await page.get_by_label("Mais opções para Regras da").click()
    await page.get_by_text("Editar", exact=True).click()
    await page.get_by_role("heading", name="Regras da Avaliação - Resolu").click()
    await page.get_by_label("Novo link de LTI em undefined").click(click_count=3)
    await page.get_by_label("Novo link de LTI em undefined").fill("Regras da Avaliação - Resolução CONSU")
    await page.get_by_label("Novo link de LTI em undefined").press("Enter")
    await page.wait_for_load_state('domcontentloaded')
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_timeout(4*1000)
    print('teste 2')
    
    # ---------------------
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())

# import sys
# import logging
# from logging.config import dictConfig

# logging_config = dict(
#     version=1,
#     formatters={
#         'verbose': {
#             'format': ("[%(asctime)s] %(levelname)s "
#                        "[%(name)s:%(lineno)s] %(message)s"),
#             'datefmt': "%d/%b/%Y %H:%M:%S",
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s',
#         },
#     },
#     handlers={
#         'api-logger': {'class': 'logging.handlers.RotatingFileHandler',
#                            'formatter': 'verbose',
#                            'level': logging.DEBUG,
#                            'filename': 'logs/api.log',
#                            'maxBytes': 52428800,
#                            'backupCount': 7},
#         'batch-process-logger': {'class': 'logging.handlers.RotatingFileHandler',
#                              'formatter': 'verbose',
#                              'level': logging.DEBUG,
#                              'filename': 'logs/batch.log',
#                              'maxBytes': 52428800,
#                              'backupCount': 7},
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#             'formatter': 'simple',
#             'stream': sys.stdout,
#         },
#     },
#     loggers={
#         'api_logger': {
#             'handlers': ['api-logger', 'console'],
#             'level': logging.DEBUG
#         },
#         'batch_process_logger': {
#             'handlers': ['batch-process-logger', 'console'],
#             'level': logging.DEBUG
#         }
#     }
# )

# dictConfig(logging_config)

# api_logger = logging.getLogger('api_logger')
# batch_process_logger = logging.getLogger('batch_process_logger')