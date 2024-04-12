from playwright.async_api import Playwright, async_playwright, expect, Page


async def ajusteSerMelhor(page: Page) -> None:
    
    await page.reload    
    await page.wait_for_load_state('domcontentloaded')
    await page.press('body','End')
    await page.wait_for_load_state('domcontentloaded')
    await page.press('body','End')
    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    await page.wait_for_load_state('load')
    await page.get_by_label("Mais opções para SER Melhor (").click()
    await page.get_by_text("Editar", exact=True).click()
    await page.get_by_placeholder("Digite um URL").click(click_count=3)
    await page.get_by_placeholder("Digite um URL").fill("https://forms.office.com/r/wX8V5625hs")
    # await page.wait_for_load_state('networkidle')
    await page.get_by_text("Máximo de 750 caracteres").click()
    await page.get_by_role("button", name="Salvar").click()
    await page.wait_for_load_state('load')