from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import *
import gc

from Metodos.Login import checkup_login
from Metodos.API import getFromAPI ,getPlanilha
from Metodos.Mescla import gruposAtividades

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
    checkup_login.checkup_login(playwright)

    total_lines_plan1 = getPlanilha.total_lines
    
    context.new_page()
    
    for index in range(total_lines_plan1) :
        index +=1
        
        cell_status = getPlanilha.getCell_status(index)
        
        if cell_status == 'OK':
            pass
        else :
            new_page = context.pages[1]
            page = context.pages[0]
            
            page.close()
            
            #request from API
            id_externo = getPlanilha.getCell(index)
            id_interno = getFromAPI.API_Req(playwright,index)
            
            classUrlUltra = f'{classURL}{id_interno}/outline'
        
            print(id_externo)
            new_page.goto(classUrlUltra)
            
            course_area = str(getFromAPI.API_Ativ_Course(playwright,id_externo))
            
            def inserirGruposAtividadesAV1(curso):
                item = f'Envio AV1 - Atividade Prática de Extensão ({curso})'
                new_page.get_by_role("link", name=item, exact=True).click()
                new_page.get_by_role("button", name="Condições de liberação").click()
                new_page.get_by_role("menuitem", name="Condições de liberação").click()
                new_page.get_by_label("Membros ou grupos específicos").check()
                new_page.get_by_label("Membros ou grupos específicos").fill(curso)
                new_page.get_by_role("button", name="Salvar").click()
                new_page.wait_for_load_state('load')
                new_page.goto(classUrlUltra)
                new_page.wait_for_load_state('networkidle')
            
            def inserirGruposAtividadesAV2(curso):
                item = f'Envio AV1 - Atividade Prática de Extensão ({curso})'
                new_page.get_by_role("link", name=item, exact=True).click()
                new_page.get_by_role("button", name="Condições de liberação").click()
                new_page.get_by_role("menuitem", name="Condições de liberação").click()
                new_page.get_by_label("Membros ou grupos específicos").check()
                new_page.get_by_label("Membros ou grupos específicos").fill(curso)
                new_page.get_by_role("button", name="Salvar").click()
                new_page.wait_for_load_state('load')
                new_page.goto(classUrlUltra)
                new_page.wait_for_load_state('networkidle')
            
            if course_area == "['Educação I']" :
                gruposAtividades.inserirArquivoEducI(playwright ,id_interno)
                curso = ['Formação Pedagógica em Matemática para Graduados','Formação Pedagógica em Pedagogia para Graduados','Formação de Docente para a Educação Básica - Geografia','Formação de Docente para a Educação Básica - História','Formação de Docente para a Educação Básica - Letras','Formação de Docente para a Educação Básica - História','Segunda Licenciatura em Geografia','Segunda Licenciatura em História','Segunda Licenciatura em Letras - Espanhol','Segunda Licenciatura em Letras - Inglês','Segunda Licenciatura em Letras - Português','Segunda Licenciatura em Matemática','Segunda Licenciatura em Pedagogia']
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1               
                
            elif course_area == "['Educação II']":
                gruposAtividades.inserirArquivoEducII(playwright,id_interno)
                curso = ["Licenciatura em Educação Especial","Licenciatura em Educação Física","Geografia","História","Ciências Biológicas","Matemática","Letras - Espanhol","Letras - Inglês","Letras - Português"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Educação III']":
                gruposAtividades.inserirArquivoEducIII(playwright,id_interno)
                curso = ["Pedagogia"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Exatas']":
                gruposAtividades.inserirArquivoExat(playwright,id_interno)
                curso = ["Engenharia Civil","Engenharia de Produção","Engenharia Elétrica","Engenharia Mecânica","Ciências Aeronáuticas"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Negócios e Gestão I']":
                gruposAtividades.inserirArquivoNegI(playwright,id_interno)
                curso = ["Administração","Ciências Contábeis","Ciências Econômicas","Gestão Hospitalar"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Negócios e Gestão II']":
                gruposAtividades.inserirArquivoNegII(playwright,id_interno)
                curso = ["Gestão Financeira","Gestão Ambiental","Gastronomia","Gestão da Qualidade","Gestão Comercial com Complementação de Estudos em Gestão de E-Commerce","E-Commerce","Gestão de Recursos Humanos","Logística","Gestão de Trânsito","Gestão Comercial","Processos Gerenciais","Negócios Imobiliários"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Negócios e Gestão III']":
                gruposAtividades.inserirArquivoNegIII(playwright,id_interno)
                curso = ["Ciência Política","Gestão de Serviços Jurídicos e Notariais","Gestão Pública","Segurança Pública"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Saúde I']":
                gruposAtividades.inserirArquivoSaudI(playwright,id_interno)
                curso = ["Farmácia","Enfermagem","Biomedicina"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Saúde II']":
                gruposAtividades.inserirArquivoSaudII(playwright,id_interno)
                curso = ["Estética e Cosmética","Podologia"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Saúde III']":
                gruposAtividades.inserirArquivoSaudIII(playwright,id_interno)
                curso = ["Bacharelado em Educação Física","Fisioterapia","Terapia Ocupacional","Nutrição"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Serviço Social e Teologia']":
                gruposAtividades.inserirArquivoServ(playwright,id_interno)
                curso = ["Serviço Social","Teologia"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            elif course_area == "['Tecnologia da Informação']":
                gruposAtividades.inserirArquivoInfo(playwright,id_interno)
                curso = ["Analise e Desenvolvimento de Sistema","Ciência De Dados/Data Science","Coding","Computação Em Nuvem","Digital Security","Empreendedorismo Digital","Experiência do Usuário e Modelagem de Projetos Inovadores","Game Design","Tecnologia da Informação","Inteligência Artificial","Internet das Coisas","Service Design"]
                
                for i in range(len(curso)):
                    gruposAtividades.openFolderAV1(playwright,id_interno)
                    inserirGruposAtividadesAV1(curso[i])
                    page.wait_for_load_state('load')
                    gruposAtividades.openFolderAV2(playwright,id_interno)
                    inserirGruposAtividadesAV2(curso[i])
                    page.wait_for_load_state('load')
                    i+=1
                
            else :
                print(f'Grande Área da sala {id_externo} não identificada')
                pass
            
            context.new_page()
            
            # Force garbage collection
            gc.collect()
        
    context.close()

with sync_playwright() as playwright:
    run(playwright)