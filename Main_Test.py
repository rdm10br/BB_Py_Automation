import asyncio, gc, pytest, os, sys, time
from playwright.async_api import Playwright, async_playwright, Page

from Metodos import (getPlanilha, getFromAPI)
from Test.Main_StartUp import playwright_StartUp


@playwright_StartUp
async def run(page: Page, index) -> None:
    
        id_externo = getPlanilha.getCell(index=index)
        id_interno = await getFromAPI.API_Req(page=page, index=index)
        
        classUrlUltra = f'https://sereduc.blackboard.com/ultra/courses/{id_interno}/outline'
        
        print(id_externo)
        
        await page.goto(classUrlUltra)

async def main():
    await run()

asyncio.run(main())