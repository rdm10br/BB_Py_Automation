from playwright.sync_api import Page


async def ajuste_mescla(page: Page, id_interno: str) -> None:
    
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
    
    #deixar visivel o item
    try:
        await page.get_by_role("cell", name="AV1* (Oculto)").wait_for(state='visible', timeout=2000)
        await page.get_by_role("cell", name="AV2* (Oculto)").wait_for(state='visible', timeout=2000)
        await page.get_by_label("AV1*").check()
        await page.get_by_label("AV2*").check()
        await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
        await page.get_by_role("menuitem", name="Mostrar colunas selecionadas", exact=True).click()
        await page.get_by_role("button", name="Enviar").click()
        await page.wait_for_load_state('load')
        
        #voltando para o centro de notas
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        
        #verificando se realmente ficou visivel
        await page.get_by_role("cell", name="AV1* (Oculto)").wait_for(state='visible', timeout=2000)
        await page.get_by_role("cell", name="AV2* (Oculto)").wait_for(state='visible', timeout=2000)
        
        #voltando para o black
    except:
        url_edit = f'./ultra/courses/{id_interno}/grades?gradebookView=list'
        await page.goto(url=url_edit, wait_until='commit')
        await page.wait_for_load_state('domcontentloaded')
        
        #entrando no boletim e removendo o "*"
        await page.get_by_role("link", name="AF*", exact=True).click()
        await page.get_by_role("heading", name="AF*").click()
        await page.get_by_label("Novo cálculo em undefined").fill("AF")
        await page.get_by_label("Novo cálculo em undefined").press("Enter")
        await page.get_by_role("button", name="Fechar").click()
        await page.get_by_role("link", name="AV1*").click()
        await page.get_by_role("heading", name="AV1*").click()
        await page.get_by_label("Novo cálculo em undefined").fill("AV1")
        await page.get_by_label("Novo cálculo em undefined").press("Enter")
        await page.get_by_role("button", name="Fechar").click()
        await page.get_by_role("link", name="AV2*").click()
        await page.get_by_role("heading", name="AV2*").click()
        await page.get_by_label("Novo cálculo em undefined").fill("AV2")
        await page.get_by_label("Novo cálculo em undefined").press("Enter")
        await page.get_by_role("button", name="Fechar").click()
        print('Boletim ajustado com sucesso')
        
        #voltando para o root pra ocultar os itens novamente
        url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
        await page.goto(url=url_edit, wait_until='commit')
        await page.wait_for_load_state('domcontentloaded')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        print('Ocultando os itens novamente...')
        await page.get_by_label("AV1").first.check()
        await page.get_by_label("AV2").first.check()
        await page.get_by_role("button", name="Mostrar/ocultar(Clique para").nth(1).hover()
        await page.get_by_role("menuitem", name="Ocultar colunas selecionadas", exact=True).click()
        await page.get_by_role("button", name="Enviar").click()
        await page.wait_for_load_state('load')
        print('Sala Ajustada com sucesso')