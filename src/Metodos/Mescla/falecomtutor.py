from playwright.async_api import Page, expect
from Metodos import getApiContent

async def falecomtutor(page: Page, id_interno: str) -> None:
    
    item = 'Fale com o Tutor'
    id_fct = await getApiContent.API_Req_Content(page, id_interno, item)
    classurl = f'./ultra/courses/{id_interno}/outline?search={item}'
    await page.goto(classurl)
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_timeout(1000*6)
    await page.locator("div").filter(has_text="Fale com o Tutor").first.click()
    await page.get_by_label("Mais opções", exact=True).click()
    await page.locator(f"#prompt-field{id_fct}_draw").click()
    await page.locator("#bb-editor-textbox").press("ControlOrMeta+a")
    await page.locator("#bb-editor-textbox").fill("Olá estudante!\nEsse canal é seu espaço pessoal para se comunicar reservadamente com o tutor da disciplina. Fique a vontade para deixar aqui aquele recado que não quer tonar público!\nAté Breve!")
    await page.get_by_role("button", name="Salvar").click()
    
async def falecomtutor_prof(page: Page, id_interno: str) -> None:
    # https://sereduc.blackboard.com/webapps/blackboard/execute/courseMain?course_id=_113431_1
    item = 'Fale com o Professor'
    id_fct = await getApiContent.API_Req_Content(page, id_interno, item)
    classurl = f'./ultra/courses/{id_interno}/outline?search={item}'
    await page.goto(classurl)
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_timeout(1000*6)
    if await page.get_by_role("heading", name="Nenhum resultado encontrado").is_visible(timeout=3*1000):
        item = 'Fale com o Tutor'
        id_fct = await getApiContent.API_Req_Content(page, id_interno, item)
        classurl = f'./ultra/courses/{id_interno}/outline?search={item}'
        await page.goto(classurl)
        await page.wait_for_load_state('domcontentloaded')
        await page.wait_for_timeout(1000*6)
        # await page.locator("div").filter(has_text="Fale com o Tutor").first.click()
        await page.get_by_role("link", name="Fale com o Tutor").click()
        await page.get_by_role("button", name="Editar Fale com o Tutor").click()
        await page.get_by_role("textbox", name="Novo diário undefined").press("ControlOrMeta+a")
        item = 'Fale com o Professor'
        await page.get_by_role("textbox", name="Novo diário undefined").fill(item)
        await page.get_by_role("textbox", name="Novo diário undefined").press("Enter")
        await page.get_by_label("Mais opções", exact=True).click()
        await page.locator(f"#prompt-field{id_fct}_draw").click()
        await page.locator("#bb-editor-textbox").press("ControlOrMeta+a")
        await page.locator("#bb-editor-textbox").fill("Olá estudante!\nEsse canal é seu espaço pessoal para se comunicar reservadamente com o professor da disciplina. Fique a vontade para deixar aqui aquele recado que não quer tonar público!\nAté Breve!")
        await page.get_by_role("button", name="Salvar").click()
    else:
        print(f'{item} found')
        pass