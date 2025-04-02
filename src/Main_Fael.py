# import asyncio
# from playwright.async_api import async_playwright
# # import Page

# from Metodos import getFromAPI, Fael
# from Decorators.Main_StartUp import playwright_StartUp_nosub


# @playwright_StartUp_nosub()
# # Execução principal
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)  # Altere para True se não precisar visualizar
#         page = await browser.new_page()
#         await Fael.ajusteGradebook(page, "_104675_1")
#         await browser.close()

# import asyncio
# asyncio.run(main())

import asyncio
from Metodos import getFromAPI, Fael
from Decorators.Main_StartUp import playwright_StartUp_nosub

@playwright_StartUp_nosub(headless=False)
async def main(page):  # Agora recebe page diretamente do decorator
    await Fael.ajusteGradebook(page, "_104675_1")

# Removendo asyncio.run(main()), pois o decorator já deve estar gerenciando a execução