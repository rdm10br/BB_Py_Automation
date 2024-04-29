from playwright.async_api import Playwright, async_playwright, expect, Page

async def AjusteNotaZero(page: Page, id_interno: str) -> None:
    """
    Function that uncheck the 'Nota Zero Automática' item in the grades options
    of the classroom.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    ContentURL = f'{classURL}{id_interno}/outline'
    GradeURL = f'{classURL}{id_interno}/grades?gradebookView=list&listViewType=assignments'
    
    await page.goto(GradeURL)
    await page.get_by_label("Configurações", exact=True).click()
    await page.get_by_text("Atribui nota zero").click()
    await page.get_by_text("Remover notas zero atribuídas").click()
    await page.get_by_role("button", name="Confirmar").click()
    await page.locator("#main-content > div:nth-child(4)").click()
    await page.goto(ContentURL)