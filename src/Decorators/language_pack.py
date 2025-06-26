import os, polib, gettext, requests, asyncio, sys, builtins
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv()
lang = os.getenv('LANGUAGE')
# Definir idioma (pode ser dinâmico)
idioma = lang or 'pt_BR'  # ou 'en_US'
translator = Translator()

# Caminho base das traduções
localedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'locale'))

IDIOMAS = ['es_ES', 'fr_FR', 'ru_RU', 'pt_BR']  # idiomas de destino
BASE_IDIOMA = 'en_US'
ARQUIVO_PO = 'messages.po'


def gerar_po_para_idiomas(base_dir='locale'):
    base_path = os.path.join(base_dir, BASE_IDIOMA, 'LC_MESSAGES', ARQUIVO_PO)
    base_po = polib.pofile(base_path)

    for idioma in IDIOMAS:
        _idioma = idioma.split('_')[0]
        destino_dir = os.path.join(base_dir, idioma, 'LC_MESSAGES')
        destino_po = os.path.join(destino_dir, ARQUIVO_PO)

        os.makedirs(destino_dir, exist_ok=True)

        if not os.path.exists(destino_po):
            # print(f"Criando arquivo de tradução: {destino_po}")
            novo_po = polib.POFile()
            novo_po.metadata = {
                'Project-Id-Version': '1.0',
                'Language': idioma,
                'Content-Type': 'text/plain; charset=UTF-8',
                'Content-Transfer-Encoding': '8bit',
            }

            for entrada in base_po:
                msgid = entrada.msgid.strip()
                if not msgid:
                    continue
                try:
                    novo_po.append(
                        polib.POEntry(
                            msgid=entrada.msgid,
                            msgstr=translator.translate(text=entrada.msgid, dest=_idioma).text
                        )
                    )
                except Exception as e:
                    print(f"[{idioma}] Erro ao traduzir '{entrada.msgid}': {e}")
                    novo_po.append(
                        polib.POEntry(
                            msgid=entrada.msgid,
                            msgstr=""  # ou msgid como fallback
                        )
                    )
                    ...

            novo_po.save(destino_po)
        else:
            # print(f"Arquivo já existe: {destino_po}")
            ...


def compilar_po_para_mo(base_locale='locale'):
    for idioma in os.listdir(base_locale):
        po_file = os.path.join(base_locale, idioma, 'LC_MESSAGES', 'messages.po')
        mo_file = os.path.join(base_locale, idioma, 'LC_MESSAGES', 'messages.mo')
        if os.path.isfile(po_file):
            # print(f"Compilando {po_file} → {mo_file}")
            polib.pofile(po_file, encoding='utf-8').save_as_mofile(mo_file)


# def lang_pack(func):
#     def wrapper (*args, **kwargs):
#         gerar_po_para_idiomas(localedir)
#         compilar_po_para_mo(localedir)
#         lang = gettext.translation('messages', localedir=localedir, languages=[idioma], fallback=True)
#         lang.install()
#         return func(*args, **kwargs)
#     return wrapper
def lang_pack(func):
    def wrapper(*args, **kwargs):
        gerar_po_para_idiomas(localedir)
        compilar_po_para_mo(localedir)
        lang = gettext.translation('messages', localedir=localedir, languages=[idioma], fallback=True)
        lang.install()

        # Monkey-patch built-in print
        original_print = builtins.print

        def translated_print(*args, **kwargs):
            translated_args = []
            for arg in args:
                if isinstance(arg, str):
                    translated_args.append(_(arg)) # type: ignore
                else:
                    translated_args.append(arg)
            original_print(*translated_args, **kwargs)

        builtins.print = translated_print

        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print  # Restore original print after execution

    return wrapper

# def lang_pack_async(func):
#     async def wrapper(*args, **kwargs):
#         gerar_po_para_idiomas(localedir)
#         compilar_po_para_mo(localedir)
#         lang = gettext.translation('messages', localedir=localedir, languages=[idioma], fallback=True)
#         lang.install()
#         return await func(*args, **kwargs)
#     return wrapper
def lang_pack_async(func):
    async def wrapper(*args, **kwargs):
        gerar_po_para_idiomas(localedir)
        compilar_po_para_mo(localedir)
        lang = gettext.translation('messages', localedir=localedir, languages=[idioma], fallback=True)
        lang.install()

        original_print = builtins.print

        def translated_print(*args, **kwargs):
            translated_args = []
            for arg in args:
                if isinstance(arg, str):
                    translated_args.append(_(arg)) # type: ignore
                else:
                    translated_args.append(arg)
            original_print(*translated_args, **kwargs)

        builtins.print = translated_print

        try:
            return await func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper