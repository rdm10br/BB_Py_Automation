from playwright.async_api import Page


async def AV2_Hide(page: Page, id_interno: str) -> None:
    # baseURL = 'https://sereduc.blackboard.com/'
    urlGradeBook = f'./ultra/courses/{id_interno}/grades?gradebookView=list'
    timer_padrão = 1000*2
    
    await page.goto(url=urlGradeBook, wait_until='commit')
    await page.wait_for_load_state('networkidle')
    await page.wait_for_load_state('domcontentloaded')
    await page.get_by_role("link", name="AV2").click()
    await page.get_by_role("button", name="Visível para alunos").click()
    await page.get_by_role("menuitem", name="Oculto para alunos").click()
    await page.wait_for_load_state('networkidle')
    await page.wait_for_timeout(timer_padrão)
    
    return 'OK'

