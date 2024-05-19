import asyncio
from playwright.async_api import Page, expect

from Metodos import getPlanilha, getFromAPI
from Decorators.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:

    id_externo = getPlanilha.getCell(index=index)
    id_interno = await getFromAPI.API_Req(page=page, index=index)

    baseURL = 'https://sereduc.blackboard.com/'
    classURL = f'{baseURL}ultra/courses/'
    classUrlUltra = f'{classURL}{id_interno}/outline'

    # API to review general content config from the classroom
    APIContent = f'{baseURL}learn/api/public/v1/courses/{id_interno}/contents'

    # API to review general config from gradebook
    APIGradeCollum = f'{baseURL}learn/api/v1/courses/
    {id_interno}/gradebook/columns'
    
    # API to review general config form gradebook filtered to Activity by name
    APIGradeCollumActivity = f'{baseURL}learn/api/v1/courses/
    {id_interno}/gradebook/columns?Name=Atividade%20de%20Autoaprendizagem'
    
    
    # // visivel para o aluno
    # "visible": true,

    # // nota maxima no item
    # "possible": 10,

    # // quantidade de tentativas do item (0 = ilimitada)
    # "multipleAttempts": 0,

    # // visbilidade no boletim
    # "visibleInBook": false,
    
    itemSearch = ''
    # Needs exact name of the item to filter
    filteredRequest = f'''
    const data = JSON.parse(document.body.innerText).results
    const filteredResults = data.filter(item => item.name === {itemSearch})[0]
    console.log(filteredResults);'''
    
    print(id_externo)

    await page.goto(classUrlUltra)


async def main():
    await run()

asyncio.run(main())
