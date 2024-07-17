from playwright.async_api import Playwright, async_playwright, expect, Page
from Metodos.API import getApiContent

async def ajusteSofia(page: Page, id_interno: str) -> None:
    """
    Function that adjusts that link in the 'Sofia' item;
    This function gets the ```id_interno``` and throw to the content API
    to find the ```itemSearch``` folder in the classroom.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    itemSearch = 'Sofia'
    url = page.url
    print(f'Getting API ID for {itemSearch}')
    try:
        id_sofia = await getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=itemSearch)
        await page.wait_for_load_state('domcontentloaded')
        # print(id_sofia)
    except Exception as e:
        if 'Item não encontrado' in str(e):
            print(f'Erro na sala: {id_interno}; Item: {itemSearch} não foi encontrado')
            pass
        else:
            print('Erro ao processar request:', e)
            pass
    if id_sofia != None:
        LinkEdit = f'{url}/edit/lti/{id_sofia}'

        print('Starting adjustments: "Sofia"')
        await page.goto(LinkEdit)
        await page.get_by_placeholder("Formato: meuwebsite.com").click(click_count=3)
        print('Changing link...')
        await page.get_by_placeholder("Formato: meuwebsite.com").fill("sofialti.ldmedtech.com.br/v1/launch/ser-sofia-plano-estudos")
        await page.wait_for_load_state('networkidle')
        await page.get_by_text("Você precisará desta informa").click()
        print('Saving...')
        await page.get_by_role("button", name="Salvar").click()
        await page.wait_for_load_state('load')
        await page.wait_for_timeout(1.5*1000)
    else:
        print(f'Item: {itemSearch} não encontrado!')
        pass