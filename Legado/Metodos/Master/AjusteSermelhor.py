from playwright.sync_api import Playwright, sync_playwright, expect


def ajusteSerMelhor(playwright: Playwright) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    # Access page
    page = context.pages[0]
    
    page.press('body','End')
    page.press('body','End')
    page.get_by_label("Mais opções para SER Melhor (").click()
    page.get_by_text("Editar", exact=True).click()
    page.get_by_placeholder("Digite um URL").click(click_count=3)
    page.get_by_placeholder("Digite um URL").fill("https://forms.office.com/r/wX8V5625hs")
    # page.wait_for_load_state('networkidle')
    page.get_by_text("Máximo de 750 caracteres").click()
    page.get_by_role("button", name="Salvar").click()
    page.wait_for_load_state('load')