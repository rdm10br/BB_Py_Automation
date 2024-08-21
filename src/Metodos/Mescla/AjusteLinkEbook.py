from playwright.async_api import Page
from Metodos.API import getApiContent
import regex as re


async def API_Ativ_Course_count(page: Page, id_interno: str) -> str:
    """
    Async Function that search in the API for the ```count``` of the
    classroom you want, in the order of the Excel file you gave.

    Args:
        page (Page): Page constructor form Playwright that
        you want this API to run
        id_externo (str): the External ID of the classroom you want

    Returns:
        str: ```count```
    """
    # baseURL = "https://sereduc.blackboard.com/"
    internalID_API = f'./learn/api/public/v3/courses/{id_interno}'
    
    request = '() => {return JSON.parse(document.body.innerText).name.match(/(?<=Extensão).*(?=[(])/)}'

    print(f'Looking on Api Request Activity to find course area of {id_interno}')

    await page.goto(internalID_API)
    count = await page.evaluate(request)
    string_sem_especiais = re.sub(r'[^\w\s]', '', str(count))
    string_sem_especiais = re.sub(r'[\s]', '', str(string_sem_especiais))
    return str(string_sem_especiais)


async def ajusteLinkEbook(page: Page, id_interno: str) -> None:
    """
    Function that adjusts that link in the 'Sofia' item;
    This function gets the ```id_interno``` and throw to the content API
    to find the ```itemSearch``` folder in the classroom.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    item = 'Materiais Didáticos'
    itemSearch = 'Biblioteca Virtual: e-Book'
    url = page.url
    print(f'Getting API ID for {itemSearch}')
    try:
        id_folder = await getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=item)
        id_ebook = await getApiContent.API_Req_Content_children(page=page, id_interno=id_interno, father_id=id_folder, item_Search=itemSearch)
        await page.wait_for_load_state('domcontentloaded')
    except Exception as e:
        if 'Item não encontrado' in str(e):
            print(f'Erro na sala: {id_interno}; Item: {itemSearch} não foi encontrado')
            pass
        else:
            print('Erro ao processar request:', e)
            pass
    if id_ebook != None:
        LinkEdit = f'{url}/edit/lti/{id_ebook}'
        print(id_ebook)
        link = {
            'I':['https://sereduc.blackboard.com/bbcswebdav/xid-486398464_1'],
            'II':['https://sereduc.blackboard.com/bbcswebdav/xid-486398463_1'],
            'III':['https://sereduc.blackboard.com/bbcswebdav/xid-486398462_1'],
            'IV':['https://sereduc.blackboard.com/bbcswebdav/xid-486398461_1']
        }
        
        count = await API_Ativ_Course_count(page=page, id_interno=id_interno)
        print(count)
        if count in link:
            print('Starting adjustments: "Biblioteca Virtual: e-Book"')
            await page.goto(LinkEdit)
            await page.get_by_placeholder("Formato: meuwebsite.com").click(click_count=3)
            print('Changing link...')
            link_s = re.sub(r"\[\'", '', str(link[count]))
            link_s = re.sub(r"\'\]", '', link_s)
            await page.get_by_placeholder("Formato: meuwebsite.com").fill(link_s)
            await page.wait_for_load_state('networkidle')
            await page.get_by_text("Você precisará desta informa").click()
            print('Saving...')
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_timeout(1.5*1000)
        else:
            print(f'{count} fora do escopo planejado!')
        pass
    else:
        print(f'Item: {itemSearch} não encontrado!')
        pass