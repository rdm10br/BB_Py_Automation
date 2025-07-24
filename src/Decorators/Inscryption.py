from playwright.async_api import Page
from async_lru import alru_cache
from functools import lru_cache
from Metodos import getFromAPI

@alru_cache(maxsize=128)
async def Auto_Sub(page: Page, index: int):
    """
    Realiza a inscrição automática do usuário autenticado em um curso específico.

    Este método utiliza a API interna para obter o identificador do curso, acessa a página de inscrição,
    preenche o formulário com o usuário autenticado e seleciona o papel 'adsala', submetendo a inscrição.

    Args:
        page (Page): Instância da página Playwright já autenticada.
        index (int): Índice da linha/curso a ser processado.

    Returns:
        None
    """
    # Obtém o ID interno do curso via API personalizada.
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    # Monta a URL de inscrição do curso e a URL para obter o usuário autenticado.
    # rootURL = f'./webapps/blackboard/execute/recycler?course_id={id_interno}&action=select&context=COURSE#'
    inscryption = f'./webapps/blackboard/execute/editCourseEnrollment?course_id={id_interno}&sourceType=COURSES'
    API_User = f'./learn/api/public/v1/users/me'
    
    # Obtém o nome de usuário autenticado via API.
    await page.goto(API_User, wait_until='commit')
    await page.wait_for_load_state('load')
    user = await page.evaluate('JSON.parse(document.body.innerText).userName')
    
    # Acessa a página de inscrição do curso.
    await page.goto(url=inscryption, wait_until='commit')
    
    # Preenche o formulário de inscrição com o usuário e papel desejado.
    await page.locator('#userName').fill(user)
    await page.locator('#courseRoleId').select_option('adsala')
    await page.locator('#bottom_Submit').click()
    await page.wait_for_load_state('load')
    

@alru_cache(maxsize=128)
async def Auto_Unsub(page: Page, index: int, showAll: bool = False):
    """
    Remove automaticamente o usuário autenticado de um curso específico.

    Este método utiliza a API interna para obter o identificador do curso, acessa a página de gerenciamento de inscrições,
    localiza o usuário autenticado e executa a remoção da inscrição, tratando possíveis exceções caso o usuário não seja encontrado.

    Args:
        page (Page): Instância da página Playwright já autenticada.
        index (int): Índice da linha/curso a ser processado.

    Returns:
        None
    """
    # Obtém o ID interno do curso via API personalizada.
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    
    # rootURL = f'./webapps/blackboard/execute/recycler?course_id='\
    #     f'{id_interno}&action=select&context=COURSE#'
    # offset = 9999
    
    # verify if the user shows up if not verify pagination
    # inscryption = f'./webapps/blackboard/execute/courseEnrollment?'\
    #     f'sortCol=userrole&sourceType=COURSES&numResults={offset}&course_id='\
    #     f'{id_interno}&sortDir=DESCENDING'
    
    classUrlUltra = f'./ultra/courses/{id_interno}/outline'
    API_User = f'./learn/api/public/v1/users/me'
    
    # Obtém o nome de usuário autenticado via API.
    await page.goto(API_User, wait_until='commit')
    await page.wait_for_load_state('load')
    user = await page.evaluate('JSON.parse(document.body.innerText).userName')
    
    # await page.goto(url=classUrlUltra, wait_until='commit')
    # await page.wait_for_load_state('load')
    # await page.locator('#course-outline-roster-link').click()
    # await page.locator('#search-button').click()
    # await page.locator('#search-roster-field').fill(user)
    # await page.wait_for_timeout(1500)
    # await page.press('body', 'Enter')
    # await page.press('#search-roster-field', 'Enter')
    # await page.get_by_placeholder("Nome ou Sobrenome").press("Enter")
    # await page.wait_for_load_state('load')
    # await page.wait_for_load_state('domcontentloaded')
    # await page.wait_for_load_state('networkidle')
    # await page.wait_for_timeout(5*1000)
    # try:
    #     await page.locator('#rosterView-list > ul > li > div > div.medium-5.columns > div > div').click(timeout=3*1000)
    #     await page.wait_for_load_state('load')
    #     await page.locator('#roster-settings > ng-form > div.nested-panel > div > div > div.element-card.account > button').click()
    #     await page.locator('body > div.panel-has-focus > div > footer > div > div.reveal-modal__footer-buttons > span:nth-child(2) > button').click()
    #     await page.wait_for_load_state('load')
    #     await page.wait_for_load_state('domcontentloaded')
    #     await page.wait_for_load_state('networkidle')
    #     await page.wait_for_timeout(1500)
    # except Exception as e:
    #     await page.locator('#rosterView-grid > ul > li > div > a > bb-username > bb-ui-username > div > div').click(timeout=3*1000)
    #     await page.wait_for_load_state('load')
    #     await page.locator('#roster-settings > ng-form > div.nested-panel > div > div > div.element-card.account > button').click()
    #     await page.locator('body > div.panel-has-focus > div > footer > div > div.reveal-modal__footer-buttons > span:nth-child(2) > button').click()
    #     await page.wait_for_load_state('load')
    #     await page.wait_for_load_state('domcontentloaded')
    #     await page.wait_for_load_state('networkidle')
    #     await page.wait_for_timeout(1500)
    
    # await page.goto(f'./webapps/blackboard/execute/courseEnrollment?sourceType=COURSES&showAll=true&course_id={id_interno}')
    if showAll:
        await page.goto(url=f'./webapps/blackboard/execute/courseEnrollment?sourceType=COURSES&showAll=true&course_id={id_interno}', timeout=60*1000)
    else:
        await page.goto(url=f'./webapps/blackboard/execute/courseEnrollment?sourceType=COURSES&sortCol=userrole&sortDir=ASCENDING&numResults=250&course_id={id_interno}', timeout=60*1000)
    await page.wait_for_load_state('load')
    try:
        print(f'Deleting {user} in {id_interno}...')
        await page.get_by_label(f"Selecionar {user}").check()
        page.once("dialog", lambda dialog: dialog.accept())
        await page.locator("#listContainer_nav_batch_top").get_by_role("button", name="Remover usuários do curso").click()
        await page.wait_for_load_state('load')
        await page.get_by_text("Sucesso: Inscrição excluída.").wait_for(state='visible', timeout=5*1000)
        print(f'Deleted {user} in {id_interno}')
        # await page.pause()
    except:
        print(f'not found {user} in {id_interno} classroom.')
        ...