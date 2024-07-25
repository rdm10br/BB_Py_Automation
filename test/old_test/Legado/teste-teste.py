from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sereduc.blackboard.com/")
    page.get_by_role("dialog").first.click()
    page.get_by_role("button", name="OK").click()
    page.get_by_label("Nome de usuário").click()
    page.get_by_label("Nome de usuário").fill("rafael.dias")
    page.get_by_label("Nome de usuário").press("Tab")
    page.get_by_label("Senha").fill("123321!")
    page.get_by_label("Senha").press("Enter")
    page.wait_for_load_state('domcontentloaded')
    page.get_by_role("link", name="Módulo C - 229623 . 7 -").click()
    page.wait_for_load_state('domcontentloaded')
    # page.get_by_label("Conteúdo da Disciplina", exact=True).locator("header").click()
    # page.locator(".panel-content").click()
    # page.locator("#main-content > div:nth-child(3)").press("End")
    # page.locator(".panel-content").click()
    # page.get_by_role("button", name="Fechar").click()
    # page.locator("#main-content > div:nth-child(3)").press("PageDown")
    # page.locator("#main-content > div:nth-child(3)").press("PageDown")
    # page.locator("#main-content > div:nth-child(3)").press("PageDown")
    # page.locator(".panel-content").click()
    # page.get_by_role("button", name="Fechar").click()
    page.wait_for_timeout(5*1000)
    page.get_by_role("heading", name='Módulo').press("End")
    page.get_by_role("heading", name='Módulo').press("End")
    page.wait_for_timeout(5*1000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)