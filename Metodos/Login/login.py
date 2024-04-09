from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.Login import getCredentials
# from . import getCredentials

async def login(page: Page) -> None:        
        baseURL = "https://sereduc.blackboard.com/"
        ultraURL = f'{baseURL}ultra/course'
        
        
        if await page.locator('#agree_button').is_visible() :
                await page.get_by_role("button", name="OK").click()
        else :
                pass
        
        username, password = getCredentials.get_credentials()
                
        await page.get_by_label("Nome de usuário").fill(value=username)
        await page.get_by_label("Senha").fill(value=password)
        await page.locator('#entry-login').click()
        await page.goto(ultraURL)