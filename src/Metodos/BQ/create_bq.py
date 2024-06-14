from playwright.async_api import Page, expect
from Metodos.BQ import getBQ as gb


async def create_bq():
    ...
    
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