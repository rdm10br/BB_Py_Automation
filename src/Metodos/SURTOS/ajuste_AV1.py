from playwright.async_api import Page
# from Metodos import getPlanilha


async def verify_calculated(page: Page, id_interno: str):
    baseURL = 'https://sereduc.blackboard.com/'
    api = f'{baseURL}learn/api/v1/courses/{id_interno}/gradebook/columns'
    item = 'AV1'
    request = f'''JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}").calculationType'''
    
    await page.goto(url=api, wait_until='commit')
    return await page.evaluate(request)


async def newAV1(page: Page, id_interno: str) -> None:
    baseURL = 'https://sereduc.blackboard.com/'
    urlGradeBook = f'{baseURL}ultra/courses/{id_interno}/grades?gradebookView=list'
    verify = await verify_calculated(page=page, id_interno=id_interno)
    timer_padrão = 1000*2
    
    if verify == "CUSTOM":
        result = 'AV1 is a calculated item'
        print(result)
        return result
    else:
        print('AV1 is not a Calculated item')
        await page.goto(url=urlGradeBook, wait_until='commit')
        await page.get_by_label("Adicionar nova coluna do boletim de notas acima do(a) Nota atual").click()
        await page.get_by_role("menuitem", name="Adicionar cálculo", exact=True).click()
        await page.get_by_label("Novo cálculo em undefined").fill("AV1")
        await page.get_by_text("Selecionar um esquema de notas").click()
        await page.wait_for_timeout(timer_padrão)
        await page.get_by_role("button", name="Total ").click()
        await page.wait_for_timeout(timer_padrão)
        await page.get_by_role("button", name="TOTAL ( )").click()
        await page.get_by_text("Trabalho do curso AV1").click()
        await page.locator("ul").filter(has_text="TOTAL ( Trabalho do curso AV1").click()
        await page.get_by_role("button", name="Salvar").click()
        await page.wait_for_load_state('load')
        return 'OK'
