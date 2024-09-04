from playwright.async_api import Page, expect
from Metodos.BQ import getBQ as gb
import regex as re
import os
from unidecode import unidecode

def get_bq_name(path: str) -> str:
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
    BQ_name = re.sub(r'\d','',BQ_name)
    BQ_name = re.sub(r'\s+', ' ', BQ_name)
    BQ_name = re.sub(r'\s$', '', BQ_name)
    BQ_name = re.sub(r'^\s', '', BQ_name)
    BQ_name = BQ_name.strip()
    BQ_name = f'{BQ_name} - {item}_GRADUACAO'
    return BQ_name

async def create_bq(page: Page, BQ_name: str) -> str:
    """_summary_

    Args:
        page (Page): _description_
        BQ_name (str): _description_
    """
    await page.get_by_role("button", name="Criar banco de testes").click()
    await page.get_by_label("Nome", exact=True).fill(BQ_name)
    await page.get_by_role("button", name="Enviar").click()
    
    
async def create_question(index: int, path: str, page: Page):
    index-=1
    enunciado = gb.get_Enunciado(index=index, path=path)
    enunciado = re.sub(r'\s+', ' ', enunciado)
    enunciado = enunciado.strip()
    
    alternativa_a = gb.get_Alternativa(index=index, path=path, choices='a')
    alternativa_a = re.sub(r'\s+', ' ', alternativa_a)
    alternativa_a = alternativa_a.strip()
    
    alternativa_b = gb.get_Alternativa(index=index, path=path, choices='b')
    alternativa_b = re.sub(r'\s+', ' ', alternativa_b)
    alternativa_b = alternativa_b.strip()
    
    alternativa_c = gb.get_Alternativa(index=index, path=path, choices='c')
    alternativa_c = re.sub(r'\s+', ' ', alternativa_c)
    alternativa_c = alternativa_c.strip()
    
    alternativa_d = gb.get_Alternativa(index=index, path=path, choices='d')
    alternativa_d = re.sub(r'\s+', ' ', alternativa_d)
    alternativa_d = alternativa_d.strip()
    
    alternativa_e = gb.get_Alternativa(index=index, path=path, choices='e')
    alternativa_e = re.sub(r'\s+', ' ', alternativa_e)
    alternativa_e = alternativa_e.strip()
    
    try:
        alternativa_correta = gb.get_correct_alternative_from_list(path=path, index=index)
    except:
        alternativa_correta = 'a'
    
    await page.get_by_role("button", name="Criar pergunta").click()
    await page.get_by_role("menuitem", name="Múltipla Escolha").click()
    await page.wait_for_load_state('domcontentloaded')
    try:
        await page.frame_locator("[id=\"questionText\\.text_ifr\"]").get_by_label("Área rich-text. Pressione ALT").fill(enunciado)
    except:
        pass
    await page.get_by_label("Numeração das Respostas").select_option("letter_lower")
    await page.get_by_label("Mostrar Respostas por Ordem").check()
    await page.get_by_role("radiogroup", name="Número de Respostas").get_by_label("Número de Respostas").select_option("5")
    await page.wait_for_load_state('domcontentloaded')
    # await page.wait_for_load_state('networkidle')
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
    
    # Right choice
    try:
        match alternativa_correta.lower():
            case 'a':
                await page.frame_locator("iframe[name=\"classic-learn-iframe\"]").get_by_role("radio", name="Correta 1").check()
                print(f'Question {index+1} right choice found: {alternativa_correta.lower()}')
            case 'b':
                await page.frame_locator("iframe[name=\"classic-learn-iframe\"]").get_by_role("radio", name="Correta 2").check()
                print(f'Question {index+1} right choice found: {alternativa_correta.lower()}')
            case 'c':
                await page.frame_locator("iframe[name=\"classic-learn-iframe\"]").get_by_role("radio", name="Correta 3").check()
                print(f'Question {index+1} right choice found: {alternativa_correta.lower()}')
            case 'd':
                await page.frame_locator("iframe[name=\"classic-learn-iframe\"]").get_by_role("radio", name="Correta 4").check()
                print(f'Question {index+1} right choice found: {alternativa_correta.lower()}')
            case 'e':
                await page.frame_locator("iframe[name=\"classic-learn-iframe\"]").get_by_role("radio", name="Correta 5").check()
                print(f'Question {index+1} right choice found: {alternativa_correta.lower()}')
            case _:
                print(f'Question {index+1} no right choice found!')
                pass
    except:
        pass
    
    await page.get_by_role("button", name="Enviar", exact=True).click()
    await page.wait_for_load_state('networkidle')