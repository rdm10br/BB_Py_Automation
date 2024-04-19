from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    username = ''
    password = ''
    page.goto("https://sereduc.blackboard.com/")
    page.get_by_label("Privacidade, cookies e termos").locator("div").nth(1).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_label("Nome de usuário").click()
    page.get_by_label("Nome de usuário").fill(username)
    page.get_by_label("Nome de usuário").press("Tab")
    page.get_by_label("Senha").fill(password)
    page.get_by_label("Senha").press("Enter")
    page.wait_for_load_state('domcontentloaded')
    page.goto(url='https://sereduc.blackboard.com/ultra/courses/_139625_1/outline', wait_until='domcontentloaded')
    page.wait_for_timeout(4*1000)
    page.wait_for_selector(selector='Avaliações', state='attached')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)