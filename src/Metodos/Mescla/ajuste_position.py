from playwright.sync_api import Page

async def ajusteGradebook(
    page: Page,
    id_interno: str,
    item_list = [
        'AV1',
        'AV2',
        'AF']) -> None:
    
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
    
    order_list: dict[str, dict[str, any]] = {
        'Nota Geral':{
            'position': 6,
            'exist': True},
        'Nota Atual': {
            'position': 6,
            'exist': True},
        'AV1': {
            'position': 7,
            'categoria': 'Assignment.name',
            'exist': True}, # .gradebookCategory.title | Assignment.name / Test.name
        'AV1': {
            'position': 8,
            'categoria': 'CUSTOM',
            'exist': True}, # Calculada | .calculationType
        'Atividade Prática': {
            'position': 9,
            'categoria': 'Exercício',
            'exist': True},
        'AV2': {
            'position': 10,
            'categoria': 'Test.name',
            'exist': True},
        'AF': {
            'position': 11,
            'categoria': 'Test.name',
            'exist': True},
        'Avaliação Final': {
            'position': 12,
            'categoria': 'Test.name',
            'exist': True},
        'AV2': {
            'position': 13,
            'categoria': 'CUSTOM',
            'exist': True},
        'AF': {
            'position': 14,
            'categoria': 'CUSTOM',
            'exist': True},
        'Atividade de Autoaprendizagem 1': {
            'position': 15,
            'categoria': 'Test.name',
            'exist': True},
        'Atividade de Autoaprendizagem 2': {
            'position': 16,
            'categoria': 'Test.name',
            'exist': True},
        'Atividade de Autoaprendizagem 3': {
            'position': 17,
            'categoria': 'Test.name',
            'exist': True},
        'Atividade de Autoaprendizagem 4': {
            'position': 18,
            'categoria': 'Test.name',
            'exist': True}
    }
    
    def request(item: str):return f'JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}" && item.visibleInBook == false).position'
    # def request_item(item: str):return f'JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}").position'
    def request_not_hidden(item: str):return f'JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}" && item.visibleInBook == true).position'
    def request_last_item(length: str):return f'JSON.parse(document.body.innerText).results[{length-1}].position'
    
    async def drag_loop(page: Page, position_list: list):
        for i, p in enumerate(position_list):
            try:
                await page.locator(f'#item_{p} > td.dragCell > span').drag_to(
                    target=page.locator(f"[id=\"item_{(position_list[i-1] if i-1 >= 0 else last)}\\.layoutCheckBox\"]"),
                    target_position = {'x': 0, 'y': 13},
                    timeout=3*1000
                    )
                print(f'{item_list[i]}: arrastado com sucesso !')
            except Exception as e:
                #  (posição do item maior do que o boletim de notar ??????????)
                print(f'{item_list[i]} error: {e} | item position not found, move all the items in the gradebook')
    
    req_length = 'JSON.parse(document.body.innerText).results.length'
    
    await page.goto(api, wait_until='networkidle')
    position = []
    position_nothidden = []
    length = await page.evaluate(req_length)
    last = await page.evaluate(request_last_item(length))
    
    for i in item_list:
        try:
            position.append(await page.evaluate(request(i)))
            print(f'{i} item já oculto')
        except:
            try:
                position_nothidden.append(await page.evaluate(request_not_hidden(i)))
                print(f'{i} item não está oculto')
            except:
                print(f'item: {i} não encontrado')
    
    await page.goto(url_edit, wait_until='domcontentloaded')
    await page.get_by_role("button", name="Gerenciar").hover()
    await page.get_by_role("menuitem", name="Organização das colunas").click()
    
    if len(position) > 0:
        drag_loop(page, position)
                
    if len(position_nothidden) > 0:
        drag_loop(page, position_nothidden)
    
    await page.get_by_role("button", name="Enviar").click()
    await page.wait_for_load_state('load')