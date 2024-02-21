from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sereduc.blackboard.com/")
    page.get_by_role('button',name='OK').click()
    page.get_by_label("Nome de usuário").fill("rafael.dias")
    page.get_by_label("Senha").fill("123321!")
    page.get_by_role("button", name="Fazer login").click()
    page1 = context.new_page()
    page1.goto("https://sereduc.blackboard.com/webapps/blackboard/execute/courseManager?sourceType=COURSES&courseInfoSearchKeyString=CourseId&courseInfoSearchOperatorString=Equals&courseInfoSearchText=6848")
    page1.wait_for_load_state("domcontentloaded")
    page1.get_by_role("button", name="Menu de opções: Código do Curso").click()
    page1.get_by_role("menuitem", name="Copiar").click()

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
