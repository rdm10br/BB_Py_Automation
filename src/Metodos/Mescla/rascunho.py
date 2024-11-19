
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
