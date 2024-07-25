from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.connect()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="example.png")