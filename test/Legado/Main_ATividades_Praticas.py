from playwright.sync_api import Playwright, sync_playwright, expect
import gc

from Metodos import checkup_login, getFromAPI, getPlanilha, gruposAtividades

def run(playwright: Playwright) -> None:
    # Connect to the existing browser
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # Access page context
    context = browser.contexts[0]
    page = context.pages[0]
    
    baseURL = "https://sereduc.blackboard.com/"
    classURL = f'{baseURL}ultra/courses/'
    
    # Access page
    page.goto(baseURL)
    
    # Verificar se está logado e logar
    checkup_login.checkup_login(playwright=playwright)

    total_lines_plan1 = getPlanilha.total_lines
    
    context.new_page()
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index=index)
        
        if cell_status != 'nan':
            pass
        else :
            new_page = context.pages[1]
            page = context.pages[0]
            
            page.close()
            
            #request from API
            id_externo = getPlanilha.getCell(index=index)
            id_interno = getFromAPI.API_Req(playwright=playwright, index=index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
        
            print(id_externo)
            new_page.goto(classUrlUltra)
            
            course_area = str(getFromAPI.API_Ativ_Course(playwright=playwright, id_interno=id_interno))
            
            if course_area == "['Educação I']" :
                
                gruposAtividades.inserirArquivoEducI(playwright=playwright, id_interno=id_interno)
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
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Educação II']":
                
                gruposAtividades.inserirArquivoEducII(playwright=playwright, id_interno=id_interno)
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
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Educação III']":
                
                gruposAtividades.inserirArquivoEducIII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Pedagogia"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright,
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Exatas']":
                
                gruposAtividades.inserirArquivoExat(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Engenharia Civil",
                         "Engenharia de Produção",
                         "Engenharia Elétrica",
                         "Engenharia Mecânica",
                         "Ciências Aeronáuticas"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Negócios e Gestão I']":
                
                gruposAtividades.inserirArquivoNegI(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Administração",
                         "Ciências Contábeis",
                         "Ciências Econômicas",
                         "Gestão Hospitalar"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Negócios e Gestão II']":
                
                gruposAtividades.inserirArquivoNegII(playwright=playwright, id_interno=id_interno)
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
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Negócios e Gestão III']":
                
                gruposAtividades.inserirArquivoNegIII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Ciência Política",
                         "Gestão de Serviços Jurídicos e Notariais",
                         "Gestão Pública",
                         "Segurança Pública"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Saúde I']":
                
                gruposAtividades.inserirArquivoSaudI(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Farmácia",
                         "Enfermagem",
                         "Biomedicina"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Saúde II']":
                
                gruposAtividades.inserirArquivoSaudII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Estética e Cosmética",
                         "Podologia"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Saúde III']":
                
                gruposAtividades.inserirArquivoSaudIII(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Bacharelado em Educação Física",
                         "Fisioterapia",
                         "Terapia Ocupacional",
                         "Nutrição"]
                
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Serviço Social e Teologia']":
                
                gruposAtividades.inserirArquivoServ(playwright=playwright, id_interno=id_interno)
                print(course_area)
                curso = ["Serviço Social",
                         "Teologia"]
                 
                for i in range(len(curso)):
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            elif course_area == "['Tecnologia da Informação']":
                
                gruposAtividades.inserirArquivoInfo(playwright=playwright, id_interno=id_interno)
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
                    gruposAtividades.inserirGruposAtividadesAV1(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.inserirGruposAtividadesAV2(playwright=playwright, 
                                                                id_interno=id_interno, curso=curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                # Função para escrever na primeira planilha
                getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
                pass
            else :
                print(f'Grande Área da sala {id_externo} não identificada; {course_area}')
                pass
            
            context.new_page()
            
            # Force garbage collection
            gc.collect()
        
    context.close()

with sync_playwright() as playwright:
    run(playwright)