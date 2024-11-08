from playwright.async_api import Page, expect
from Metodos import getApiContent
import regex as re


async def DoubleCheckDB(page: Page, id_interno: str) -> None:

    item_list = [
        'Meu Desempenho',
        'Organize seus estudos com a Sofia',
        'Fale com o Tutor',
        'Desafio Colaborativo',
        'Unidade 1',
        'Unidade 2',
        'Unidade 3',
        'Unidade 4',
        'Workshop',
        'AV1',
        'Avaliações',
        'WebAula'
    ]
    _Item = [
        'Workshop',
        'AV1',
        'Avaliações',
        'WebAula'
    ]
    # todos que tem config clicar [ex: _Item]
    # Sofia link

    async def loopItemList(page: Page, id_interno, item_list):
        for item in item_list:
            if "Unidade" in item:
                id_DB = await getApiContent.API_Req_Content(page, id_interno, item)
                await page.goto(url=f"./ultra/courses/{id_interno}/outline")
                try:
                    await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
                    await page.get_by_text("Atividade de Autoaprendizagem").first.click()
                    await page.get_by_role("link", name="Configurações", exact=True).click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(3*1000)
                    await page.mouse.wheel(0, 1000)  # Rola 1000px para baixo
                    await page.wait_for_timeout(2*1000)
                    await page.mouse.wheel(0, 800)  # Rola 800px para baixo
                    await page.wait_for_timeout(2*1000)
                    await page.mouse.wheel(0, 350)  # Rola 350px para baixo
                    await page.wait_for_timeout(2*1000)
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(6*1000)
                    await page.get_by_role("button", name="Fechar").click()
                    await page.get_by_role("button", name="Fechar").click()
                except Exception as e:
                    print(f'Erro ao processar request {
                          item} in {id_interno}:', e)
            else:
                id_DB = await getApiContent.API_Req_Content(page, id_interno, item)
                await page.goto(url=f"./ultra/courses/{id_interno}/outline")
                await page.wait_for_load_state('load')
                await page.wait_for_timeout(5*1000)
                try:
                    if item in _Item:
                        # Rola 5000px para baixo
                        await page.mouse.wheel(0, 5000)
                        await page.wait_for_timeout(2*1000)
                    await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(5*1000)
                    await page.get_by_role("button", name="Fechar").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(5*1000)
                except Exception as e:
                    print(f'Erro ao processar request {
                          item} in {id_interno}:', e)

    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    await page.get_by_role("link", name="Boletim de notas").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_label("Configurações", exact=True).click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(4*1000)
    await page.mouse.wheel(0, 500)  # Rola 500px para baixo
    await page.wait_for_timeout(3*1000)
    await page.get_by_role("button", name="Fechar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(4*1000)
    await page.get_by_role("link", name="Grupos").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(4*1000)
    await page.get_by_role("link", name="Conteúdo da disciplina").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(4*1000)
    await loopItemList(page, id_interno, item_list)
    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    await page.get_by_role("link", name="Banco de questões Gerenciar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(6*1000)
    await page.get_by_role("button", name="Fechar").click()
    await page.get_by_role("link", name="Imagem do curso Editar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(6*1000)
    await page.get_by_role("button", name="Fechar").click()