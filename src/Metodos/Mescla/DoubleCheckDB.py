from playwright.async_api import Page, expect
from Metodos import getApiContent
import regex as re
import requests, json, os, asyncio
from dotenv import load_dotenv

# def load_cache() -> dict:
#     """Carrega o cache de cookies de um arquivo JSON."""
#     cache_file = r'src\Metodos\Login\__pycache__\login_cache.json'
#     if os.path.exists(cache_file):
#         with open(cache_file, 'r') as c:
#             return json.load(c)
#     return {}

# # Função para salvar o cache de cookies de volta para o arquivo JSON
# def save_cache(cache: dict) -> None:
#     """Salva o cache de cookies no arquivo JSON."""
#     cache_file = r'src\Metodos\Login\__pycache__\login_cache.json'
#     with open(cache_file, 'w') as c:
#         json.dump(cache, c, indent=4)

def folder(id_interno: str, item) -> bool:
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
    data = API(url)  # A API deve retornar os dados completos
    
    try:
        # Verifica se o item contém 'hasChildren' e se ele é True
        for i in data.get('results', []):
            if i.get('title') == item:  # Verifica o item específico
                if 'hasChildren' in i:  # Verifica se a chave 'hasChildren' existe
                    return i.get('hasChildren', False)  # Retorna o valor de 'hasChildren'
                else:
                    return False  # Se 'hasChildren' não existir, retorna False
        return False  # Se o item não for encontrado
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o item: {e}")
        return False
    
    # id_DB = await getApiContent.API_Req_Content(page, id_interno, item)
    
# def API_ID(id_interno: str, item):
#     url = f'/learn/api/public/v1/courses/{id_interno}/contents'
#     data = API(url)  # A API deve retornar os dados completos
   
#     try:
#         # Verifica se o item contém 'hasChildren' e se ele é True
#         for i in data.get('results', []):
#             if i.get('title') == item:  # Verifica o item específico
#                 if 'id' in i:  # Verifica se a chave 'hasChildren' existe
#                     return i.get('id', False)  # Retorna o valor de 'hasChildren'
#                 else:
#                     return False  # Se 'hasChildren' não existir, retorna False
#         return False  # Se o item não for encontrado
#     except Exception as e:
#         print(f"Ocorreu um erro ao verificar o item: {e}")
#         return False

def API_ID(id_interno: str, item):
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
    data = API(url)  # A API deve retornar os dados completos
    
    try:
        # Verifique se a resposta é uma lista ou um dicionário
        if isinstance(data, dict):  # Se for um dicionário, tente acessar 'results'
            items = data.get('results', [])
        elif isinstance(data, list):  # Se for uma lista, use diretamente
            items = data
            
        # Verifique se o item existe na lista de itens
        for i in items:
            if i.get('title') == item:  # Verifica se o item tem o título correspondente
                if 'id' in i:  # Verifica se existe a chave 'id'
                    return i.get('id', False)  # Retorna o id ou False
        return False  # Se o item não for encontrado ou o formato estiver errado
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o item: {e}")
        return False

