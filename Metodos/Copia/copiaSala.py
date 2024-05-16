from playwright.async_api import Playwright, async_playwright, expect, Page
from Metodos.API import getPlanilha

async def copySala(page: Page, index: int) -> None:
    """
    Function to copy Material from one class to another acording to the copiaSala
    plan sheet collums ID_ORIGIN and ID_DESTINY

    Args:
        page (Page): Page constructor form Playwright that
        you want this function to run
        index (int): row in the plan sheet where the function get the ID's
    """
    id_master = getPlanilha.getCell_plan2(index=index)
    id_copia = getPlanilha.getCell_copy_plan2(index=index)
    baseURL = "https://sereduc.blackboard.com/"
    coppyOnBlack = f"{baseURL}webapps/blackboard/execute/copy_content?navItem=copy_course_content_new&target=no&type=course"
    
    await page.goto(coppyOnBlack)
    
    # await page.get_by_label("Selecionar Tipo de cópia").select_option("O") #curso existente
    await page.get_by_label("Selecionar Tipo de cópia").select_option("N") #nova disciplina
    # await page.get_by_label("Selecionar Tipo de cópia").select_option("E") #copia exata
    
    await page.get_by_label("Código do Curso de Origem").fill(value=id_master)
    await page.get_by_label("Código do Curso de Destino").fill(value=id_copia)
    await page.locator('#bottom_Submit').click()
    await page.wait_for_load_state('domcontentloaded')
    await page.evaluate('document.querySelector("#stepcontent2 > ol > li:nth-child(4) > div > div > a:nth-child(1)").click()')
    await page.locator('#bottom_Submit').click()