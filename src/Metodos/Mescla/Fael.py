from playwright.async_api import async_playwright, Page
import json, os

async def ajusteGradebook(page: Page, id_interno: str) -> None:
    # Agora usa o base_url diretamente do contexto do decorator
    base_url = os.getenv('BASE_URL')  # Ou, se o decorator já passar, use conforme necessário
    api = f'{base_url}/learn/api/v1/courses/{id_interno}/gradebook/columns'
    await page.goto(api, wait_until='networkidle')

    # Código para extrair as colunas e comparar
    order_list = {
    'Attendance': 3,
    'Nota geral': 4,
    'Pesquisa de Satisfação': 6,
    'Exercício de Fixação 01': 7,
    'Exercício de Fixação 02': 8,
    'Exercício de Fixação 03': 9,
    'Avaliação Workshop': 10,
    'Exercício do Conhecimento': 11,
    'Avaliação Discursiva': 12,
    'AV1': 13,
    'Avaliação Objetiva': 14,
    'AV2': 16,
    'Nota Final': 17,
    'Nota Final - Espelho': 18,
    'Exame Final': 20,
    'AF': 21,
    'AF - Espelho': 22,
    'Nota Final com Exame': 23
    }
    extract_js = """
    JSON.parse(document.body.innerText).results.map(item => ({
        columnName: item.columnName,
        position: item.position
    }))
    """
    extracted_data = await page.evaluate(extract_js)

    extracted_dict = {item["columnName"]: item["position"] for item in extracted_data}
    diferencas = {col: extracted_dict[col] for col in extracted_dict if col in order_list and extracted_dict[col] != order_list[col]}

    print("\n### Dados Extraídos ###")
    print(json.dumps(extracted_dict, indent=2))

    if diferencas:
        print("\n### Diferenças Encontradas ###")
        print(json.dumps(diferencas, indent=2))
    else:
        print("\nTodos os valores correspondem à lista predefinida.")