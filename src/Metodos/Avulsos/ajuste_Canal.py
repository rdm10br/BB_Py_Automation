from playwright.async_api import Page


async def ajusteCanal(page: Page, id_interno: str) -> None:
    
    classURL = f'./ultra/courses/'
    urlClassUltra = f'{classURL}{id_interno}/outline'
    urlSearch = f'{urlClassUltra}?search=Canais de Comunicação'
    link = 'https://sereduc.blackboard.com/bbcswebdav/xid-345163866_1'
    
    print('Starting adjustments: "Canais de Comunicação"')
    await page.goto(urlSearch)
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('networkidle')
    await page.wait_for_load_state('load')
    if  await page.get_by_text('Canais de Comunicação').is_visible():
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