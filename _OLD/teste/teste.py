from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Realize ações antes do loop, se necessário
        initial_context = browser.new_context()
        initial_page = initial_context.new_page()
        initial_page.goto('https://example.com')
        # Realize outras ações necessárias

        old_context = initial_context

        for _ in range(5):  # Supondo que você queira criar e fechar 5 contextos
            # Realize ações no contexto antigo, se necessário

            # Crie um novo contexto
            new_context = browser.new_context()

            # Realize ações no novo contexto
            page = new_context.new_page()
            page.goto('https://example.com')

            # Feche o contexto antigo
            old_context.close()

            # Atualize a referência para o novo contexto
            old_context = new_context

        # No final, feche o último contexto
        old_context.close()

        # Feche o navegador
        browser.close()

if __name__ == "__main__":
    main()