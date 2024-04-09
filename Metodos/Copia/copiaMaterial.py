from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.API import getPlanilha

async def copyMaterial(page: Page , index) -> None:    
    id_master = getPlanilha.getCell_plan2(index=index)
    id_copia = getPlanilha.getCell_copy_plan2(index=index)
    baseURL = "https://sereduc.blackboard.com/"
    coppyOnBlack = f"{baseURL}webapps/blackboard/execute/copy_content?navItem=copy_course_content_new&target=no&type=course"
    
    await page.goto(coppyOnBlack)
    
    await page.get_by_label("Selecionar Tipo de cópia").select_option("O") #curso existente
    # await page.get_by_label("Selecionar Tipo de cópia").select_option("N") #nova disciplina
    # await page.get_by_label("Selecionar Tipo de cópia").select_option("E") #copia exata
    
    await page.get_by_label("Código do Curso de Origem").fill(value=id_master)
    await page.get_by_label("Código do Curso de Destino").fill(value=id_copia)
    await page.locator('#bottom_Submit').click()
    await page.wait_for_load_state('domcontentloaded')
    await page.evaluate('document.querySelector("#stepcontent2 > ol > li:nth-child(4) > div > div > a:nth-child(1)").click()')
    # await page.get_by_label('Imagem de banner').uncheck()
    await page.locator('#bottom_Submit').click()