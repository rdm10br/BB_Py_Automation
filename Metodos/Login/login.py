from playwright.async_api import Playwright, async_playwright, expect, Page

from Metodos.Login import getCredentials
# from . import getCredentials

async def login(page: Page) -> None:
        """
        Function that attempts to login;
        This function ask for your credentials and tries to login with it

        Args:
            page (Page): Page constructor form Playwright that
        you want this Function to run
        """
        baseURL = "https://sereduc.blackboard.com/"
        ultraURL = f'{baseURL}ultra/course'
        
        
        if await page.locator('#agree_button').is_visible() :
                await page.get_by_role("button", name="OK").click()
        else :
                pass
        print('Getting credentials to log in.')
        username, password = getCredentials.get_credentials()

        print('Caught credentials!')
        await page.get_by_label("Nome de usuário").fill(value=username)
        await page.get_by_label("Senha").fill(value=password)
        await page.locator('#entry-login').click()
        await page.goto(ultraURL)