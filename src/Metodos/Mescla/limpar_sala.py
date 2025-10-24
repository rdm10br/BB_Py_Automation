from playwright.async_api import Page

async def limpar_sala_root(page: Page, id_interno: str) -> None:
    
    await page.goto(f"./webapps/blackboard/execute/recycler?course_id={id_interno}&action=select&context=SYSTEM&sourceType=COURSES")
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("load")
    
    print(f"Iniciando limpeza da sala: {id_interno} via root...")
    await page.get_by_role("checkbox", name="ROOT").check()
    await page.get_by_role("checkbox", name="INTERACTIVE").check()
    await page.get_by_role("checkbox", name="INDIRECT").check()
    await page.get_by_role("checkbox", name="Avisos").check()
    await page.get_by_role("checkbox", name="Contatos").check()
    await page.get_by_role("checkbox", name="Usuários").check()
    await page.get_by_role("checkbox", name="Grupos").check()
    await page.get_by_role("checkbox", name="Fórum de discussão").check()
    await page.get_by_role("checkbox", name="Testes, Pesquisas e Bancos de").check()
    await page.get_by_role("checkbox", name="Colunas do Centro de Notas").check()
    await page.get_by_role("checkbox", name="Estatísticas").check()
    await page.get_by_role("checkbox", name="Glossário").check()
    await page.get_by_role("checkbox", name="Blogs").check()
    await page.get_by_role("checkbox", name="Diários").check()
    await page.get_by_role("checkbox", name="Mensagens do curso").check()
    await page.get_by_role("textbox", name="* Digite \"Excluir\" para").fill("Excluir")
    print("Selecionado todos os itens para exclusão.")
    await page.locator("#stepcontent3 div").nth(1).click()
    await page.get_by_role("button", name="Enviar").click()
    
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("load")
    
    await page.goto(f"./ultra/courses/{id_interno}/grades?gradebookView=list")
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("load")
    
    print("Iniciando limpeza do Gradebook...")
    await page.get_by_role("button", name="Mais opções para Nota atual").click()
    # await page.locator("#grader-column-open-button-id_2_trash").click()
    await page.locator('//html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/bb-course-grades-grader/div/div[2]/div/div/bb-course-grades-grader-list/table/tbody/tr[2]/td[7]/div/bb-overflow-menu/div/ul/li[2]/a').click()
    await page.get_by_role("button", name="Excluir").click()
    print("Gradebook limpo com sucesso.")
    
    print(f"Limpeza da sala: {id_interno} concluída com sucesso.")
    
    return