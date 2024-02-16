from playwright.sync_api import Playwright, sync_playwright, expect

def AjusteNotaZero(playwright: Playwright, id_interno) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    page = context.pages[1]
    baseURL = "https://sereduc.blackboard.com/"
    classURL = baseURL+"ultra/courses/"
    ContentURL = classURL+id_interno+"/outline"
    GradeURL = classURL+id_interno+'/grades?gradebookView=list&listViewType=assignments'
    page.goto(GradeURL)
    page.get_by_label("Configurações", exact=True).click()
    page.get_by_text("Atribui nota zero").click()
    page.get_by_text("Remover notas zero atribuídas").click()
    page.get_by_role("button", name="Confirmar").click()
    page.locator("#main-content > div:nth-child(4)").click()