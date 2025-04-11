from playwright.async_api import Page


async def ajusteData(page: Page) -> None:
    """
    Function that sets the ```dataShow``` and ```dataHide``` of an item

    Args:
        await page (Page): Page constructor form Playwright that
        you want this Function to run
        dataShow (str): Date to show the item in classroom
        dataHide (str): Date to hide the item in classroom
    """
    # baseURL = "https://sereduc.blackboard.com/"
    # rootURL = f'{baseURL}webapps/blackboard/execute/content/adaptiveReleaseRules?course_id={internalID}&content_id={contentID}'
    
    # await page.get_by_role("checkbox", name="Fale com o Tutor").check()
    # await page.get_by_role("checkbox", name="Desafio Colaborativo").check()
    
    listaum =[
        "Exercício de Fixação 01",
        "Exercício de Fixação 02",
        "Exercício de Fixação 03",
        "Exercício do Conhecimento",
        
    ]# datas de entrega do dia 17
    
    
    listadois =[
        "Avaliação Workshop",
        "Avaliação Discursiva",
    ]# datas de entrega do dia 10
    
    
    listatres =[
        "Fale com o tutor"
    ]# condição de liberação dia 17
    
    
    listaquatro =[
        "Converse com a sua Turma"
    ]# condição de liberação dia 10
    
    
    listacinco =[
        "Avaliação Workshop"
    ]# condição de liberação dia 20
    
    
    await page.get_by_role("row", name="​📝​ Avaliações e Exercícios").get_by_label("row.openFolder").click()
    await page.get_by_text("Exercícios de Fixação").click()
    await page.get_by_text("Avaliação Exercício do").click()
    
    
    
    for item in listaum:
        await page.get_by_role("checkbox", name=item, exact=True).check()
        await page.wait_for_timeout(2500)
        
        
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de entrega").check()
    await page.get_by_role("textbox", name="Data de entrega").fill("17/05/25")
    await page.get_by_role("checkbox", name="Hora de entrega").check()
    await page.wait_for_timeout(2000)
    await page.get_by_role("textbox", name="Hora de entrega").fill("23:59")
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de entregaHora de entrega").click()
    await page.wait_for_timeout(2000)
    await page.get_by_role("button", name="Editar datas").click()
    
    await page.wait_for_timeout(3000)
    
    
    await page.locator("#Avaliação\\ Workshop-2-checkbox").click()
    await page.locator("#Avaliação\\ Discursiva-3-checkbox").click()


    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de entrega").check()
    await page.get_by_role("textbox", name="Data de entrega").fill("10/05/25")
    await page.get_by_role("checkbox", name="Hora de entrega").check()
    await page.wait_for_timeout(2000)
    await page.get_by_role("textbox", name="Hora de entrega").fill("23:59")
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de entregaHora de entrega").click()
    await page.wait_for_timeout(2000)
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(2000)


    
    await page.get_by_role("checkbox", name="Fale com o tutor").check()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de fim do acesso").check()
    await page.get_by_role("textbox", name="Data de fim do acesso").fill("17/05/25")
    await page.wait_for_timeout(1500)
    await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
    await page.get_by_role("textbox", name="Horário de fim do acesso").fill("23:59")
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de fim do acessoHorário").click()
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    
    
    
    await page.get_by_role("checkbox", name="Converse com a sua Turma").check()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de fim do acesso").check()
    await page.get_by_role("textbox", name="Data de fim do acesso").fill("10/05/25")
    await page.wait_for_timeout(1500)
    await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
    await page.get_by_role("textbox", name="Horário de fim do acesso").fill("23:59")
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de fim do acessoHorário").click()
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    
    
    await page.get_by_text("Avaliação Workshop").click()
    await page.locator("#Avaliação\\ Workshop-0-checkbox").click()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_role("checkbox", name="Data de início do acesso").check()
    await page.get_by_role("textbox", name="Data de início do acesso").fill("20/04/25")
    await page.wait_for_timeout(1500)
    await page.get_by_role("checkbox", name="Horário de início do acesso").check()
    await page.get_by_role("textbox", name="Horário de início do acesso").fill("00:00")
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de início do acessoHorá").click()
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)