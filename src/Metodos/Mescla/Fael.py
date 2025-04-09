from playwright.async_api import Page
import json

async def ajusteGradebook(page: Page, id_interno: str) -> None:
    
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
    # atualizar a tabela da posição na API
    await page.goto(url_edit, wait_until='domcontentloaded')
    await page.get_by_role("button", name="Gerenciar").hover()
    await page.get_by_role("menuitem", name="Organização das colunas").click()
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('load')
    await page.get_by_role("button", name="Enviar").click()
    await page.wait_for_load_state('load')
    
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    await page.goto(api, wait_until='networkidle')

    # Código para extrair as colunas e comparar
    order_list = {
    'nota geral': 6,
    'pesquisa de satisfação': 7,
    'exercício de fixação 01': 8,
    'exercício de fixação 02': 9,
    'exercício de fixação 03': 10,
    'avaliação workshop': 11,
    'exercício do conhecimento': 12,
    'avaliação discursiva': 13,
    'av1': 14,
    'avaliação objetiva': 15,
    'av2': 16,
    'nota final': 17,
    'nota final - Espelho': 18,
    'exame final': 19,
    'af': 20,
    'af - Espelho': 21,
    'nota final com exame': 22
    }
    
    extract_js = """
    JSON.parse(document.body.innerText).results.map(item => ({
        columnName: item.columnName,
        position: item.position
    }))
    """
    extracted_data = await page.evaluate(extract_js)
    def request_last_item(length: str):return f'JSON.parse(document.body.innerText).results[{length-1}].position'
    req_length = 'JSON.parse(document.body.innerText).results.length'
    length = await page.evaluate(req_length)
    last = await page.evaluate(request_last_item(length))

    extracted_dict = {str(item["columnName"]).lower(): item["position"] for item in extracted_data}
    diferencas = {col: extracted_dict[col] for col in extracted_dict if col in order_list and extracted_dict[col] != order_list[col]}
    
    async def drag_loop(page: Page, id_interno: str, extracted_dict: dict, order_list: dict, _last):
        url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
        await page.goto(url_edit, wait_until='domcontentloaded')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        await page.wait_for_load_state('load')

        # Organize os nomes com base na ordem desejada
        sorted_items = sorted(order_list.items(), key=lambda x: x[1])

        # Cria lista dos nomes que estão com posição diferente
        diff_items = [name for name, _ in sorted_items if name in extracted_dict and extracted_dict[name] != order_list[name]]
        
        def encontrar_target(name_atual, order_list, extracted_dict, diff_items):
            sorted_items = sorted(order_list.items(), key=lambda x: x[1])
            idx_atual = next((i for i, (name, _) in enumerate(sorted_items) if name == name_atual), None)

            if idx_atual is None:
                return None  # não encontrou o item na ordem esperada

            # Buscar para trás por um item que esteja na posição correta
            for i in range(idx_atual - 1, -1, -1):
                nome_anterior = sorted_items[i][0]
                if nome_anterior in extracted_dict and nome_anterior not in diff_items:
                    return nome_anterior  # encontrado item anterior corretamente posicionado

            return None  # não encontrou nenhum item anterior correto

        for i, name in enumerate(diff_items):
            try:
                source_pos = extracted_dict[name]
                target_name = encontrar_target(name, order_list, extracted_dict, diff_items)
                target_pos = extracted_dict[target_name] if target_name else _last
                await page.locator(f'#item_{source_pos} > td.dragCell > span').drag_to(
                    target=page.locator(f"#item_{target_pos} > td.dragCell > span"),
                    target_position={'x': 0, 'y': 23},
                    timeout=3 * 1000,
                    force=True
                )
                await page.wait_for_timeout(1.5*1000)
                await page.wait_for_load_state('domcontentloaded')
                await page.wait_for_load_state('load')
                await page.get_by_role("button", name="Enviar").click()
                await page.wait_for_load_state('load')
                print(f'{name}: arrastado com sucesso!')
            except Exception as e:
                print(f'{name} erro: {e} | item não encontrado.')
    
    
    if len(diferencas) > 0:
        await drag_loop(page, id_interno, extracted_dict, order_list, last)

    print("\n### Dados Extraídos ###")
    print(json.dumps(extracted_dict, indent=2))

    if diferencas:
        print("\n### Diferenças Encontradas ###")
        print(json.dumps(diferencas, indent=2))
    else:
        print("\nTodos os valores correspondem à lista predefinida.")
        
