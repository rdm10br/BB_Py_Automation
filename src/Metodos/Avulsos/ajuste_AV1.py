from playwright.async_api import Page
# from Metodos import getPlanilha


async def verify_calculated(page: Page, id_interno: str, item: str):
    
    api = f'./learn/api/v1/courses/{id_interno}/gradebook/columns'
    request = f'JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}" && item.calculationType=="CUSTOM").calculationType'
    request2 = f'JSON.parse(document.body.innerText).results.find(item => item.columnName == "{item}")'
    
    await page.goto(url=api, wait_until='networkidle')
    await page.wait_for_load_state('load')
    try:
        result = await page.evaluate(request)
        return str(result)
    except Exception as e:
        try:
            await page.evaluate(request2)
            return None
        except:
            print(e)
            result = 'Item not found'
            return result

async def createcalc(page: Page, id_interno: str, item: str):
    urlGradeBook = f'./ultra/courses/{id_interno}/grades?gradebookView=list'
    verify = await verify_calculated(page=page, id_interno=id_interno, item=item)
    timer_padrão = 1000*2
    # await page.pause()
    
    if verify == "CUSTOM":
        result = f'{item} is a calculated item'
        print('salvo pelo gongo')
        print(result)
        return result
    elif verify == 'Item not found':
        result = f'{item} Item not found'
        print(result)
        return result
    else:
        print(f'{item} is not a Calculated item')
        await page.goto(url=urlGradeBook, wait_until='commit')
        await page.wait_for_load_state('networkidle')
        await page.wait_for_load_state('load')
        await page.get_by_role("link", name="Nota atual").wait_for(state='visible', timeout=8*1000)
        try:
            # await page.get_by_label("Adicionar nova coluna do boletim de notas acima do(a) Nota atual").click(timeout=4*1000)
            # await page.locator("bb-grader-column").filter(has_text="AV2 Sem categoria").get_by_label("Adicionar nova coluna do").click(timeout=4*1000)
            await page.get_by_label("Adicionar nova coluna do boletim de notas abaixo do(a) AV2").nth(1).click(timeout=4*1000)
        except:
            try:
                # await page.locator("bb-grader-column").filter(has_text="AV1 Sem categoria").get_by_label("Adicionar nova coluna do").click(timeout=4*1000)
                await page.get_by_label("Adicionar nova coluna do boletim de notas abaixo do(a) AV1").nth(1).click(timeout=4*1000)
            except:
                await page.get_by_label("Adicionar nova coluna do boletim de notas abaixo do(a) AF").click(timeout=4*1000)
        await page.get_by_role("menuitem", name="Adicionar cálculo", exact=True).click()
        await page.get_by_label("Novo cálculo em undefined").fill(f"{item}")
        await page.get_by_text("Selecionar um esquema de notas").click()
        await page.wait_for_timeout(timer_padrão)
        await page.get_by_role("button", name="Total ").click()
        await page.wait_for_timeout(timer_padrão)
        await page.get_by_role("button", name="TOTAL ( )").click()
        await page.get_by_text(f"Trabalho do curso {item}", exact=True).click()
        await page.locator("ul").filter(has_text= f"TOTAL ( Trabalho do curso {item}").click()
        await page.wait_for_timeout(4*1000)
        await page.get_by_role("button", name="Salvar").click()
        await page.get_by_role("button", name="Fechar").click()
        await page.wait_for_load_state('load')
        await page.wait_for_timeout(4*1000)
        print(f'{item} Calculated item created!')
        
async def rebuceteio(
    page: Page,
    id_interno: str,
    item_list: list = ["AV1", "AV2", "AF"]
    ) -> str:
    result: list = []
    for item in item_list:
       try:
           await createcalc(page, id_interno, item)
       except Exception as e:
           print(f'{item} error: {e}')
           result.append(item)
    return str(result) if len(result) > 0 else 'OK'

async def ajusteFael(page: Page, id_interno: str) -> None:
    urlGradeBook = f'./ultra/courses/{id_interno}/grades?gradebookView=list'
    timer_padrão = 2*1000
    items = ['AV2', 'AF']
    
    for item in items:
        verify = await verify_calculated(page=page, id_interno=id_interno, item=item)
        if verify == "CUSTOM":
            result = f'{item} is a calculated item'
            print(result)
            await page.goto(urlGradeBook, wait_until='domcontentloaded')
            await page.wait_for_load_state('load')
            await page.get_by_role("link", name="Nota atual").wait_for(state='visible', timeout=4*timer_padrão)
            
            # await page.get_by_role("row", name=f"{item} Sem categoria Mais opções").click(timeout=timer_padrão)
            await page.get_by_role("row", name=f"{item} Sem categoria Mais opções").get_by_label("components.directives.element").click(timeout=timer_padrão)
            # await page.locator("bb-grader-column").filter(has_text=f"{item} Sem categoria").locator("path").click(timeout=timer_padrão)
            await page.locator("#gradebook-item-panel-content a").nth(2).click()
            try:
                await page.get_by_role("button", name="TOTAL ( )").hover(timeout=timer_padrão)
                await page.get_by_label("Remover função").click()
                await page.get_by_role("button", name="Total ").click()
                await page.wait_for_timeout(timer_padrão)
                await page.get_by_role("button", name="TOTAL ( )").click()
                
                match item:
                    case 'AV2':
                        item_case = 'Avaliação Objetiva'
                    case 'AF':
                        item_case = 'Exame Final'
                        
                await page.get_by_text(f"Trabalho do curso {item_case}").click()
                await page.get_by_role("button", name="TOTAL ( Trabalho do curso").click()
                await page.wait_for_timeout(timer_padrão)
                await page.get_by_role("button", name="Salvar").click()
                await page.get_by_role("button", name="Fechar").click()
                await page.wait_for_load_state('load')
                await page.wait_for_timeout(timer_padrão)
            except Exception as e:
                print(f'{item} error  in {id_interno}: {e}')
        elif verify == 'Item not found':
            result = f'{item} Item not found in {id_interno}'
            print(result)