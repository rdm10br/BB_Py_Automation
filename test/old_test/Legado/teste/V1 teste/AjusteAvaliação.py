from playwright.sync_api import Playwright, sync_playwright, expect
import re

def ajusteAvaliacao(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    # Access page
    page = context.pages[0]
    
    # page.wait_for_load_state('domcontentloaded')
    # page.press('body','End')
    # page.wait_for_load_state('domcontentloaded')
    # page.press('body','End')
    # page.get_by_text("Avaliações").click()
    # page.get_by_label("Mais opções para Regras da").click()
    # page.locator("div").filter(has_text=re.compile(r"^Editar$")).click()
    
    page.wait_for_load_state('domcontentloaded')
    page.press('body','End')
    page.wait_for_load_state('domcontentloaded')
    page.press('body','End')
    page.get_by_role("button", name="Avaliações", exact=True).click()
    page.get_by_label("Mais opções para Regras da").click()
    page.get_by_text("Editar", exact=True).click()
    page.get_by_role("heading", name="Regras da Avaliação - Resolu").click()
    page.get_by_label("Novo link de LTI em undefined").click(click_count=3)
    page.get_by_label("Novo link de LTI em undefined").fill("Regras da Avaliação - Resolução CONSU")
    page.get_by_label("Novo link de LTI em undefined").press("Enter")
    page.wait_for_load_state('domcontentloaded')
    page.get_by_role("button", name="Salvar").click()
    page.wait_for_load_state('networkidle')