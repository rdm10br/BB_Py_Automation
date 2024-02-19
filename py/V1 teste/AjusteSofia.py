from playwright.sync_api import Playwright, sync_playwright, expect

cliqueMenu = ('''const xpath = '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/course-content-outline/react-course-content-outline/div/div/div[1]/div[3]/div[3]/div[1]/div/div[2]/div/div[2]/button';
const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

if (element) {
    element.dispatchEvent(new MouseEvent('mouseover'));
    element.click();
} else {
    console.error('Elemento não encontrado com a expressão XPath fornecida.');}''')

cliqueEditar = ('''const xpath = '/html/body/div[12]/div[3]/ul/li[1]';
const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

if (element) {
    element.dispatchEvent(new MouseEvent('mouseover'));
    element.click();
} else {
    console.error('Elemento não encontrado com a expressão XPath fornecida.');}''')

def ajusteSofia(playwright: Playwright) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    # page.set_default_timeout(timeout=5000)
    
    page.wait_for_load_state('networkidle')
    URLpage = page.url+'?search=organize'
    page.wait_for_load_state('networkidle')
    page.evaluate(cliqueMenu)
    page.wait_for_load_state('networkidle')
    page.evaluate(cliqueEditar)
    page.wait_for_load_state('networkidle')
    page.wait_for_url("**/edit/lti")
    page.get_by_placeholder("Formato: meuwebsite.com").click(click_count=3)
    page.get_by_placeholder("Formato: meuwebsite.com").fill("sofialti.ldmedtech.com.br/v1/launch/ser-sofia-plano-estudos")
    page.wait_for_load_state('networkidle')
    page.get_by_role("button", name="Salvar").click()