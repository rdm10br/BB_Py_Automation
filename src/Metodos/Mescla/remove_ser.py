from playwright.async_api import Page

async def removeSer(page: Page, id_interno: str) -> None:
    baseURL = 'https://sereduc.blackboard.com/'
    item = 'Ser Melhor'
    classurl = f'{baseURL}ultra/courses/outline?serach={item}'
    await page.goto(url=classurl, wait_until='commit')
    await page.wait_for_timeout(1000*4)
    await page.wait_for_load_state('networkidle')
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(1000*6)
    if await page.get_by_role("heading", name="Nenhum resultado encontrado").is_visible():
        print(f'no {item} found')
        pass
    else:
        print(f'{item} found')
        await page.get_by_label('Mais opções para SER Melhor (').click()
        await page.wait_for_load_state('load')
        await page.get_by_role('menuitem', name='Excluir').click()
        await page.wait_for_load_state('load')
        await page.get_by_role('button', name='Excluir').click()
        await page.wait_for_load_state('load')
        await page.wait_for_timeout(1000*3)