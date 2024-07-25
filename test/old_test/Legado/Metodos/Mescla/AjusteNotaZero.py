from playwright.sync_api import Playwright, sync_playwright, expect

def AjusteNotaZero(playwright: Playwright, id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    page = context.pages[0]
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    ContentURL = f'{classURL}{id_interno}/outline'
    GradeURL = f'{classURL}{id_interno}/grades?gradebookView=list&listViewType=assignments'
    
    page.goto(GradeURL)
    page.get_by_label("Configurações", exact=True).click()
    page.get_by_text("Atribui nota zero").click()
    page.get_by_text("Remover notas zero atribuídas").click()
    page.get_by_role("button", name="Confirmar").click()
    page.locator("#main-content > div:nth-child(4)").click()
    page.goto(ContentURL)
    page.wait_for_load_state('domcontentloaded')