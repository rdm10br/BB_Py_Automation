import asyncio, re
from playwright.async_api import expect, Page

from Metodos.BQ import getBQ

async def QuestionOnBB(page: Page, index: int, path: str) -> None:
    """
    This function sets the configuration on the BB root  for questions
    and throws the statement and questions choices.

    Args:
        page (Page): Page constructor form Playwright that
        index (int): Index of question
        path (str): Path of the Questionary file
    """
    
    statement = getBQ.get_Enunciado(index=index, path=path)
    choiceA = getBQ.get_Alternativa(index=index, path=path, choices="A")
    choiceB = getBQ.get_Alternativa(index=index, path=path, choices="B")
    choiceC = getBQ.get_Alternativa(index=index, path=path, choices="C")
    choiceD = getBQ.get_Alternativa(index=index, path=path, choices="D")
    choiceE = getBQ.get_Alternativa(index=index, path=path, choices="E")
    
    # await page.hover("menuitem")
    # await page.get_by_role("menuitem", name="Múltipla Escolha").click()

    await page.wait_for_load_state('domcontentloaded')

    await page.frame_locator("[id=\"questionText\\.text_ifr\"]"
                             ).get_by_label("Área rich-text. Pressione ALT"
                                            ).fill(statement)

    await page.get_by_label("Numeração das Respostas").select_option(
        "letter_lower")

    await page.get_by_label("Mostrar Respostas por Ordem").check()

    await page.get_by_role("radiogroup", name="Número de Respostas"
                           ).get_by_label("Número de Respostas"
                                          ).select_option("5")

    await page.wait_for_load_state('domcontentloaded')

    # await page.frame_locator("internal:role=row[name=\"Correta 1 Resposta a. "\
    # "Para\"i] >> iframe[title=\"Rich Text Area\"]"
    # ).get_by_label("Área rich-text. Pressione ALT").click()

    await page.frame_locator("internal:role=row[name=\"Correta 1 Resposta a. "
                             "Para\"i] >> iframe[title=\"Rich Text Area\"]"
                             ).get_by_role("paragraph").fill(choiceA)

    await page.frame_locator("internal:role=row[name=\"Correta 2 Resposta b. "
                             "Para\"i] >> iframe[title=\"Rich Text Area\"]"
                             ).get_by_role("paragraph").fill(choiceB)

    await page.frame_locator("internal:role=row[name=\"Correta 3 Resposta c. "
                             "Para\"i] >> iframe[title=\"Rich Text Area\"]"
                             ).get_by_role("paragraph").fill(choiceC)

    await page.frame_locator("internal:role=row[name=\"Correta 4 Resposta d. "
                             "Para\"i] >> iframe[title=\"Rich Text Area\"]"
                             ).get_by_role("paragraph").fill(choiceD)

    await page.frame_locator("internal:role=row[name=\"Correta 5 Resposta e. "
                             "Para\"i] >> iframe[title=\"Rich Text Area\"]"
                             ).get_by_role("paragraph").fill(choiceE)

    # await page.get_by_role("button", name="Enviar", exact=True)

    await page.get_by_role("button", name="Enviar e Criar outra")