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
    
    # https://sereduc.blackboard.com/ultra/courses/_307132_1/outline/bulkEditContent
    
    await page.goto(url=classBulkEdit, wait_until='domcontentloaded')
    
    listaum =[
        "Exercício de Fixação 01",
        "Exercício de Fixação 02",
        "Exercício de Fixação 03",
        "Exercício do Conhecimento",
    ]
    
    print('adjusting items date...')
    await page.get_by_role("row", name="​📝​ Avaliações e Exercícios").wait_for(state='visible', timeout=20*1000)
    await page.get_by_role("row", name="​📝​ Avaliações e Exercícios").get_by_label("row.openFolder").click()
    await page.get_by_text("Exercícios de Fixação").click()
    await page.get_by_text("Avaliação Exercício do").click()
    print(f'adjusting items: {listaum}')
    
    for item in listaum:
        await page.get_by_role("checkbox", name=item, exact=True).wait_for(state='visible', timeout=8*1000)
        await page.get_by_role("checkbox", name=item, exact=True).check()
        await page.wait_for_timeout(2500)
    
    print('edit date...')
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    print('due date...')
    await page.get_by_role("checkbox", name="Data de entrega").check()
    await page.get_by_role("textbox", name="Data de entrega").fill(data1)
    print('due hour...')
    await page.get_by_role("checkbox", name="Hora de entrega").check()
    await page.wait_for_timeout(2000)
    await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de entregaHora de entrega").click()
    await page.wait_for_timeout(2000)
    print('saving...')
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2000)
    
    print('adjusting "workshop" folder, "discursiva" folder.....')
    try:
        await page.locator("#Avaliação\\ Workshop-2-checkbox").wait_for(state='visible', timeout=15*1000)
        await page.locator("#Avaliação\\ Workshop-2-checkbox").click()
        await page.locator("#Avaliação\\ Discursiva-3-checkbox").click()
    except:
        try:
            await page.locator("#Avaliação\\ Workshop-3-checkbox").wait_for(state='visible', timeout=5*1000)
            await page.locator("#Avaliação\\ Workshop-3-checkbox").click()
            await page.locator("#Avaliação\\ Discursiva-4-checkbox").click()
        except:
            await page.locator("#Avaliação\\ Workshop-0-checkbox").wait_for(state='visible', timeout=5*1000)
            await page.locator("#Avaliação\\ Workshop-0-checkbox").click()
            await page.locator("#Avaliação\\ Discursiva-3-checkbox").click()

    print('edit date...')
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    print('due date...')
    await page.get_by_role("checkbox", name="Data de entrega").check()
    await page.get_by_role("textbox", name="Data de entrega").fill(data2)
    print('due hour...')
    await page.get_by_role("checkbox", name="Hora de entrega").check()
    await page.wait_for_timeout(2000)
    await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de entregaHora de entrega").click()
    print('saving...')
    await page.wait_for_timeout(2000)
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(2000)
    
    print('edit "Fale com o tutor" date...')
    await page.get_by_role("checkbox", name="Fale com o tutor").wait_for(state='visible', timeout=8*1000)
    await page.get_by_role("checkbox", name="Fale com o tutor").check()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    print('end date....')
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    await page.get_by_role("checkbox", name="Data de fim do acesso").check()
    await page.get_by_role("textbox", name="Data de fim do acesso").fill(data1)
    await page.wait_for_timeout(1500)
    print('end hour...')
    await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
    await page.get_by_role("textbox", name="Horário de fim do acesso").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de fim do acessoHorário").click()
    print('saving...')
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    
    print('edit "Converse com a sua Turma" date...')
    await page.get_by_role("checkbox", name="Converse com a sua Turma").wait_for(state='visible', timeout=8*1000)
    await page.get_by_role("checkbox", name="Converse com a sua Turma").check()
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    await page.get_by_label("Tipo de edição").click()
    await page.get_by_role("option", name="Alterar para data e/ou hora").click()
    print('end date....')
    await page.get_by_role("checkbox", name="Data de fim do acesso").check()
    await page.get_by_role("textbox", name="Data de fim do acesso").fill(data2)
    await page.wait_for_timeout(1500)
    print('end hour...')
    await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
    await page.get_by_role("textbox", name="Horário de fim do acesso").fill(horaFinal)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de fim do acessoHorário").click()
    print('saving...')
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    
    print('edit workshop date...')
    
    try:
        await page.get_by_text("Avaliação Workshop").wait_for(state='visible', timeout=8*1000)
        await page.get_by_text("Avaliação Workshop").click()
        await page.locator("#Avaliação\\ Workshop-0-checkbox").click()
    except:
        await page.get_by_text("PastaAvaliação Workshop").wait_for(state='visible', timeout=8*1000)
        await page.get_by_text("PastaAvaliação Workshop").click()
        await page.locator("#Avaliação\\ Workshop-0-checkbox").click()
        # await page.get_by_role("row", name="Avaliação Workshop Teste").get_by_label("", exact=True).check()
    
    await page.get_by_role("button", name="Editar datas", exact=True).click()
    print('release date...')
    await page.get_by_role("checkbox", name="Data de início do acesso").check()
    await page.get_by_role("textbox", name="Data de início do acesso").fill(data3)
    await page.wait_for_timeout(1500)
    print('release hour...')
    await page.get_by_role("checkbox", name="Horário de início do acesso").check()
    await page.get_by_role("textbox", name="Horário de início do acesso").fill(horaInicial)
    await page.wait_for_timeout(1500)
    await page.get_by_text("Data de início do acessoHorá").click()
    print('saving...')
    await page.get_by_role("button", name="Editar datas").click()
    await page.wait_for_timeout(1500)
    

