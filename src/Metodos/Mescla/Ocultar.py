from playwright.sync_api import Page


async def ocultar_boletim(page: Page, id_interno: str) -> None:
    
    # entra no black
    url_edit = f'./ultra/courses/{id_interno}/grades?gradebookView=grid'
    await page.goto(url=url_edit, wait_until='commit')
    await page.wait_for_load_state('domcontentloaded')
    print('Login na blackboard efetuado com sucesso')
    
    #entra no root
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
    await page.goto(url=url_edit, wait_until='commit')
    await page.wait_for_load_state('domcontentloaded')
    await page.get_by_role("button", name="Gerenciar").hover()
    await page.get_by_role("menuitem", name="Organização das colunas").click()
    print('Entrando no Root...')
        
    try:
        url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
        await page.goto(url=url_edit, wait_until='commit')
        await page.wait_for_load_state('domcontentloaded')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        print('Ocultando os itens novamente...')
        # await page.get_by_label("AV1").first.check()
        await page.get_by_role("row", name="AV1 Não está em um Período de avaliação Nota calculada").get_by_label("AV1").check(timeout=2*1000)
        await page.wait_for_timeout(1000)
        await page.get_by_role("row", name="AV2 Não está em um Período de avaliação Nota calculada").get_by_label("AV2").check()
        await page.wait_for_timeout(1000)
        await page.get_by_role("row", name="AF Não está em um Período de avaliação Nota calculada").get_by_label("AF").check()
        await page.wait_for_timeout(1000)
        # await page.get_by_label("AV2").first.check()
        # await page.get_by_label("AF").first.check()
        await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
        await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
        await page.get_by_role("button", name="Enviar").click()
        await page.wait_for_load_state('load')
        print('Sala Ajustada com sucesso')
            
    except:
        await page.get_by_role("cell", name="AV1 (Oculto)").wait_for(state='visible', timeout=2000)
        print('AV1 Oculto')
        await page.get_by_role("cell", name="AV2 (Oculto)").wait_for(state='visible', timeout=2000)
        print('AV2 Oculto')
        await page.get_by_role("cell", name="AF (Oculto)").wait_for(state='visible', timeout=2000)
        print('AF Oculto')
        