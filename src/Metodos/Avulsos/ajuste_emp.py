from playwright.async_api import Page


# from Metodos import getApiContent


async def ajusteMatD(page: Page, id_interno: str) -> None:
    
    classURL = f'./ultra/courses/'
    urlClassUltra = f'{classURL}{id_interno}/outline'
    def urlSearch(i: int): return f'{urlClassUltra}?search=Unidade {i}'
    
    link = [
            'https://sereduc.blackboard.com/bbcswebdav/xid-342284753_1',
            'https://sereduc.blackboard.com/bbcswebdav/xid-342313078_1',
            'https://sereduc.blackboard.com/bbcswebdav/xid-342313184_1',
            'https://sereduc.blackboard.com/bbcswebdav/xid-342311920_1'
            ]
    
    # internalID_API = f'./learn/api/public/v1/courses/{id_interno}/contents'
    # id_folder: list = []
    
    # def filteredRequest_title(item_search: str, config: str):
    #     request = f'''() => {{
    #         const data = JSON.parse(document.body.innerText).results.find(item => item.title === "{item_search}");
    #         if (data && (data.{config}).toString) {{
    #             return data.{config};
    #         }} else {{
    #             throw new Error('{item_search} not found in room {id_interno}');
    #             }}
    #         }}'''
    #     return request
    
    # def APIFolder(father_id: str):
    #     API = f'./learn/api/public/v1/courses/{id_interno}/contents/{father_id}/children'
    #     return API
    
    # await page.goto(url=internalID_API, wait_until='networkidle')
    
    # for index in range(4):
    #     index += 1
    #     config = 'id'
    #     unidade = f'Unidade {index}'
    #     print(f'Checking Unidade {index} id...')
    #     id_value = await page.evaluate(filteredRequest_title(item_search=unidade, config=config))
    #     id_folder.append(id_value)
    #     print(id_folder[index-1])
        
    
    for i in range(4):
        i += 1
        
        print(f'Starting adjustments: "Unidade {i}"')
        await page.goto(url=urlSearch(i=i))
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_load_state('networkidle')
        await page.wait_for_load_state('load')
        if  await page.get_by_role("button", name=f"Unidade {i}", exact=True).is_visible():
            print(f'Opening "Unidade {i}" folder')
            await page.get_by_role("button", name=f"Unidade {i}", exact=True).click()
            print('Opening menu options')
            await page.get_by_label("Mais opções para Material Didático Interativo").click()
            print('Editing item...')
            await page.get_by_text("Editar", exact=True).click()
            await page.get_by_placeholder("Formato: meuwebsite.com").click(click_count=3)
            print(f'Changing link to "{link[i-1]}"...')
            await page.get_by_placeholder("Formato: meuwebsite.com").fill(link[i-1])
            await page.get_by_text("Máximo de 750 caracteres").click()
            print('Saving...')
            await page.get_by_role("button", name="Salvar").click()
            await page.wait_for_load_state('load')
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(1.5*1000)
        else:
            print('Canais de Comunicação não encontrado!')