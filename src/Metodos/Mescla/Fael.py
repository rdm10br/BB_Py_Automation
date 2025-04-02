from playwright.async_api import async_playwright, Page
import json

async def ajusteGradebook(page: Page, id_interno: str) -> None:
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    url_edit = f'./webapps/gradebook/do/instructor/enterGradeCenter?course_id={id_interno}'

    # Lista esperada de colunas e posições
    order_list = {
        'Attendance': 3,
        'Nota geral': 4,
        # 'AV1': 7,
        # 'AV2': 10,
        # 'AF': 11,
        # 'Avaliação Final': 12,
        # 'Atividade Prática': 9,
        # 'Atividade de Autoaprendizagem 1': 15,
        # 'Atividade de Autoaprendizagem 2': 16,
        # 'Atividade de Autoaprendizagem 3': 17,
        # 'Atividade de Autoaprendizagem 4': 18
    }

    # Código JavaScript para extrair o JSON
    extract_js = """
    JSON.parse(document.body.innerText).results.map(item => ({
        columnName: item.columnName,
        position: item.position
    }))
    """

    await page.goto(api, wait_until='networkidle')

    # Executa o JS para extrair os dados
    extracted_data = await page.evaluate(extract_js)

    # Comparação com a lista esperada
    extracted_dict = {item["columnName"]: item["position"] for item in extracted_data}
    diferencas = {col: extracted_dict[col] for col in extracted_dict if col in order_list and extracted_dict[col] != order_list[col]}

    # Exibe os resultados
    print("\n### Dados Extraídos ###")
    print(json.dumps(extracted_dict, indent=2))

    if diferencas:
        print("\n### Diferenças Encontradas ###")
        print(json.dumps(diferencas, indent=2))
    else:
        print("\nTodos os valores correspondem à lista predefinida.")

    # # Agora continua a lógica de interação na interface
    # await page.goto(url_edit, wait_until='domcontentloaded')
    # await page.get_by_role("button", name="Gerenciar").hover()
    # await page.get_by_role("menuitem", name="Organização das colunas").click()

    # await page.get_by_role("button", name="Enviar").click()
    # await page.wait_for_load_state('load')

# # Execução principal
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)  # Altere para True se não precisar visualizar
#         page = await browser.new_page()
#         await ajusteGradebook(page, "ID_DO_CURSO_AQUI")
#         await browser.close()

# import asyncio
# asyncio.run(main())