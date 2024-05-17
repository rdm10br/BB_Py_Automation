from playwright.async_api import Playwright, async_playwright, expect, Page
from Metodos.API import getApiContent

async def ajusteAvaliacao(page: Page, id_interno: str) -> None:
    """
    Function that adjusts that name of the 'Avaliação' item;
    This function gets the ```id_interno``` and throw to the content API
    to find the ```itemSearch``` folder in the classroom.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    itemSearch = 'Avaliações'
    Classurl = page.url
    print(f'Getting API ID for {itemSearch} folder')
    id_avaliacao = await getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=itemSearch)
    print('ID found')
    
    print('Starting adjustments: "Avaliação"')
    await page.goto(url=f'{Classurl}?search=Avaliações',wait_until='domcontentloaded')
    print('Opening Folder')
    await page.locator(f'#folder-title-{id_avaliacao}').click()
    print('Opening menu options')
    await page.get_by_label("Mais opções para Regras da").click()
    print('Editing item...')
    await page.get_by_text("Editar", exact=True).click()
    await page.get_by_role("heading", name="Regras da Avaliação - Resolu").click()
    await page.get_by_label("Novo link de LTI em undefined").click(click_count=3)
    print('Adjusting name')
    await page.get_by_label("Novo link de LTI em undefined").fill("Regras da Avaliação - Resolução CONSU")
    await page.get_by_label("Novo link de LTI em undefined").press("Enter")
    await page.wait_for_load_state('domcontentloaded')
    print('Saving...')
    await page.get_by_role("button", name="Salvar").click()