import asyncio, os
from playwright.async_api import Page

from Metodos import getPlanilha, MesclaOrfãoCA
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index) -> None:
    
        # if os.path.exists(r'src\Metodos\Mescla\__pycache__\api_courses.json'):
        #     os.remove(r'src\Metodos\Mescla\__pycache__\api_courses.json')
            
        termo = getPlanilha.getCell(index=index)
        
        MesclaOrfãoCA.loop(termo=termo)

async def main():
    await run()

asyncio.run(main())