from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import getPlanilha

clickButtonMenu = ('''const xpathExpression = '/html/body/div[2]/div[3]/div/div/div[4]/form/div[2]/div[2]/div/table/tbody/tr/td[2]/span[2]/span/a';
    const xpathResult = document.evaluate(xpathExpression, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);

    // Verificar se o resultado XPath é válido e o elemento existe
    if (xpathResult && xpathResult.singleNodeValue) {
    // Obter o elemento do resultado XPath
    const element = xpathResult.singleNodeValue;
    
    // Disparar o evento de hover no elemento
    element.dispatchEvent(new MouseEvent('mouseover'));

    // Simular um clique no elemento
    element.click();
    } else {
    console.error('Elemento não encontrado com a expressão XPath fornecida.');}''')

clickButtonCopy = ('''const xpathExpression = '/html/body/div[4]/ul[4]/li/a';
    const xpathResult = document.evaluate(xpathExpression, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);

    // Verificar se o resultado XPath é válido e o elemento existe
    if (xpathResult && xpathResult.singleNodeValue) {
    // Obter o elemento do resultado XPath
    const element = xpathResult.singleNodeValue;

    // Simular um clique no elemento
    element.click();
    } else {
    console.error('Elemento não encontrado com a expressão XPath fornecida.');}''')

def copySala(playwright: Playwright , index) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    baseURL = "https://sereduc.blackboard.com/"
    searchOnBlack = "https://sereduc.blackboard.com/webapps/blackboard/execute/courseManager?sourceType=COURSES&courseInfoSearchKeyString=CourseId&courseInfoSearchOperatorString=Equals&courseInfoSearchText="
    
    id_master = getPlanilha.getCell_plan2(index)
    id_copia = getPlanilha.getCell_copy_plan2(index)
    
    page.goto(searchOnBlack+id_master)
    # click no menu de opções da sala
    page.evaluate(clickButtonMenu)
    page.wait_for_load_state('domcontentloaded')
    # click no botão de copia
    page.evaluate(clickButtonCopy)
    page.wait_for_load_state('domcontentloaded')
    page.locator('#destinationCourseId').fill(id_copia)
    page.locator('#bottom_Submit').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator('#stepcontent2 > ol > li:nth-child(5) > div > div > a:nth-child(1)').click()
    page.locator('#bottom_Submit').click()
    
# with sync_playwright() as playwright:
#     copySala(playwright ,index=1)