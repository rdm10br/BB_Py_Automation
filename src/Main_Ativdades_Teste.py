import asyncio, time
from playwright.async_api import Page
from Metodos import getPlanilha, getFromAPI, gruposAtividades, AjusteNotaZero
from Decorators.Main_StartUp import playwright_StartUp

@playwright_StartUp
async def run(page: Page, index) -> None:
    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)
    
    
    classURL = f'./ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'
    
    print(id_externo)
    
    await page.goto(classUrlUltra)
    
    await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)
    
    course_area = await getFromAPI.API_Ativ_Course(page=page, id_externo=id_externo)
    
    course_mapping = {
        "['Educação I']": [
            'Formação de Docente para Educação Básica - Pedagogia',
            'Formação Pedagógica em Matemática para Graduados',
            'Formação Pedagógica em Pedagogia para Graduados',
            'Segunda Licenciatura em Geografia',
            'Segunda Licenciatura em História',
            'Segunda Licenciatura em Letras - Português',
            'Segunda Licenciatura em Matemática',
            'Segunda Licenciatura em Pedagogia'
        ],
        "['Educação II']": [
            "Ciências Biológicas",
            "Geografia",
            "História",
            "Letras - Espanhol",
            "Letras - Inglês",
            "Letras - Português",
            "Letras - Português e Espanhol",
            "Licenciatura em Educação Especial",
            "Licenciatura em Educação Física",
            "Matemática"
        ],
        "['Educação III']": [
            "Pedagogia"
        ],
        "['Exatas']": [
            "Ciências Aeronáuticas",
            "Engenharia Civil",
            "Engenharia de Produção",
            "Engenharia Elétrica",
            "Engenharia Mecânica"
        ],
        "['Negócios e Gestão I']": [
            "Administração",
            "Ciências Contábeis",
            "Ciências Econômicas",
            "Gestão Hospitalar"
        ],
        "['Negócios e Gestão II']": [
            "Gastronomia",
            "Gestão Ambiental",
            "Gestão da Qualidade",
            "Gestão de Recursos Humanos",
            "Gestão Financeira",
            "Negócios Imobiliários"
        ],
        "['Negócios e Gestão III']": [
            "E-Commerce",
            "Gestão Comercial",
            "Gestão de Trânsito",
            "Logística",
            "Processos Gerenciais"
        ],
        "['Saúde I']": [
            "Biomedicina",
            "Enfermagem",
            "Farmácia"
        ],
        "['Saúde II']": [
            "Estética e Cosmética",
            "Podologia"
        ],
        "['Saúde III']": [
            "Bacharelado em Educação Física",
            "Fisioterapia",
            "Nutrição",
            "Terapia Ocupacional"
        ],
        "['Serviço Social e Teologia']": [
            "Serviço Social",
            "Teologia"
        ],
        "['Tecnologia da Informação']": [
            "Analise e Desenvolvimento de Sistema",
            "Ciência De Dados/Data Science",
            "Coding",
            "Computação Em Nuvem",
            "Digital Security",
            "Empreendedorismo Digital",
            "Experiência do Usuário e Modelagem de Projetos Inovadores",
            "Game Design",
            "Inteligência Artificial",
            "Internet das Coisas",
            "Service Design",
            "Tecnologia da Informação"
        ],
        "['Arquitetura e Design']": [
            "Arquitetura e Urbanismo",
            "Design de Interiores"
        ],
        "['Comunicação']": [
            "Coaching Digital",
            "Coaching e Mentoring",
            "Filmmaker",
            "Marketing",
            "Streaming Profissional"
        ],
        "['Negócios e Gestão IV']": [
            "Ciência Política",
            "Gestão da Qualidade",
            "Gestão de Serviços Jurídicos, Cartorários e Notariais",
            "Gestão de Serviços Jurídicos e Notariais",
            "Gestão Pública",
            "Segurança Pública"
        ]
    }
    
    async def process_courses(page: Page, id_interno: str, course_area: str, cursos: list, index: int):
        await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
        print(course_area)
        
        start_time0 = time.time()
        for curso in cursos:
            await gruposAtividades.inserirGruposAtividadesAV1(page=page, id_interno=id_interno, curso=curso)
            await page.wait_for_load_state('load')
            await gruposAtividades.inserirGruposAtividadesAV2(page=page, id_interno=id_interno, curso=curso)
            await page.wait_for_load_state('load')
        end_time0 = time.time()
        execution_time = end_time0 - start_time0
        executionTime0 = f'Execution time: {'{:.2f}'.format(execution_time)} seconds'
        print(executionTime0)
        
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
    
    if course_area in course_mapping:
        await process_courses(page, id_interno, course_area, course_mapping[course_area], index)
    else:
        print(f'Grande Área da sala {id_externo} não identificada; {course_area}')
        getPlanilha.writeOnExcel_Plan1(index=index, return_status='Não identificado')


async def main():
    await run()

asyncio.run(main())
