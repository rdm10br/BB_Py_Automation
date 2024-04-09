from playwright.async_api import Playwright, async_playwright, expect, Page


async def ajusteData(page: Page, dataShow, dataHide) -> None:
    
    baseURL = "https://sereduc.blackboard.com/"
    # rootURL = f'{baseURL}webapps/blackboard/execute/content/adaptiveReleaseRules?course_id={internalID}&content_id={contentID}'
    
    await page.get_by_role("checkbox", name="Fale com o Tutor").check()
    await page.get_by_role("checkbox", name="Desafio Colaborativo").check()
    await page.get_by_role("button", name="Editar datas").click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Mostrar na data").check()
    await page.get_by_role("checkbox", name="Mostrar no horário").check()
    await page.get_by_role("checkbox", name="Ocultar após a data").check()
    await page.get_by_role("checkbox", name="Ocultar após o horário").check()
    await page.get_by_role("textbox", name="Mostrar na data").fill(dataShow)
    await page.get_by_role("textbox", name="Mostrar no horário").fill("00:00")
    await page.get_by_role("textbox", name="Ocultar após a data").fill(dataHide)
    await page.get_by_role("textbox", name="Ocultar após o horário").fill("23:59")
    # await page.get_by_role("button", name="Editar datas").click()