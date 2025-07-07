from playwright.async_api import Page


async def expurgo (page: Page, id_user: str, id_interno: str) -> None:
    
    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_role("link", name="Participantes Visualizar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_role("button", name="Nome ou Sobrenome").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_placeholder("Nome ou Sobrenome").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    # await page.get_by_placeholder("Nome ou Sobrenome").fill("dhiego.moura")
    await page.get_by_placeholder("Nome ou Sobrenome").fill(id_user)
    await page.wait_for_load_state('load')
    await page.wait_for_load_state('domcontentloaded')
    await page.press('body', 'Enter')
    await page.press('#search-roster-field', 'Enter')
    await page.get_by_placeholder("Nome ou Sobrenome").press("Enter")
    try:
        await page.locator('#rosterView-list > ul > li > div > div.medium-5.columns > div > div').click(timeout=3*1000)
        await page.wait_for_load_state('load')
        await page.locator('#roster-settings > ng-form > div.nested-panel > div > div > div.element-card.account > button').click()
        await page.locator('body > div.panel-has-focus > div > footer > div > div.reveal-modal__footer-buttons > span:nth-child(2) > button').click()
        await page.wait_for_load_state('load')
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(1500)
    except Exception as e:
        await page.locator('#rosterView-grid > ul > li > div > a > bb-username > bb-ui-username > div > div').click(timeout=3*1000)
        await page.wait_for_load_state('load')
        await page.locator('#roster-settings > ng-form > div.nested-panel > div > div > div.element-card.account > button').click()
        await page.locator('body > div.panel-has-focus > div > footer > div > div.reveal-modal__footer-buttons > span:nth-child(2) > button').click()
        await page.wait_for_load_state('load')
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(1500)
    # await page.wait_for_load_state('load')
    # await page.wait_for_timeout(2*1000)
    # await page.get_by_label("Remover membro").click()
    # await page.wait_for_load_state('load')
    # await page.wait_for_timeout(2*1000)
    # await page.get_by_role("button", name="Remover membro").click()

async def expurgo_root (page: Page, id_user: str, id_interno: str) -> None:
    
    await page.goto(f'./webapps/blackboard/execute/courseEnrollment?sourceType=COURSES&showAll=true&course_id={id_interno}')
    await page.wait_for_load_state('load')
    try:
        print(f'Deleting {id_user} in {id_interno}...')
        await page.get_by_label(f"Selecionar {id_user}").check()
        page.once("dialog", lambda dialog: dialog.accept())
        await page.locator("#listContainer_nav_batch_top").get_by_role("button", name="Remover usuários do curso").click()
        await page.wait_for_load_state('load')
        await page.get_by_text("Sucesso: Inscrição excluída.").wait_for(state='visible', timeout=5*1000)
        print(f'Deleted {id_user} in {id_interno}')
        # await page.pause()
    except:
        print(f'not found {id_user} in {id_interno} classroom.')
        ...
    
async def expurgo_root_lote (page: Page, id_user: list, id_interno: str) -> None:
    
    await page.goto(f'./webapps/blackboard/execute/courseEnrollment?sourceType=COURSES&showAll=true&course_id={id_interno}')
    await page.wait_for_load_state('load')
    try:
        for _i in id_user:
            try:
                await page.get_by_label(f"Selecionar {_i}").check(timeout=10*1000)
                print(f'{_i} found and selected')
            except:
                print(f'{_i} not found in {id_interno} classroom.')
            
        page.once("dialog", lambda dialog: dialog.accept())
        await page.locator("#listContainer_nav_batch_top").get_by_role("button", name="Remover usuários do curso").click()
        await page.wait_for_load_state('load')
        await page.get_by_text("Sucesso: Inscrição excluída.").wait_for(state='visible', timeout=5*1000)
        print(f'All users deleted from {id_interno}')
        print(f'User list: {id_user}')
        # await page.pause()
    except:
        ...