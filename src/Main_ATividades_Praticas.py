import asyncio
from playwright.async_api import Page, expect


from Metodos import getPlanilha, getFromAPI, gruposAtividades
from Decorators.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        baseURL = 'https://sereduc.blackboard.com/'
        classURL = f'{baseURL}ultra/courses/'
        classUrlUltra = f'{classURL}{id_interno}/outline'
        
        print(id_externo)
        
        await page.goto(classUrlUltra)
        
        course_area = str(await getFromAPI.API_Ativ_Course(page=page, id_externo=id_externo))
            
        if course_area == "['Educação I']" :
                
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
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
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Educação II']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
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
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Educação III']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Pedagogia"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Exatas']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Engenharia Civil",
                        "Engenharia de Produção",
                        "Engenharia Elétrica",
                        "Engenharia Mecânica",
                        "Ciências Aeronáuticas"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão I']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Administração",
                        "Ciências Contábeis",
                        "Ciências Econômicas",
                        "Gestão Hospitalar"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão II']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
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
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão III']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Ciência Política",
                        "Gestão de Serviços Jurídicos e Notariais",
                        "Gestão Pública",
                        "Segurança Pública"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Saúde I']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Farmácia",
                        "Enfermagem",
                        "Biomedicina"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Saúde II']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Estética e Cosmética",
                        "Podologia"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Saúde III']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Bacharelado em Educação Física",
                        "Fisioterapia",
                        "Terapia Ocupacional",
                        "Nutrição"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Serviço Social e Teologia']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Serviço Social",
                        "Teologia"]
                
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Tecnologia da Informação']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
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
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Arquitetura e Design']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = ["Arquitetura E Urbanismo",
                        "Design de Interiores"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        else :
            print(f'Grande Área da sala {id_externo} não identificada; {course_area}')
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='Não identificado')
            pass

async def main():
    await run()

asyncio.run(main())