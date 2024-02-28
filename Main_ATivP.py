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
            
            gruposAtividades.openFolderAV1(playwright,id_interno)
            gruposAtividades.openFolderAV2(playwright,id_interno)
            
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
                gruposAtividades.openFolderAV1(playwright,id_interno)
                gruposAtividades.openFolderAV2(playwright,id_interno)
            
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
                gruposAtividades.openFolderAV1(playwright,id_interno)
                gruposAtividades.openFolderAV2(playwright,id_interno)
            
            if course_area == "['Educação I']" :
                gruposAtividades.inserirArquivoEducI(playwright ,id_interno)
                curso1 = "Formação Pedagógica em Matemática para Graduados"
                curso2 = "Formação Pedagógica em Pedagogia para Graduados"
                curso3 = "Formação de Docente para a Educação Básica - Geografia"
                curso4 = "Formação de Docente para a Educação Básica - História"
                curso5 = "Formação de Docente para a Educação Básica - Letras"
                curso7 = "Segunda Licenciatura em Geografia"
                curso8 = "Segunda Licenciatura em História"
                curso9 = "Segunda Licenciatura em Letras - Espanhol"
                curso10 = "Segunda Licenciatura em Letras - Inglês"
                curso11 = "Segunda Licenciatura em Letras - Português"
                curso12 = "Segunda Licenciatura em Matemática"
                curso13 = "Segunda Licenciatura em Pedagogia"
                
                inserirGruposAtividadesAV1(curso1)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso2)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso3)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso4)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso5)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso7)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso8)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso9)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso10)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso11)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso12)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso13)
                page.wait_for_load_state('load')
                
                inserirGruposAtividadesAV2(curso1)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso2)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso3)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso4)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso5)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso7)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso8)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso9)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso10)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso11)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso12)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso13)
                page.wait_for_load_state('load')                
                
            elif course_area == "['Educação II']":
                gruposAtividades.inserirArquivoEducII(playwright,id_interno)
                curso1 = "Licenciatura em Educação Especial"
                curso2 = "Licenciatura em Educação Física"
                curso3 = "Geografia"
                curso4 = "História"
                curso5 = "Ciências Biológicas"
                curso6 = "Matemática"
                curso7 = "Letras - Espanhol"
                curso8 = "Letras - Inglês"
                curso9 = "Letras - Português"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                inserirGruposAtividadesAV1(curso4)
                inserirGruposAtividadesAV1(curso5)
                inserirGruposAtividadesAV1(curso6)
                inserirGruposAtividadesAV1(curso7)
                inserirGruposAtividadesAV1(curso8)
                inserirGruposAtividadesAV1(curso9)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                inserirGruposAtividadesAV2(curso4)
                inserirGruposAtividadesAV2(curso5)
                inserirGruposAtividadesAV2(curso6)
                inserirGruposAtividadesAV2(curso7)
                inserirGruposAtividadesAV2(curso8)
                inserirGruposAtividadesAV2(curso9)
                
            elif course_area == "['Educação III']":
                gruposAtividades.inserirArquivoEducIII(playwright,id_interno)
                curso1 = "Pedagogia"
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV2(curso1)
                
            elif course_area == "['Exatas']":
                gruposAtividades.inserirArquivoExat(playwright,id_interno)
                curso1 = "Engenharia Civil"
                curso2 = "Engenharia de Produção"
                curso3 = "Engenharia Elétrica"
                curso4 = "Engenharia Mecânica"
                curso5 = "Ciências Aeronáuticas"
                
                inserirGruposAtividadesAV1(curso1)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso2)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso3)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso4)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV1(curso5)
                page.wait_for_load_state('load')
                
                inserirGruposAtividadesAV2(curso1)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso2)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso3)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso4)
                page.wait_for_load_state('load')
                inserirGruposAtividadesAV2(curso5)
                page.wait_for_load_state('load')
                
            elif course_area == "['Negócios e Gestão I']":
                gruposAtividades.inserirArquivoNegI(playwright,id_interno)
                curso1 = "Administração"
                curso2 = "Ciências Contábeis"
                curso3 = "Ciências Econômicas"
                curso4 = "Gestão Hospitalar"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                inserirGruposAtividadesAV1(curso4)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                inserirGruposAtividadesAV2(curso4)
                
            elif course_area == "['Negócios e Gestão II']":
                gruposAtividades.inserirArquivoNegII(playwright,id_interno)
                curso1 = "Gestão Financeira"
                curso2 = "Gestão Ambiental"
                curso3 = "Gastronomia"
                curso4 = "Gestão da Qualidade"
                curso5 = "Gestão Comercial com Complementação de Estudos em Gestão de E-Commerce"
                curso6 = "E-Commerce"
                curso7 = "Gestão de Recursos Humanos"
                curso8 = "Logística"
                curso9 = "Gestão de Trânsito"
                curso10 = "Gestão Comercial"
                curso11 = "Processos Gerenciais"
                curso12 = "Negócios Imobiliários"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                inserirGruposAtividadesAV1(curso4)
                inserirGruposAtividadesAV1(curso5)
                inserirGruposAtividadesAV1(curso6)
                inserirGruposAtividadesAV1(curso7)
                inserirGruposAtividadesAV1(curso8)
                inserirGruposAtividadesAV1(curso9)
                inserirGruposAtividadesAV1(curso10)
                inserirGruposAtividadesAV1(curso11)
                inserirGruposAtividadesAV1(curso12)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                inserirGruposAtividadesAV2(curso4)
                inserirGruposAtividadesAV2(curso5)
                inserirGruposAtividadesAV2(curso6)
                inserirGruposAtividadesAV2(curso7)
                inserirGruposAtividadesAV2(curso8)
                inserirGruposAtividadesAV2(curso9)
                inserirGruposAtividadesAV2(curso10)
                inserirGruposAtividadesAV2(curso11)
                inserirGruposAtividadesAV2(curso12)
                
            elif course_area == "['Negócios e Gestão III']":
                gruposAtividades.inserirArquivoNegIII(playwright,id_interno)
                curso1 = "Ciência Política"
                curso2 = "Gestão de Serviços Jurídicos e Notariais"
                curso3 = "Gestão Pública"
                curso4 = "Segurança Pública"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                inserirGruposAtividadesAV1(curso4)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                inserirGruposAtividadesAV2(curso4)
                
            elif course_area == "['Saúde I']":
                gruposAtividades.inserirArquivoSaudI(playwright,id_interno)
                curso1 = "Farmácia"
                curso2 = "Enfermagem"
                curso3 = "Biomedicina"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                
            elif course_area == "['Saúde II']":
                gruposAtividades.inserirArquivoSaudII(playwright,id_interno)
                curso1 = "Estética e Cosmética"
                curso2 = "Podologia"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                
            elif course_area == "['Saúde III']":
                gruposAtividades.inserirArquivoSaudIII(playwright,id_interno)
                curso1 = "Bacharelado em Educação Física"
                curso2 = "Fisioterapia"
                curso3 = "Terapia Ocupacional"
                curso4 = "Nutrição"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                inserirGruposAtividadesAV1(curso4)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                inserirGruposAtividadesAV2(curso4)
                
            elif course_area == "['Serviço Social e Teologia']":
                gruposAtividades.inserirArquivoServ(playwright,id_interno)
                curso1 = "Serviço Social"
                curso2 = "Teologia"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                
            elif course_area == "['Tecnologia da Informação']":
                gruposAtividades.inserirArquivoInfo(playwright,id_interno)
                curso1 = "Analise e Desenvolvimento de Sistema"
                curso2 = "Ciência De Dados/Data Science"
                curso3 = "Coding"
                curso4 = "Computação Em Nuvem"
                curso5 = "Digital Security"
                curso6 = "Empreendedorismo Digital"
                curso7 = "Experiência do Usuário e Modelagem de Projetos Inovadores"
                curso8 = "Game Design"
                curso9 = "Tecnologia da Informação"
                curso10 = "Inteligência Artificial"
                curso11 = "Internet das Coisas"
                curso12 = "Service Design"
                
                inserirGruposAtividadesAV1(curso1)
                inserirGruposAtividadesAV1(curso2)
                inserirGruposAtividadesAV1(curso3)
                inserirGruposAtividadesAV1(curso4)
                inserirGruposAtividadesAV1(curso5)
                inserirGruposAtividadesAV1(curso6)
                inserirGruposAtividadesAV1(curso7)
                inserirGruposAtividadesAV1(curso8)
                inserirGruposAtividadesAV1(curso9)
                inserirGruposAtividadesAV1(curso10)
                inserirGruposAtividadesAV1(curso11)
                inserirGruposAtividadesAV1(curso12)
                
                inserirGruposAtividadesAV2(curso1)
                inserirGruposAtividadesAV2(curso2)
                inserirGruposAtividadesAV2(curso3)
                inserirGruposAtividadesAV2(curso4)
                inserirGruposAtividadesAV2(curso5)
                inserirGruposAtividadesAV2(curso6)
                inserirGruposAtividadesAV2(curso7)
                inserirGruposAtividadesAV2(curso8)
                inserirGruposAtividadesAV2(curso9)
                inserirGruposAtividadesAV2(curso10)
                inserirGruposAtividadesAV2(curso11)
                inserirGruposAtividadesAV2(curso12)
                
            else :
                print(f'Grande Área da sala {id_externo} não identificada')
                pass
            
            context.new_page()
            
            # Force garbage collection
            gc.collect()
        
    context.close()

with sync_playwright() as playwright:
    run(playwright)