async def ajusteData_especiais(
    page: Page,
    id_interno: str,
    horaInicial: str = '00:00',
    horaFinal: str = '23:59',
    dataI1: list[str] = ['25/08/25', '15/09/25', '06/10/25', '27/10/25'],
    dataF1: list[str] = ['05/09/25', '25/09/25', '17/10/25', '10/11/25'],
    dataI2: list[str] = ['17/11/25', '01/12/25'],
    dataF2: list[str] = ['30/11/25', '28/12/25'],
    ) -> None:
    """_summary_
    This function change the date opening and due date of some items in
    classroom for special cases like engineering

    Lembrar de alterar a data para as engenharias (RODAR SEPARADO)
    Args:
        page (Page): _description_: Deafault Playwright item
        id_interno (str): _description_: Deafault classroom ID
        horaInicial (_type_, optional): _description_: Defaults to '00:00'.
        horaFinal (_type_, optional): _description_: Defaults to '23:59'.
        dataI1 (list[str], optional): _description_: Defaults to ['25/08/25', '15/09/25', '06/10/25', '27/10/25'].
        dataF1 (list[str], optional): _description_: Defaults to ['05/09/25', '25/09/25', '17/10/25', '10/11/25'].
        dataI2 (list[str], optional): _description_: Defaults to ['17/11/25', '01/12/25'].
        dataF2 (list[str], optional): _description_: Defaults to ['30/11/25', '28/12/25'].
    """
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    classBulkEdit = f'{classUrlUltra}/bulkEditContent'

    # https://sereduc.blackboard.com/ultra/courses/_307132_1/outline/bulkEditContent

    await page.goto(url=classBulkEdit, wait_until='domcontentloaded')

    # pasta etapa 1
    await page.get_by_role("row", name="Trabalho de Conclusão de Curso (T1) Pasta row.openFolder Data não ajustada Não").get_by_label("row.openFolder").click()
    # pasta etapa 2
    await page.get_by_role("gridcell", name="Pasta row.openFolder", exact=True).get_by_label("row.openFolder").click()

    # loop etapa 1
    for i in range(1, 5):
        try:
            print(f"Trabalho de Conclusão de Curso (T1) - Etapa {i}")
            await page.get_by_role("checkbox", name=f"Trabalho de Conclusão de Curso (T1) - Etapa {i}").wait_for(state='visible', timeout=10*1000)
            await page.get_by_role("checkbox", name=f"Trabalho de Conclusão de Curso (T1) - Etapa {i}").check()
            await page.get_by_role("button", name="Editar datas", exact=True).click()
            await page.get_by_role("checkbox", name="Data de início do acesso").check()
            await page.get_by_role("checkbox", name="Horário de início do acesso").check()
            await page.get_by_role("checkbox", name="Data de entrega").check()
            # await page.get_by_text("Hora de entrega").click()
            await page.get_by_role("checkbox", name="Hora de entrega").check()
            await page.get_by_role("textbox", name="Data de início do acesso").fill(dataI1[i-1])
            await page.get_by_role("textbox", name="Horário de início do acesso").fill(horaInicial)
            await page.get_by_role("textbox", name="Data de entrega").fill(dataF1[i-1])
            await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
            await page.get_by_text("Editar datas e/ou horários de").click()
            await page.get_by_role("button", name="Editar datas").click()
        except Exception as e:
            print(f"Error adjusting T1 Etapa {i}: {e}")

    for i in range(1, 3):
        if i == 1:
            try:
                print("Trabalho de Conclusão de Curso (T2) Exercício Trabalho de Conclusão de Curso")
                await page.get_by_role("row", name="Trabalho de Conclusão de Curso (T2) Exercício Trabalho de Conclusão de Curso (").get_by_label("", exact=True).wait_for(state='visible', timeout=10*1000)
                await page.get_by_role("row", name="Trabalho de Conclusão de Curso (T2) Exercício Trabalho de Conclusão de Curso (").get_by_label("", exact=True).check()
            except:
                print("Trabalho de Conclusão de Curso (T2) Exercício Trabalho de Conclusão de Curso not found, skipping...")
        elif i == 2:
            try:
                print('Ata de Apresentação')
                await page.get_by_role("checkbox", name="Ata de Apresentação -").wait_for(state='visible', timeout=10*1000)
                await page.get_by_role("checkbox", name="Ata de Apresentação -").check()
            except:
                print("Ata de Apresentação not found, skipping...")

        await page.get_by_role("button", name="Editar datas", exact=True).click()
        await page.get_by_role("checkbox", name="Data de início do acesso").check()
        await page.get_by_role("checkbox", name="Horário de início do acesso").check()
        await page.get_by_role("checkbox", name="Data de entrega").check()
        await page.get_by_role("checkbox", name="Hora de entrega").check()
        await page.get_by_role("textbox", name="Data de início do acesso").fill(dataI2[i-1])
        await page.get_by_role("textbox", name="Horário de início do acesso").fill(horaInicial)
        await page.get_by_role("textbox", name="Data de entrega").fill(dataF2[i-1])
        await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
        await page.get_by_text("Editar datas e/ou horários de").click()
        await page.get_by_role("button", name="Editar datas").click()
   
   
