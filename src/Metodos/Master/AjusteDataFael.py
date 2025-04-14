from playwright.async_api import Page


async def ajusteData(
    page: Page,
    id_interno: str,
    horaInicial: str = '00:00',
    horaFinal: str = '23:59',
    data1: str = '17/05/25',
    data2: str = '10/05/25',
    data3: str = '20/04/25'
    ) -> None:
    """_summary_
    This function change the date opening and due date of some items in
    classroom
    Args:
        page (Page): _description_: Deafault Playwright item
        id_interno (str): _description_: Deafault classroom ID
        horaInicial (_type_, optional): _description_: Defaults to '00:00'.
        horaFinal (_type_, optional): _description_: Defaults to '23:59'.
        data1 (str, optional): _description_: Defaults to '17/05/25', this date changes the due date to [Exercício de Fixação 01, 02, 03, Exercício do Conhecimento] and Opening date [Fale com o tutor].
        data2 (str, optional): _description_: Defaults to '10/05/25', this date changes the due date to [Avaliação Workshop, Discursiva] and Opening date [Converse com a sua Turma]
        data3 (str, optional): _description_: Defaults to '20/04/25', this date changes the Opening date to [Avaliação Workshop]
    """
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    classBulkEdit = f'{classUrlUltra}/bulkEditContent'
    
    await page.goto(classBulkEdit)
    
    listaum =[
        "Exercício de Fixação 01",
        "Exercício de Fixação 02",
        "Exercício de Fixação 03",
        "Exercício do Conhecimento",
    ]
    
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
    await page.get_by_role("textbox", name="Data de entrega").fill(data1)
    await page.get_by_role("checkbox", name="Hora de entrega").check()
    await page.wait_for_timeout(2000)
    await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de entregaHora de entrega").click()
    await page.wait_for_timeout(2000)
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2000)
    
    await page.locator("#Avaliação\\ Workshop-2-checkbox").click()
    await page.wait_for_timeout(1500)
    await page.locator("#Avaliação\\ Discursiva-3-checkbox").click()

    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de entrega").check()
    await page.get_by_role("textbox", name="Data de entrega").fill(data2)
    await page.get_by_role("checkbox", name="Hora de entrega").check()
    await page.wait_for_timeout(2000)
    await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
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
    await page.get_by_role("textbox", name="Data de fim do acesso").fill(data1)
    await page.wait_for_timeout(1500)
    await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
    await page.get_by_role("textbox", name="Horário de fim do acesso").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de fim do acessoHorário").click()
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    
    await page.get_by_role("checkbox", name="Converse com a sua Turma").check()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de fim do acesso").check()
    await page.get_by_role("textbox", name="Data de fim do acesso").fill(data2)
    await page.wait_for_timeout(1500)
    await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
    await page.get_by_role("textbox", name="Horário de fim do acesso").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de fim do acessoHorário").click()
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    
    await page.get_by_text("Avaliação Workshop").click()
    await page.locator("#Avaliação\\ Workshop-0-checkbox").click()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_role("checkbox", name="Data de início do acesso").check()
    await page.get_by_role("textbox", name="Data de início do acesso").fill(data3)
    await page.wait_for_timeout(1500)
    await page.get_by_role("checkbox", name="Horário de início do acesso").check()
    await page.get_by_role("textbox", name="Horário de início do acesso").fill(horaInicial)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de início do acessoHorá").click()
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)