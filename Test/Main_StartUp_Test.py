import asyncio, gc, pytest, sys
from functools import wraps
from playwright.async_api import Playwright, async_playwright, expect


# importando Metodos principais
from Metodos import (getPlanilha, checkup_login, getFromAPI,
                     capture_console_output_async, TimeStampedStream)


# Decorator for log
@capture_console_output_async
async def run(playwright: Playwright) -> None:
    sys.stdout = TimeStampedStream(sys.stdout)
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()

    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    total_lines_plan1 = getPlanilha.total_lines

    # Verificar se está logado e logar
    await checkup_login.checkup_login(page=page)

    # Salvar os cookies da página original
    cookies = await page.context.cookies(urls=baseURL)

    for index in range(total_lines_plan1):
        index += 1

        cell_status = getPlanilha.getCell_status(index=index)

        if cell_status != 'nan':
            pass
        else:
            new_browser = await playwright.chromium.launch(headless=False)
            new_context = await new_browser.new_context(no_viewport=True)
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)
            new_page = await new_context.new_page()

            # request from API
            id_externo = getPlanilha.getCell(index=index)
            id_interno = await getFromAPI.API_Req(page=new_page, index=index)

            classUrlUltra = f'{classURL}{id_interno}/outline'

            print(id_externo)

            await new_page.goto(classUrlUltra)

            #

            await new_context.close()
            await new_browser.close()

            gc.collect()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())