################################################################################
from playwright.async_api import Page
import json

async def ajusteGradebook(page: Page, id_interno: str) -> None:
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'

    order_list = {
        'nota geral': 6,
        'pesquisa de satisfação': 7,
        'exercício de fixação 01': 8,
        'exercício de fixação 02': 9,
        'exercício de fixação 03': 10,
        'avaliação workshop': 11,
        'exercício do conhecimento': 12,
        'avaliação discursiva': 13,
        'av1': 14,
        'avaliação objetiva': 15,
        'av2': 16,
        'nota final': 17,
        'nota final - Espelho': 18,
        'exame final': 19,
        'af': 20,
        'af - Espelho': 21,
        'nota final com exame': 22
    }

    async def get_column_state():
        await page.goto(api, wait_until='networkidle')
        extract_js = """
        JSON.parse(document.body.innerText).results.map(item => ({
            columnName: item.columnName,
            position: item.position
        }))
        """
        extracted_data = await page.evaluate(extract_js)
        extracted_dict = {str(item["columnName"]).lower(): item["position"] for item in extracted_data}
        req_length = 'JSON.parse(document.body.innerText).results.length'
        length = await page.evaluate(req_length)
        last = await page.evaluate(f'JSON.parse(document.body.innerText).results[{length - 1}].position')
        return extracted_dict, last

    async def drag_loop(page: Page, id_interno: str, extracted_dict: dict, order_list: dict, _last, target_name, source_name):
        await page.goto(url_edit, wait_until='domcontentloaded')
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        await page.wait_for_load_state('load')

        try:
            source_pos = extracted_dict[source_name]
            target_pos = extracted_dict.get(target_name, _last)

            await page.locator(f'#item_{source_pos} > td.dragCell > span').drag_to(
                target=page.locator(f"#item_{target_pos} > td.dragCell > span"),
                target_position={'x': 0, 'y': 23},
                timeout=3 * 1000,
                force=True
            )

            await page.wait_for_timeout(1.5 * 1000)
            await page.wait_for_load_state('domcontentloaded')
            await page.wait_for_load_state('load')
            await page.get_by_role("button", name="Enviar").click()
            await page.wait_for_load_state('load')
            print(f'{source_name}: arrastado com sucesso!')
        except Exception as e:
            print(f'{source_name} erro: {e} | item não encontrado.')

    def encontrar_target(name_atual, order_list, extracted_dict, diff_items):
        sorted_items = sorted(order_list.items(), key=lambda x: x[1])
        idx_atual = next((i for i, (name, _) in enumerate(sorted_items) if name == name_atual), None)

        if idx_atual is None:
            return None

        for i in range(idx_atual - 1, -1, -1):
            nome_anterior = sorted_items[i][0]
            if nome_anterior in extracted_dict and nome_anterior not in diff_items:
                return nome_anterior
        return None

    # Initial save to ensure columns can be dragged
    await page.goto(url_edit, wait_until='domcontentloaded')
    await page.get_by_role("button", name="Gerenciar").hover()
    await page.get_by_role("menuitem", name="Organização das colunas").click()
    await page.wait_for_load_state('load')
    await page.get_by_role("button", name="Enviar").click()
    await page.wait_for_load_state('load')

    # 🔁 Loop until all differences are resolved
    while True:
        extracted_dict, last = await get_column_state()
        diferencas = {col: extracted_dict[col] for col in extracted_dict if col in order_list and extracted_dict[col] != order_list[col]}

        if not diferencas:
            break  # 🎉 all in order!

        sorted_items = sorted(order_list.items(), key=lambda x: x[1])
        diff_items = [name for name, _ in sorted_items if name in extracted_dict and extracted_dict[name] != order_list[name]]

        name = diff_items[0]
        target_name = encontrar_target(name, order_list, extracted_dict, diff_items)
        await drag_loop(page, id_interno, extracted_dict, order_list, last, target_name, name)

    print("\n✅ Todos os valores estão em ordem!")
