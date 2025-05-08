from playwright.async_api import Page
import json

async def ajusteGradebook(page: Page, id_interno: str) -> None:
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    
    url_mescla = f'/learn/api/public/v3/courses/{id_interno}'
    await page.goto(url_mescla, wait_until='domcontentloaded')
    isMescla = await page.evaluate('JSON.parse(document.body.innerText).hasChildren')
    
    
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

    async def drag_loop(page: Page, extracted_dict: dict, target_name, source_name):
        await page.goto(url_edit, wait_until='domcontentloaded')
        await page.wait_for_timeout(1.5*1000)
        await page.get_by_role("button", name="Gerenciar").hover()
        await page.wait_for_timeout(1.5*1000)
        await page.get_by_role("menuitem", name="Organização das colunas").click()
        await page.wait_for_load_state('load')
        
        # EU VOU CORRINGAR NESSA POHA PQP
        if source_name == 'attendance':
            source_name = target_name
            target_name = 'attendance'
            
        try:
            source_pos = extracted_dict[source_name]
            target_pos = extracted_dict.get(target_name)
            if target_pos is None:
                target_pos = 0  # Move para o topo da lista

            await page.locator(f'#item_{source_pos} > td.dragCell > span').drag_to(
                target=page.locator(f"#item_{target_pos} > td.dragCell > span"),
                target_position={'x': 0, 'y': 33},
                timeout=3 * 1000,
                force=True
            )

            await page.wait_for_timeout(2 * 1000)
            await page.wait_for_load_state('domcontentloaded')
            await page.wait_for_load_state('load')
            await page.get_by_role("button", name="Enviar").click()
            await page.wait_for_load_state('load')
            print(f'{source_name}: arrastado com sucesso!')
        except Exception as e:
            print(f'{source_name} erro: {e} | item não encontrado.')

    # def encontrar_target(name_atual, order_list, extracted_dict, diff_items):
    #     sorted_items = sorted(order_list.items(), key=lambda x: x[1])
    #     idx_atual = next((i for i, (name, _) in enumerate(sorted_items) if name == name_atual), None)

    #     if idx_atual is None:
    #         return None

    #     for i in range(idx_atual - 1, -1, -1):
    #         nome_anterior = sorted_items[i][0]
    #         if nome_anterior in extracted_dict and nome_anterior not in diff_items:
    #             return nome_anterior
    #     return None
    
    def encontrar_target(name_atual, order_list, extracted_dict, diff_items):
        # Regra especial: se for 'attendance', usar 'nota geral' como target
        if name_atual == 'attendance' and 'nota geral' in extracted_dict:
            return 'nota geral'

        sorted_items = sorted(order_list.items(), key=lambda x: x[1])
        idx_atual = next((i for i, (name, _) in enumerate(sorted_items) if name == name_atual), None)

        if idx_atual is None:
            return None

        # Procura por um item anterior que esteja em ordem
        for i in range(idx_atual - 1, -1, -1):
            nome_anterior = sorted_items[i][0]
            if nome_anterior in extracted_dict and nome_anterior not in diff_items:
                return nome_anterior

        # Se não achar ninguém antes, tenta achar o PRÓXIMO em ordem
        for i in range(idx_atual + 1, len(sorted_items)):
            nome_proximo = sorted_items[i][0]
            if nome_proximo in extracted_dict and nome_proximo not in diff_items:
                return nome_proximo

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
        
        if str(isMescla).lower == 'true':
            if 'attendance' in extracted_dict and 'atividade prática' in extracted_dict:
                order_list = {
                    'attendance': 8,
                    'nota geral': 9,
                    'pesquisa de satisfação': 10,
                    'atividade prática': 11,
                    'exercício de fixação 01': 12,
                    'exercício de fixação 02': 13,
                    'exercício de fixação 03': 14,
                    'avaliação workshop': 15,
                    'exercício do conhecimento': 16,
                    'avaliação discursiva': 17,
                    'av1': 18,
                    'avaliação objetiva': 19,
                    'av2': 20,
                    'nota final': 21,
                    'nota final - espelho': 22,
                    'exame final': 23,
                    'af': 24,
                    'af - espelho': 25,
                    'nota final com exame': 26
                    }
            elif 'attendance' in extracted_dict:
                order_list = {
                'attendance': 8,
                'nota geral': 9,
                'pesquisa de satisfação': 10,
                'exercício de fixação 01': 11,
                'exercício de fixação 02': 12,
                'exercício de fixação 03': 13,
                'avaliação workshop': 14,
                'exercício do conhecimento': 15,
                'avaliação discursiva': 16,
                'av1': 17,
                'avaliação objetiva': 18,
                'av2': 19,
                'nota final': 20,
                'nota final - espelho': 21,
                'exame final': 22,
                'af': 23,
                'af - espelho': 24,
                'nota final com exame': 25
                }
            elif 'atividade prática' in extracted_dict:
                order_list = {
                'nota geral': 8,
                'pesquisa de satisfação': 9,
                'atividades prática': 10,
                'exercício de fixação 01': 11,
                'exercício de fixação 02': 12,
                'exercício de fixação 03': 13,
                'avaliação workshop': 14,
                'exercício do conhecimento': 15,
                'avaliação discursiva': 16,
                'av1': 17,
                'avaliação objetiva': 18,
                'av2': 19,
                'nota final': 20,
                'nota final - espelho': 21,
                'exame final': 22,
                'af': 23,
                'af - espelho': 24,
                'nota final com exame': 25
                }
            else:
                order_list = {
                'nota geral': 8,
                'pesquisa de satisfação': 9,
                'exercício de fixação 01': 10,
                'exercício de fixação 02': 11,
                'exercício de fixação 03': 12,
                'avaliação workshop': 13,
                'exercício do conhecimento': 14,
                'avaliação discursiva': 15,
                'av1': 16,
                'avaliação objetiva': 17,
                'av2': 18,
                'nota final': 19,
                'nota final - espelho': 20,
                'exame final': 21,
                'af': 22,
                'af - espelho': 23,
                'nota final com exame': 24
                }
        else:
            if 'attendance' in extracted_dict and 'atividade prática' in extracted_dict:
                order_list = {
                    'attendance': 6,
                    'nota geral': 7,
                    'pesquisa de satisfação': 8,
                    'atividade prática': 9,
                    'exercício de fixação 01': 10,
                    'exercício de fixação 02': 11,
                    'exercício de fixação 03': 12,
                    'avaliação workshop': 13,
                    'exercício do conhecimento': 14,
                    'avaliação discursiva': 15,
                    'av1': 16,
                    'avaliação objetiva': 17,
                    'av2': 18,
                    'nota final': 19,
                    'nota final - espelho': 20,
                    'exame final': 21,
                    'af': 22,
                    'af - espelho': 23,
                    'nota final com exame': 24
                    }
            elif 'attendance' in extracted_dict:
                order_list = {
                'attendance': 6,
                'nota geral': 7,
                'pesquisa de satisfação': 8,
                'exercício de fixação 01': 9,
                'exercício de fixação 02': 10,
                'exercício de fixação 03': 11,
                'avaliação workshop': 12,
                'exercício do conhecimento': 13,
                'avaliação discursiva': 14,
                'av1': 15,
                'avaliação objetiva': 16,
                'av2': 17,
                'nota final': 18,
                'nota final - espelho': 19,
                'exame final': 20,
                'af': 21,
                'af - espelho': 22,
                'nota final com exame': 23
                }
            elif 'atividade prática' in extracted_dict:
                order_list = {
                'nota geral': 6,
                'pesquisa de satisfação': 7,
                'atividade prática': 8,
                'exercício de fixação 01': 9,
                'exercício de fixação 02': 10,
                'exercício de fixação 03': 11,
                'avaliação workshop': 12,
                'exercício do conhecimento': 13,
                'avaliação discursiva': 14,
                'av1': 15,
                'avaliação objetiva': 16,
                'av2': 17,
                'nota final': 18,
                'nota final - espelho': 19,
                'exame final': 20,
                'af': 21,
                'af - espelho': 22,
                'nota final com exame': 23
                }
            else:
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
                'nota final - espelho': 18,
                'exame final': 19,
                'af': 20,
                'af - espelho': 21,
                'nota final com exame': 22
                }
                
        diferencas = {
        name: extracted_dict[name]
        for name, pos in order_list.items()
        if name in extracted_dict and extracted_dict[name] != pos
        }

        if not diferencas:
            break  # 🎉 all in order!

        sorted_items = sorted(order_list.items(), key=lambda x: x[1])
        diff_items = [name for name, _ in sorted_items if name in extracted_dict and extracted_dict[name] != order_list[name]]
        
        # test = diff_items[1] if diff_items[0] == 'nota geral' else diff_items[0]
        name = diff_items[0]
        target_name = encontrar_target(name, order_list, extracted_dict, diff_items)
        await drag_loop(page, extracted_dict, target_name, name)

    print("\n✅ Todos os valores estão em ordem!")