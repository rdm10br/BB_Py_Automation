import requests, json, os
from dotenv import load_dotenv


def API(_url: str) -> list:
    try:
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        BASE_URL = os.getenv('BASE_URL')

        # Caminho do arquivo de cache dos dados da URL
        cache_file = r'src\Metodos\Mescla\__pycache__\api_courses.json'  # Cache específico para dados da URL
        
        cookie_file = r'src\Metodos\Login\__pycache__\login_cache.json'
        
        # Lê o arquivo de cache para obter os cookies
        with open(cookie_file, 'r') as c:
            cache_cookies = json.load(c)
        # Verifica se o arquivo de cache existe
        
        cookies = {cookie['name']: cookie['value'] for cookie in cache_cookies['cookies']}
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='UTF-8') as f:
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


def loop(termo: str):
    paging: bool = True
    offset: int = 0
    limit = 100
    cache_file = r'src\Metodos\Mescla\__pycache__\api_courses.json'
    
    while paging:
        url = f'/learn/api/public/v3/courses?limit={limit}&offset={offset}&sort=name(asce)&termId=externalId:{termo}'
        API(url)
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='UTF-8') as f:
                cache = json.load(f)
        try:
            cache[url]['paging']
            offset += limit
        except KeyError:
            paging = False
    filtro()


def filtro():
    cache_file = r'src\Metodos\Mescla\__pycache__\api_courses.json'
    
    if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='UTF-8') as f:
                data = json.load(f)

   # Dictionary for filtered results and a list for orphaned entries
    filtered_data = {}
    orphan_entries = []
    
    print(data)
    # Loop through each URL key in the JSON
    for url_key, content in data.items():
        results = content.get("results", [])
        for entry in results:
            key = entry.get("name") or entry.get("externalId")  # Use name, fallback to externalId
            if key:
                # Build the filtered dictionary dynamically, only including existing fields
                filtered_entry = {"url": url_key}  # Always include API URL
            
                # Check and add only if the field exists in the entry
                if "availability" in entry:
                    filtered_entry["availability"] = entry["availability"]
                if "courseId" in entry:
                    filtered_entry["courseId"] = entry["courseId"]
                if "name" in entry:
                    filtered_entry["name"] = entry["name"]
                if "parentId" in entry:
                    filtered_entry["parentId"] = entry["parentId"]
                if "hasChildren" in entry:
                    filtered_entry["hasChildren"] = entry["hasChildren"]
                
                # availability.available
                # availability.duration.type
                
                # Check if entry has neither parentId nor hasChildren
                if "parentId" not in entry and "hasChildren" not in entry:
                    orphan_entries.append(filtered_entry)
                elif "hasChildren" in entry:
                    print(f'{entry['courseId']}    {entry['name']}')
                else:
                    filtered_data[key] = filtered_entry
    print(orphan_entries)