import os, json, asyncio

from Metodos import getCredentials


async def run() -> None:
    
    print('asking for credentials...')
    username, password = getCredentials.get_credentials()
    print('credentials caugth...')
    cache_file = os.path.join(os.path.curdir, r'src\Metodos\Login\__pycache__\login.json')
    cache_info = {
        "username": username,
        "password": password
    }

    print('dumping in the json...')
    with open(cache_file, 'w', encoding='UTF-8') as file:
        json.dump(cache_info, file, ensure_ascii=False, indent=4)
    print(f'login credentials cached at:\n{cache_file}')

async def main():
    await run()

asyncio.run(main())