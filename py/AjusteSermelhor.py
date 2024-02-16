from playwright.sync_api import Playwright, sync_playwright, expect


def ajusteSerMelhor(playwright: Playwright) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    # Access page
    page = context.pages[0]
    page.set_default_timeout(timeout=5000)
    
    # page.wait_for_load_state('domcontentloaded')
    page.press('body','End')
    page.press('body','End')
    # page.wait_for_load_state('domcontentloaded')
    page.press('body','End')
    page.get_by_label("Mais opções para SER Melhor (").click()
    page.get_by_text("Editar", exact=True).click()
    page.get_by_placeholder("Digite um URL").click()
    page.get_by_placeholder("Digite um URL").press("Control+a")
    page.get_by_placeholder("Digite um URL").fill("https://forms.office.com/r/wX8V5625hs")
    page.wait_for_load_state('networkidle')
    # page.wait_for_load_state('domcontentloaded')
    page.locator('#tabpanel-webLink > div.additional-tools.panel-section > h2').click()
    page.get_by_role("button", name="Salvar").click()
