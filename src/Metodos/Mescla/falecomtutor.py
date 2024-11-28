from playwright.async_api import Page, expect
from Metodos import getApiContent

async def falecomtutor(page: Page, id_interno: str) -> None:
    
    item = 'Fale com o Tutor'
    id_fct = await getApiContent.API_Req_Content(page, id_interno, item)
    classurl = f'./ultra/courses/{id_interno}/outline?search={item}'
    await page.goto(classurl)
    await page.wait_for_load_state('domcontentloaded')
    await page.locator("div").filter(has_text="Fale com o Tutor").first.click()
    await page.get_by_label("Mais opções", exact=True).click()
    await page.locator(f"#prompt-field{id_fct}_draw").click()
    await page.locator("#bb-editor-textbox").press("ControlOrMeta+a")
    await page.locator("#bb-editor-textbox").fill("Olá estudante!\nEsse canal é seu espaço pessoal para se comunicar reservadamente com o professor da disciplina. Fique a vontade para deixar aqui aquele recado que não quer tonar público!\nAté Breve!")
    await page.get_by_role("button", name="Salvar").click()