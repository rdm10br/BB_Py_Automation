import asyncio
from playwright.async_api import Playwright, async_playwright, expect


from Metodos.API import getApiContent


async def run(playwright: Playwright) -> None:
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
    await page.goto(url='https://sereduc.blackboard.com/ultra/courses/_139625_1/outline', wait_until='domcontentloaded')
    await page.wait_for_timeout(4*1000)
    Classurl = page.url
    id_interno = '_139625_1'
    itemSearch = 'Avaliações'
    id_avaliacao = await getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=itemSearch)
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
    
    # ---------------------
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())