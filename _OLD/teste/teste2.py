import asyncio
from playwright.async_api import async_playwright, Playwright

async def login_and_create_new_context(playwright: Playwright, email, password):
    # Cria um navegador e uma página para o contexto original
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    
    baseURL = 'https://practicetestautomation.com/practice-test-login/'

    # Navega para a página de login
    await page.goto(baseURL)

    # Preenche os campos de e-mail e senha
    await page.fill("#username", email)
    await page.fill("#password", password)

    # Clica no botão de login
    await page.click("#submit")

    # Espera até que a página esteja carregada
    await page.wait_for_load_state("networkidle")

    # Cria um novo contexto com as mesmas credenciais de login
    new_context = await browser.new_context(storage_state={"cookies": page.context.cookies(urls=baseURL)})

    # Retorna o novo contexto
    return new_context

async def main():
    async with async_playwright() as playwright:
        # Define as credenciais de login
        email = "student"
        password = "Password123"

        # Faz login e cria um novo contexto
        new_context = await login_and_create_new_context(playwright, email, password)

        # Cria uma nova página no novo contexto
        page = await new_context.new_page()
        
        # Navega para uma página protegida
        await page.goto("https://example.com/protected")

        # Verifica se o usuário está logado
        if "Logged In Successfully" in await page.text_content():
            print("Usuário logado com sucesso!")
        else:
            print("Erro ao logar o usuário.")

        # Fecha o contexto
        await new_context.close()

if __name__ == "__main__":
    asyncio.run(main())