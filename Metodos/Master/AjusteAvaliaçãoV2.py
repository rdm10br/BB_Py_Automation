from playwright.async_api import Playwright, async_playwright, expect, Page
from Metodos.API import getApiContent

async def ajusteAvaliacao(page: Page, id_interno) -> None:    
    itemSearch = 'Avaliações'
    url = page.url
    id_avaliacao = await getApiContent.API_Req_Content(page=page, id_interno=id_interno, item_Search=itemSearch)
    
    await page.goto(url)
    await page.wait_for_load_state('domcontentloaded')
    page.get_by_role("heading", name='Módulo').press("End")
    page.get_by_role("heading", name='Módulo').press("End")
    await page.press('body','End')
    await page.wait_for_load_state('domcontentloaded')
    await page.press('body','End')
    await page.locator(f'#folder-title-{id_avaliacao}').click()
    await page.get_by_label("Mais opções para Regras da").click()
    await page.get_by_text("Editar", exact=True).click()
    await page.get_by_role("heading", name="Regras da Avaliação - Resolu").click()
    await page.get_by_label("Novo link de LTI em undefined").click(click_count=3)
    await page.get_by_label("Novo link de LTI em undefined").fill("Regras da Avaliação - Resolução CONSU")
    await page.get_by_label("Novo link de LTI em undefined").press("Enter")
    await page.wait_for_load_state('domcontentloaded')
    await page.get_by_role("button", name="Salvar").click()