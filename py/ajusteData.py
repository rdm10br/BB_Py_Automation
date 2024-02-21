from playwright.sync_api import Playwright, sync_playwright, expect


def ajusteData(playwright: Playwright,dataShow,dataHide) -> None:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    
    page.get_by_role("checkbox", name="Fale com o Tutor").check()
    page.get_by_role("checkbox", name="Desafio Colaborativo").check()
    page.get_by_role("button", name="Editar datas").click()
    page.get_by_label("Tipo de edição").click()
    page.get_by_role("option", name="Alterar para data e/ou hora").click()
    page.get_by_role("checkbox", name="Mostrar na data").check()
    page.get_by_role("checkbox", name="Mostrar no horário").check()
    page.get_by_role("checkbox", name="Ocultar após a data").check()
    page.get_by_role("checkbox", name="Ocultar após o horário").check()
    page.get_by_role("textbox", name="Mostrar na data").fill(dataShow)
    page.get_by_role("textbox", name="Mostrar no horário").fill("00:00")
    page.get_by_role("textbox", name="Ocultar após a data").fill(dataHide)
    page.get_by_role("textbox", name="Ocultar após o horário").fill("23:59")
    page.get_by_role("button", name="Editar datas").click()