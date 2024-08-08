from playwright.sync_api import Page


async def open_Mescla(page: Page, id_interno: str) -> None:
    # baseURL = 'https://sereduc.blackboard.com/'
    url_edit = f'./webapps/blackboard/execute/editCourseManager?sourceType=COURSES&context=MODIFY&course_id={id_interno}'
    await page.goto(url=url_edit, wait_until='commit')
    await page.wait_for_load_state('domcontentloaded')
    await page.get_by_label("Usar disponibilidade de termo").check()
    await page.get_by_label("Usar definição de termo (").check()
    await page.get_by_role("button", name="Enviar")
    await page.wait_for_load_state('load')
    await page.wait_for_load_state('networkidle')