from playwright.async_api import Page


async def ajusteConsu(page: Page, id_interno: str) -> None:

    item = "Regras da Avaliação - Resolução CONSU"
            
    await page.goto(f"./learn/api/public/v1/courses/{id_interno}/contents?title=Avaliações")
    try:
        id_folder = await page.evaluate('JSON.parse(document.body.innerText).results[0].id')
        await page.goto(f"./learn/api/public/v1/courses/{id_interno}/contents/{id_folder}/children?title={item}")
        available = str(await page.evaluate('JSON.parse(document.body.innerText).results[0].availability.available')).lower()
        
        if available == "yes":
            await page.goto(f"./ultra/courses/{id_interno}/outline?search={item}")
            await page.wait_for_load_state("networkidle")
            await page.wait_for_load_state("domcontentloaded")
            # await page.locator("div").filter(has_text="Regras da Avaliação - Resolução CONSUO").nth(2).wait_for(state="visible", timeout=10*1000)
            await page.get_by_role("button", name="Visível para alunos").click()
            await page.get_by_role("option", name="Oculto para alunos").click()
            await page.wait_for_load_state("networkidle")
            await page.wait_for_load_state("domcontentloaded")
            print(f"{item} : está oculta para os alunos.")
        else:
            print(f"{item} : já está oculta para os alunos.")
    except Exception as e:
        print(f"{item} : not found in room {id_interno}")