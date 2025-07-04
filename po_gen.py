import ast, os
from datetime import datetime

def gen_po():
    SRC_DIR = "src"
    PO_FILE = "messages.po"

    found_msgs = set()

    def extract_print_strings_from_file(filepath):
        with open(filepath, encoding="utf-8") as f:
            source = f.read()

        try:
            tree = ast.parse(source, filename=filepath)
        except SyntaxError:
            return []

        msgs = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'print':
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        msgs.append(arg.value)
                    elif isinstance(arg, ast.JoinedStr):  # f-strings
                        # Reconstroi f-string como template com {campo}
                        parts = []
                        for value in arg.values:
                            if isinstance(value, ast.FormattedValue):
                                parts.append("{" + ast.unparse(value.value) + "}")
                            elif isinstance(value, ast.Constant):
                                parts.append(value.value)
                        msgs.append("".join(parts))
        return msgs

    # Percorre recursivamente o diretório src/
    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                found_msgs.update(extract_print_strings_from_file(full_path))

    # Cria arquivo .po com mensagens únicas
    with open(PO_FILE, "w", encoding="utf-8") as po:
        po.write(
    f'''msgid ""
    msgstr ""
    "Project-Id-Version: BB_Py_Automation 1.0\\n"
    "POT-Creation-Date: {datetime.utcnow().strftime("%Y-%m-%d %H:%M+0000")}\\n"
    "Language: pt_BR\\n"
    "Content-Type: text/plain; charset=UTF-8\\n"
    "Content-Transfer-Encoding: 8bit\\n"

    ''')

        for msg in sorted(found_msgs):
            # Escapa aspas internas
            msg = msg.replace('"', '\\"')
            po.write(f'msgid "{msg}"\nmsgstr ""\n\n')

    print(f"✅ Arquivo {PO_FILE} gerado com {len(found_msgs)} mensagens únicas.")
    
if __name__ == "__main__":
    gen_po()
    ...