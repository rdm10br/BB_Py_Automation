import asyncio
from playwright.async_api import Page

from Metodos import getPlanilha, MesclaOrfãoCA
from Decorators import playwright_StartUp


@playwright_StartUp()
async def run(page: Page, index) -> None:
    
        termo = getPlanilha.getCell(index=index)
        
        MesclaOrfãoCA.loop(termo=termo)

async def main():
    await run()

asyncio.run(main())