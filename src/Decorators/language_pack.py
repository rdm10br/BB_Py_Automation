import os, polib, gettext, requests, asyncio, sys, builtins, inspect, ast
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv('user_pref.env')
lang = os.getenv('LANGUAGE')
# Definir idioma (pode ser dinâmico)
idioma = lang or 'pt_BR'  # ou 'en_US'
translator = Translator()

# Caminho base das traduções
localedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'locale'))

# IDIOMAS = ['es_ES', 'fr_FR', 'ru_RU', 'pt_BR']  # idiomas de destino
IDIOMAS = ['pt_BR', 'es_ES']
if idioma not in IDIOMAS:
    IDIOMAS.append(idioma)
BASE_IDIOMA = 'en_US'
ARQUIVO_PO = 'messages.po'

def extract_raw_fstring():
    try:
        # Pega o frame de onde print foi chamado
        frame = inspect.stack()[2]
        code_context = frame.code_context
        if not code_context:
            return None

        line = ''.join(code_context).strip()

        # Faz parse da linha usando AST
        tree = ast.parse(line)

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'print':
                for arg in node.args:
                    if isinstance(arg, ast.JoinedStr):
                        raw = ast.get_source_segment(line, arg)
                        if raw:
                            # print(raw.lstrip('fF')[1:-1])
                            return raw.lstrip('fF')[1:-1]  # remove f" e "

    except Exception as e:
        print(f"[extract_raw_fstring ERROR]: {e}")
        return None

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
                    translation = translator.translate(text=entrada.msgid, dest=_idioma)
                    novo_po.append(
                        polib.POEntry(
                            msgid=entrada.msgid,
                            msgstr=translation.text
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

async def gerar_po_para_idiomas_async(base_dir='locale'):
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
                    translation = await translator.translate(text=entrada.msgid, dest=_idioma)
                    novo_po.append(
                        polib.POEntry(
                            msgid=entrada.msgid,
                            msgstr=translation.text
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
                    translated = _(arg) # type: ignore
                    raw = extract_raw_fstring()

                    if raw and translated == arg:
                        translated_template = _(raw) # type: ignore
                        try:
                            frame = inspect.currentframe().f_back
                            local_vars = frame.f_locals.copy()
                            translated = translated_template.format(**local_vars)
                        except Exception as e:
                            translated = translated_template  # Se falhar, usa não interpolada
                    translated_args.append(translated)
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
        await gerar_po_para_idiomas_async(localedir)
        compilar_po_para_mo(localedir)
        lang = gettext.translation('messages', localedir=localedir, languages=[idioma], fallback=True)
        lang.install()

        original_print = builtins.print

        def translated_print(*args, **kwargs):
            translated_args = []
            for arg in args:
                if isinstance(arg, str):
                    translated = _(arg) # type: ignore
                    raw = extract_raw_fstring()

                    if raw and translated == arg:
                        translated_template = _(raw) # type: ignore
                        try:
                            frame = inspect.currentframe().f_back
                            local_vars = frame.f_locals.copy()
                            translated = translated_template.format(**local_vars)
                        except Exception as e:
                            translated = translated_template  # Se falhar, usa não interpolada
                    translated_args.append(translated)
                else:
                    translated_args.append(arg)
            original_print(*translated_args, **kwargs)

        builtins.print = translated_print

        try:
            return await func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper