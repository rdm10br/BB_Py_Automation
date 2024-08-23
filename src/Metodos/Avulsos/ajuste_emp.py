from playwright.async_api import Page


from Metodos import getApiContent


async def ajusteMatD(page: Page, id_interno: str) -> None:
    
    classURL = f'./ultra/courses/'
    urlClassUltra = f'{classURL}{id_interno}/outline'
    urlSearch = f'{urlClassUltra}?search=Manuais'
    
    
    for i in range(4):
        i += 1
        # get all unidades id's
    
    for i in range(4):
        i += 1
        # get all links for Material Didatico
        link = {
            'https://sereduc.blackboard.com/bbcswebdav/xid-345163866_1',
            'https://sereduc.blackboard.com/bbcswebdav/xid-345163866_1',
            'https://sereduc.blackboard.com/bbcswebdav/xid-345163866_1',
            'https://sereduc.blackboard.com/bbcswebdav/xid-345163866_1'
            }
        
        print(f'Starting adjustments: "Unidade {i}"')
        await page.goto(urlSearch)
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_load_state('networkidle')
        await page.wait_for_load_state('load')
        if  await page.get_by_role("button", name="Manuais", exact=True).is_visible():
            print('Opening "Manuais" folder')
            await page.get_by_role("button", name="Manuais", exact=True).click()
            print('Opening menu options')
            await page.get_by_label("Mais opções para Canais de Comunicação").click()
            print('Editing item...')
            await page.get_by_text("Editar", exact=True).click()
            await page.get_by_placeholder("Digite um URL").click(click_count=3)
            print('Changing link...')
            await page.get_by_placeholder("Digite um URL").fill(link)
            await page.get_by_text("Máximo de 750 caracteres").click()
            print('Saving...')
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(1.5*1000)
        else:
            print('Canais de Comunicação não encontrado!')