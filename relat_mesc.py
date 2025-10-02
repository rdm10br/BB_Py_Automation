import json
import pandas as pd

# Carregar o arquivo JSON
with open(r"src\\Metodos\\Mescla\\__pycache__\\api_courses.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Lista para armazenar todos os resultados
all_results = []

# Iterar sobre todas as chaves do dicionário
for key, value in data.items():
    results = value.get("results", [])
    all_results.extend(results)

# Transformar em DataFrame
df = pd.DataFrame(all_results)

# import caas_jupyter_tools
# caas_jupyter_tools.display_dataframe_to_user("Tabela de Cursos", df)

# Filtrar apenas os itens que possuem o atributo 'hasChildren'
df_has_children = df[df["hasChildren"].notna()]

# Exportar os cursos com hasChildren para Excel
output_path = "cursos_com_hasChildren.xlsx"
df_has_children.to_excel(output_path, index=False)