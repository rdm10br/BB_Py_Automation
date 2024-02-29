import pandas as pd

# Dados fornecidos
arq_excel = 'BB_Py_Automation\\Planilhas\\SALAS.xlsx'

# Criar DataFrame
df = pd.read_excel(arq_excel, sheet_name='atividades')

# Solicitar ao usuário para inserir o índice da grande área
indice_grande_area = input("Insira o índice da grande área: ")

# Filtrar os cursos correspondentes ao índice inserido pelo usuário
cursos_filtrados = df.loc[df['GRANDE ÁREA'] == indice_grande_area, 'CURSO']

print("Cursos na grande área '{}':".format(indice_grande_area))
print(cursos_filtrados)