from playwright.async_api import Page, expect
from Metodos.BQ import getBQ as gb
import regex as re
import os
from unidecode import unidecode


async def create_bq(page: Page, path: str) -> str:
    """_summary_

    Args:
        page (Page): _description_
        path (str): _description_
    """
    file_name = os.path.basename(path)
    BQ_name = re.sub(r'.docx','',file_name).upper()
    unidade = ''.join([ch for ch in BQ_name if ch.isdigit()])
    match unidade[0]:
            case '1' :
                item = 'BQ 01'
            case '2' :
                item = 'BQ 02'
            case '3' :
                item = 'BQ 03'
            case '4' :
                item = 'BQ 04'
    BQ_name = unidecode(BQ_name)
    BQ_name = f'{BQ_name} - {item}_GRADUACAO'
    await page.get_by_role("button", name="Criar banco de testes").click()
    await page.get_by_label("Nome", exact=True).fill(BQ_name)
    await page.get_by_role("button", name="Enviar").click()
    return BQ_name
    
    
async def create_question(index: int, path: str, page: Page):
    index-=1
    enunciado = gb.get_Enunciado(index=index, path=path)
    alternativa_a = gb.get_Alternativa(index=index, path=path, choices='a')
    alternativa_b = gb.get_Alternativa(index=index, path=path, choices='b')
    alternativa_c = gb.get_Alternativa(index=index, path=path, choices='c')
    alternativa_d = gb.get_Alternativa(index=index, path=path, choices='d')
    alternativa_e = gb.get_Alternativa(index=index, path=path, choices='e')
    
    await page.get_by_role("button", name="Criar pergunta").click()
    await page.get_by_role("menuitem", name="Múltipla Escolha").click()
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('networkidle')
    await page.wait_for_load_state('load')
    try:
        await page.frame_locator("[id=\"questionText\\.text_ifr\"]").get_by_label("Área rich-text. Pressione ALT").fill(enunciado)
    except:
        pass
    await page.get_by_label("Numeração das Respostas").select_option("letter_lower")
    await page.get_by_label("Mostrar Respostas por Ordem").check()
    await page.get_by_role("radiogroup", name="Número de Respostas").get_by_label("Número de Respostas").select_option("5")
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('networkidle')
    await page.wait_for_load_state('load')
    try:
        await page.frame_locator("internal:role=row[name=\"Correta 1 Resposta a. Para\"i] >> iframe[title=\"Rich Text Area\"]").get_by_label("Área rich-text. Pressione ALT").fill(alternativa_a)
    except:
        pass
    try:
        await page.frame_locator("internal:role=row[name=\"Correta 2 Resposta b. Para\"i] >> iframe[title=\"Rich Text Area\"]").get_by_label("Área rich-text. Pressione ALT").fill(alternativa_b)
    except:
        pass
    try:
        await page.frame_locator("internal:role=row[name=\"Correta 3 Resposta c. Para\"i] >> iframe[title=\"Rich Text Area\"]").get_by_label("Área rich-text. Pressione ALT").fill(alternativa_c)
    except:
        pass
    try:
        await page.frame_locator("internal:role=row[name=\"Correta 4 Resposta d. Para\"i] >> iframe[title=\"Rich Text Area\"]").get_by_label("Área rich-text. Pressione ALT").fill(alternativa_d)
    except:
        pass
    try:
        await page.frame_locator("internal:role=row[name=\"Correta 5 Resposta e. Para\"i] >> iframe[title=\"Rich Text Area\"]").get_by_label("Área rich-text. Pressione ALT").fill(alternativa_e)
    except:
        pass
    await page.get_by_role("button", name="Enviar", exact=True).click()
    await page.wait_for_load_state('networkidle')