def API(_url: str) -> list:
    try:
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        BASE_URL = os.getenv('BASE_URL')

        # Caminho do arquivo de cache dos dados da URL
        cache_file = r'src\Metodos\Mescla\__pycache__\api_cache.json'  # Cache específico para dados da URL
        
        cookie_file = r'src\Metodos\Login\__pycache__\login_cache.json'
        
        # Lê o arquivo de cache para obter os cookies
        with open(cookie_file, 'r') as c:
            cache_cookies = json.load(c)
        # Verifica se o arquivo de cache existe
        
        cookies = {cookie['name']: cookie['value'] for cookie in cache_cookies['cookies']}
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                cache = json.load(f)
        else:
            cache = {}

        # Verifica se a URL já está no cache
        if _url in cache:
            print(f"Cache encontrado para a URL: {_url}")
            return cache[_url]  # Retorna os dados armazenados para a URL

        # Se não houver cache, faz a requisição HTTP
        print(f"Fazendo requisição para a URL: {_url}")
        
        response = requests.get(
            url=f'{BASE_URL}{_url}',
            cookies=cookies
        )
        
        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()
        
        # Converte a resposta em JSON
        data = response.json()

        # Armazena o retorno da URL no cache
        cache[_url] = data
        
        # Salva o cache atualizado no arquivo de cache
        with open(cache_file, 'w', encoding='UTF-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)

        return data
    except Exception as e:
        # Aqui você pode logar o erro ou retorná-lo de alguma forma mais informativa
        print(f"Ocorreu um erro: {e}")
        return []  # Retorna uma lista vazia em caso de erro
    
    
def Item_list(id_interno: str):
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
    data = API(url)
    # Extrai o campo 'title' do JSON. Se não existir, retorna uma lista vazia
    item_list = [item.get('title', '') for item in data.get('results', [])]
    return item_list

# def API(url: str) -> list:
#     try:
#         # Carrega as variáveis de ambiente do arquivo .env
#         load_dotenv()
#         BASE_URL = os.getenv('BASE_URL')
        
#         # Caminho do arquivo de cache de cookies
#         cookie_file = r'src\Metodos\Login\__pycache__\login_cache.json'
        
#         # Lê o arquivo de cache para obter os cookies
#         with open(cookie_file, 'r') as c:
#             cache = json.load(c)
        
#         # Verifica se 'cookies' está presente e é uma lista
#         if not isinstance(cache, dict) or not isinstance(cache.get('cookies'), list):
#             raise ValueError(f"Erro: O arquivo de cache não contém a chave 'cookies' ou ela não é uma lista. Conteúdo do cache: {cache}")
        
#         # Converte a lista de cookies em um dicionário
#         cookies = {cookie['name']: cookie['value'] for cookie in cache['cookies']}
        
#         # Fazendo a requisição HTTP síncrona com requests
#         response = requests.get(
#             url=f'{BASE_URL}{url}',
#             cookies=cookies
#         )
        
#         # Verifica se a requisição foi bem-sucedida
#         response.raise_for_status()
        
#         # Converte a resposta em JSON
#         data = response.json()
        
#         # Extrai o campo 'title' do JSON. Se não existir, retorna uma lista vazia
#         item_list = [item.get('title', '') for item in data.get('results', [])]
#         # item_list = data.get('title', [])
        
#         return item_list

#     except Exception as e:
#         # Aqui você pode logar o erro ou retorná-lo de alguma forma mais informativa
#         print(f"Ocorreu um erro: {e}")
#         return []  # Retorna uma lista vazia em caso de erro

async def DoubleCheckDB(page: Page, id_interno: str) -> None:
    # Chama a função API de forma assíncrona usando asyncio.to_thread
    url = f'/learn/api/public/v1/courses/{id_interno}/contents'
   
    _item_list = await asyncio.to_thread(Item_list, id_interno)
    print(_item_list)
    
    item_list = _item_list  # Agora estamos usando o item_list retornado pela função API
    
    # try:
    #     isFolder = folder()
    #     ...
    # except:
    #     isFolder = False
    #     ...
        
    # hasChildren
    
    _ItemRolagem = [
        'Workshop',
        'AV1',
        'Avaliações',
        'WebAula'
    ]
    _ItemConfig = [  #todos que tem config clicar, menos fale com tutor
        'Desafio Colaborativo',
        'AV1'
    ]
    _ItemConfigFcT = [  #Fale com tutor config
        'Fale com o Tutor'
    ]
    
    # Sofia link
    
    async def loopItemList(page: Page, id_interno, item_list):
        for item in item_list:
            if "Unidade" in item:
                # id_DB = await getApiContent.API_Req_Content(page, id_interno, item)
                id_DB = API_ID(id_interno, item)
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
                    print(f'Erro ao processar request {item} in {id_interno}:', e)
            else:
                # id_DB = await getApiContent.API_Req_Content(page, id_interno, item)
                id_DB = API_ID(id_interno, item)
                await page.goto(url=f"./ultra/courses/{id_interno}/outline")
                await page.wait_for_load_state('load')
                await page.wait_for_timeout(5*1000)
                try:
                    if item in _ItemRolagem:
                        await page.mouse.wheel(0, 5000)  # Rola 5000px para baixo
                        await page.wait_for_timeout(2*1000)
                    await page.locator(f'//div[@data-content-id="{id_DB}"]').click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(3*1000)
                    if item in _ItemConfigFcT:
                        await page.get_by_label("Editar configurações do diário").click()
                        await page.wait_for_load_state('load')
                        await page.wait_for_timeout(2*1000)
                    if item in _ItemConfig:
                        await page.get_by_role("link", name="Configurações", exact=True).click()
                        await page.wait_for_load_state('load')
                        await page.wait_for_timeout(3*1000)
                    await page.get_by_role("button", name="Fechar").click()
                    await page.wait_for_load_state('load')
                    await page.wait_for_timeout(5*1000)
                except Exception as e:
                    print(f'Erro ao processar request {item} in {id_interno}:', e)
    
    await page.goto(url=f"./ultra/courses/{id_interno}/outline")
    await page.get_by_role("link", name="Boletim de notas").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.get_by_label("Configurações", exact=True).click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(2*1000)
    await page.mouse.wheel(0, 500)  # Rola 500px para baixo
    await page.wait_for_timeout(2*1000)
    await page.get_by_role("button", name="Fechar").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(3*1000)
    await page.get_by_role("link", name="Grupos").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(3*1000)
    await page.get_by_role("link", name="Conteúdo da disciplina").click()
    await page.wait_for_load_state('load')
    await page.wait_for_timeout(3*1000)
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