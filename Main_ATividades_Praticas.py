import asyncio, gc
from playwright.async_api import Playwright, async_playwright, expect


from Metodos import checkup_login, getFromAPI, getPlanilha, gruposAtividades


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    
    # Access page
    await page.goto(baseURL)
    
    # Verificar se está logado e logar
    await checkup_login.checkup_login(page=page)

    total_lines_plan1 = getPlanilha.total_lines
    
    cookies = await page.context.cookies(urls=baseURL)
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_browser = await playwright.chromium.launch(headless=False)
            new_context = await new_browser.new_context(no_viewport=True)
            # Assuming 'cookies' is the list of cookies obtained earlier
            await new_context.add_cookies(cookies)
            new_page = await new_context.new_page()
            
            #request from API
            id_externo = await getPlanilha.getCell(index=index)
            id_interno = await getFromAPI.API_Req(page=new_page, index=index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
        
            print(id_externo)
            await new_page.goto(classUrlUltra)
            
            course_area = str(getFromAPI.API_Ativ_Course(playwright=playwright, id_interno=id_interno))
            
            if course_area == "['Educação I']" :
                
                await gruposAtividades.inserirArquivoEducI(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ['Formação Pedagógica em Matemática para Graduados',
                         'Formação Pedagógica em Pedagogia para Graduados',
                         'Formação de Docente para a Educação Básica - Geografia',
                         'Formação de Docente para a Educação Básica - História',
                         'Formação de Docente para a Educação Básica - Letras',
                         'Segunda Licenciatura em Geografia',
                         'Segunda Licenciatura em História',
                         'Segunda Licenciatura em Letras - Espanhol',
                         'Segunda Licenciatura em Letras - Inglês',
                         'Segunda Licenciatura em Letras - Português',
                         'Segunda Licenciatura em Matemática',
                         'Segunda Licenciatura em Pedagogia']
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Educação II']":
                
                await gruposAtividades.inserirArquivoEducII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Licenciatura em Educação Especial",
                         "Licenciatura em Educação Física",
                         "Geografia",
                         "História",
                         "Ciências Biológicas",
                         "Matemática",
                         "Letras - Espanhol",
                         "Letras - Inglês",
                         "Letras - Português"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Educação III']":
                
                await gruposAtividades.inserirArquivoEducIII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Pedagogia"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright,
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Exatas']":
                
                await gruposAtividades.inserirArquivoExat(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Engenharia Civil",
                         "Engenharia de Produção",
                         "Engenharia Elétrica",
                         "Engenharia Mecânica",
                         "Ciências Aeronáuticas"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Negócios e Gestão I']":
                
                await gruposAtividades.inserirArquivoNegI(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Administração",
                         "Ciências Contábeis",
                         "Ciências Econômicas",
                         "Gestão Hospitalar"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Negócios e Gestão II']":
                
                await gruposAtividades.inserirArquivoNegII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Gestão Financeira",
                         "Gestão Ambiental",
                         "Gastronomia",
                         "Gestão da Qualidade",
                         "Gestão Comercial com Complementação de Estudos em Gestão de E-Commerce",
                         "E-Commerce",
                         "Gestão de Recursos Humanos",
                         "Logística",
                         "Gestão de Trânsito",
                         "Gestão Comercial",
                         "Processos Gerenciais",
                         "Negócios Imobiliários"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Negócios e Gestão III']":
                
                await gruposAtividades.inserirArquivoNegIII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Ciência Política",
                         "Gestão de Serviços Jurídicos e Notariais",
                         "Gestão Pública",
                         "Segurança Pública"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Saúde I']":
                
                await gruposAtividades.inserirArquivoSaudI(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Farmácia",
                         "Enfermagem",
                         "Biomedicina"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Saúde II']":
                
                await gruposAtividades.inserirArquivoSaudII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Estética e Cosmética",
                         "Podologia"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Saúde III']":
                
                await gruposAtividades.inserirArquivoSaudIII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Bacharelado em Educação Física",
                         "Fisioterapia",
                         "Terapia Ocupacional",
                         "Nutrição"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Serviço Social e Teologia']":
                
                await gruposAtividades.inserirArquivoServ(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Serviço Social",
                         "Teologia"]
                 
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Tecnologia da Informação']":
                
                await gruposAtividades.inserirArquivoInfo(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Analise e Desenvolvimento de Sistema",
                         "Ciência De Dados - Data Science",
                         "Coding",
                         "Computação Em Nuvem",
                         "Digital Security",
                         "Empreendedorismo Digital",
                         "Experiência do Usuário e Modelagem de Projetos Inovadores",
                         "Game Design",
                         "Tecnologia da Informação",
                         "Inteligência Artificial",
                         "Internet das Coisas",
                         "Service Design"]
                
                for i in range(len(curso)):
                    await gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    await gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                await getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            else :
                print(f'Grande Área da sala {id_externo} não identificada; {course_area}')
                pass
            
        
            await new_context.close() 
            await new_browser.close()  
            
            # Force garbage collection
            await gc.collect() 

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())