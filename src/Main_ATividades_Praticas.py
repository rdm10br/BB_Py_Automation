import asyncio
from playwright.async_api import Page, expect


from Metodos import getPlanilha, getFromAPI, gruposAtividades, AjusteNotaZero
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
        
        await AjusteNotaZero.AjusteNotaZero(page=page, id_interno=id_interno)
        
        course_area = str(await getFromAPI.API_Ativ_Course(page=page, id_externo=id_externo))
        
        if course_area == "['Educação I']" :
                
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   'Formação de Docente para Educação Básica - Pedagogia',
                        'Formação Pedagógica em Matemática para Graduados',
                        'Formação Pedagógica em Pedagogia para Graduados',
                        'Segunda Licenciatura em Geografia',
                        'Segunda Licenciatura em História',
                        'Segunda Licenciatura em Letras - Português',
                        'Segunda Licenciatura em Matemática',
                        'Segunda Licenciatura em Pedagogia']
                                    
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Educação II']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Ciências Biológicas",
                        "Geografia",
                        "História",
                        "Letras - Espanhol",
                        "Letras - Inglês",
                        "Letras - Português",
                        "Letras - Português e Espanhol",
                        "Licenciatura em Educação Especial",
                        "Licenciatura em Educação Física",
                        "Matemática"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Educação III']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Pedagogia"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Exatas']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Ciências Aeronáuticas",
                        "Engenharia Civil",
                        "Engenharia de Produção",
                        "Engenharia Elétrica",
                        "Engenharia Mecânica"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão I']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Administração",
                        "Ciências Contábeis",
                        "Ciências Econômicas",
                        "Gestão Hospitalar"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão II']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Gastronomia",
                        "Gestão Ambiental",
                        "Gestão da Qualidade",
                        "Gestão de Recursos Humanos",
                        "Gestão Financeira",
                        "Negócios Imobiliários"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão III']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "E-Commerce",
                        "Gestão Comercial",
                        "Gestão de Trânsito",
                        "Logística",
                        "Processos Gerenciais"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Saúde I']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Biomedicina",
                        "Enfermagem",
                        "Farmácia"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Saúde II']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Estética e Cosmética",
                        "Podologia"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Saúde III']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Bacharelado em Educação Física",
                        "Fisioterapia",
                        "Nutrição",
                        "Terapia Ocupacional"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Serviço Social e Teologia']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Serviço Social",
                        "Teologia"]
                
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Tecnologia da Informação']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Analise e Desenvolvimento de Sistema",
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
                        "Tecnologia da Informação"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Arquitetura e Design']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Arquitetura e Urbanismo",
                        "Design de Interiores"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Comunicação']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Coaching Digital",
                        "Coaching e Mentoring",
                        "Filmmaker",
                        "Marketing",
                        "Streaming Profissional"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                i+=1
            
            getPlanilha.writeOnExcel_Plan1(index=index, return_status='OK')
            pass
        elif course_area == "['Negócios e Gestão IV']":
            
            await gruposAtividades.inserirArquivo(page=page, id_interno=id_interno, Area=course_area)
            print(course_area)
            curso = [   "Ciência Política",
                        "Gestão da Qualidade",
                        "Gestão de Serviços Jurídicos, Cartorários e Notariais",
                        "Gestão de Serviços Jurídicos e Notariais",
                        "Gestão Pública",
                        "Segurança Pública"]
            
            for i in range(len(curso)):
                await gruposAtividades.inserirGruposAtividadesAV1(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
                await gruposAtividades.inserirGruposAtividadesAV2(page=page,
                                                            id_interno=id_interno, curso=curso[i])
                await page.wait_for_load_state('load')
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