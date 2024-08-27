from playwright.async_api import Page, expect

async def AjusteNotaZero(page: Page, id_interno: str) -> None:
    """
    Function that uncheck the 'Nota Zero Automática' item in the grades options
    of the classroom.

    Args:
        page (Page): Page constructor form Playwright that
        you want this Function to run
        id_interno (str): internal ID of the classroom
    """
    # baseURL = "https://sereduc.blackboard.com/"
    classURL = f'./ultra/courses/'
    ContentURL = f'{classURL}{id_interno}/outline'
    GradeURL = f'{classURL}{id_interno}/grades?gradebookView=list&listViewType=assignments'

    print('Starting adjustments: "Nota Zero"')
    await page.goto(GradeURL)
    print('Opening config...')
    await page.get_by_label("Configurações", exact=True).click()
    await page.wait_for_load_state('load')
    print('Opening "Nota Zero"...')
    await expect(page.get_by_text('Atribuição automática da nota zero')).to_be_visible(timeout=1000*10)
    
    if await page.get_by_text("Atribui nota zero").is_checked():
        print('Atribui nota zero is checked...')
        await page.get_by_text("Atribui nota zero").click()
        print('Removing...')
        await page.get_by_text("Remover notas zero atribuídas").click()
        print('Saving...')
        await page.get_by_role("button", name="Confirmar").click()
        await page.locator("#main-content > div:nth-child(4)").click()
        await page.goto(ContentURL)
    else:
        print('Nota zero already unchecked!')
        pass