async def ajusteData_estag(
    page: Page,
    id_interno: str,
    horaInicial: str = '00:00',
    horaFinal: str = '23:59',
    dataI: list[str] = ['16/08/25', '16/10/25', '01/09/25', '01/11/25'],
    dataF: list[str] = ['16/10/25', '30/11/25', '15/10/25', '29/11/25'],
    ) -> None:
    """_summary_
    This function change the date opening and due date of some items in
    classroom for special cases like engineering
    Lembrar de alterar a data para as engenharias (RODAR SEPARADO)
    Args:
        page (Page): _description_: Deafault Playwright item
        id_interno (str): _description_: Deafault classroom ID
        horaInicial (_type_, optional): _description_: Defaults to '00:00'.
        horaFinal (_type_, optional): _description_: Defaults to '23:59'.
        dataI (list[str], optional): _description_: Defaults to ['16/08/25', '16/10/25', '01/09/25', '01/11/25'].
        dataF (list[str], optional): _description_: Defaults to ['16/10/25', '30/11/25', '15/10/25', '29/11/25'].
    """
    await page.goto(f"./ultra/courses/{id_interno}/outline/bulkEditContent")
    await page.wait_for_load_state('domcontentloaded')
    await page.wait_for_load_state('load')
    
    await page.get_by_text("Módulo de aprendizagem📝").click()
    
    for i in range(1,5):
        if i < 3:
            try:
                await page.get_by_role("checkbox", name=f"Fórum - Etapa {i}").wait_for(state='visible', timeout=10*1000)
                await page.get_by_role("checkbox", name=f"Fórum - Etapa {i}").check()
                
                await page.get_by_role("button", name="Editar datas", exact=True).click()
                await page.get_by_role("checkbox", name="Data de início do acesso").check()
                await page.get_by_role("checkbox", name="Horário de início do acesso").check()
                await page.get_by_role("checkbox", name="Data de fim do acesso").check()
                await page.get_by_role("checkbox", name="Horário de fim do acesso").check()
                await page.get_by_role("textbox", name="Data de início do acesso").fill(dataI[i-1])
                await page.get_by_role("textbox", name="Horário de início do acesso").fill(horaInicial)
                await page.get_by_role("textbox", name="Data de fim do acesso").fill(dataF[i-1])
                await page.get_by_role("textbox", name="Horário de fim do acesso").fill(horaFinal)
                await page.get_by_text("Editar datas e/ou horários de").click()
                await page.get_by_role("button", name="Editar datas").click()
                await page.wait_for_load_state('load')
                await page.wait_for_load_state('networkidle')
                await page.wait_for_timeout(2*1000)

            except Exception as e:
                print(f"Error adjusting Fórum - Etapa {i}: {e}")
        elif i >= 3:
            try:
                if i == 3:
                    await page.get_by_role("checkbox", name="Postagem Planos e Termo de").check()
                elif i == 4:
                    await page.get_by_role("checkbox", name="Postagem Relatório e Fichas").check()
                    
                await page.get_by_role("button", name="Editar datas", exact=True).click()
                await page.get_by_role("checkbox", name="Data de início do acesso").check()
                await page.get_by_role("checkbox", name="Horário de início do acesso").check()
                await page.get_by_role("checkbox", name="Data de entrega").check()
                await page.get_by_role("checkbox", name="Hora de entrega").check()
                await page.get_by_role("textbox", name="Data de início do acesso").fill(dataI[i-1])
                await page.get_by_role("textbox", name="Horário de início do acesso").fill(horaInicial)
                await page.get_by_role("textbox", name="Data de entrega").fill(dataF[i-1])
                await page.get_by_role("textbox", name="Hora de entrega").fill(horaFinal)
                await page.get_by_text("Editar datas e/ou horários de").click()
                await page.get_by_role("button", name="Editar datas").click()
                await page.wait_for_load_state('load')
                await page.wait_for_load_state('networkidle')
                await page.wait_for_timeout(2*1000)
                
            except Exception as e:
                print(f"Error adjusting Postagem - Etapa {i}: {e}")