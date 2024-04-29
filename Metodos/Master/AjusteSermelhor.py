from playwright.async_api import Playwright, async_playwright, expect, Page


async def ajusteSerMelhor(page: Page, id_interno: str) -> None:
    """
    Function that adjusts that link in the 'Ser Melhor' item;

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    urlClassUltra = f'{classURL}{id_interno}/outline'
    urlSearch = f'{urlClassUltra}?search=Ser Melhor'
    
    await page.goto(urlSearch)
    await page.wait_for_load_state('domcontentloaded')
    # await page.get_by_role("heading", name='Módulo').press("End")
    # await page.get_by_role("heading", name='Módulo').press("End")
    # await page.press('body','End')
    # await page.wait_for_load_state('domcontentloaded')
    # await page.press('body','End')
    # await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    # await page.wait_for_load_state('load')
    await page.get_by_label("Mais opções para SER Melhor (").click()
    await page.get_by_text("Editar", exact=True).click()
    await page.get_by_placeholder("Digite um URL").click(click_count=3)
    await page.get_by_placeholder("Digite um URL").fill("https://forms.office.com/r/wX8V5625hs")
    # await page.wait_for_load_state('networkidle')
    await page.get_by_text("Máximo de 750 caracteres").click()
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_load_state('load')