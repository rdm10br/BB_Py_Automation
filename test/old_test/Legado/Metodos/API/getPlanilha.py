import pandas as pd
import openpyxl
import pyarrow

# Acessando o arquivo
arq_excel = r'BB_Py_Automation\Planilhas\SALAS.xlsx'

# Lendo o arquivo
col = "ID"
col_status = 'STATUS'
df_map = pd.read_excel(arq_excel, sheet_name='salas')
total_lines = len(df_map)

col_plan2 = "ID_ORIGIN"
col_plan2_copy = 'ID_DESTINY'
col_plan2_status = 'STATUS'
df_map_plan2 = pd.read_excel(arq_excel, sheet_name='salaCopia')
total_lines_plan2 = len(df_map_plan2)

col_plan3_curso = "CURSO"
col_plan3_GA = 'GRANDE ÁREA'
df_map_plan3 = pd.read_excel(arq_excel, sheet_name='atividades')
total_lines_plan3 = len(df_map_plan3)

def getCell(index):
    # Ajustando o índice para começar do zero
    index -= 1
    try :
    # Verificando se o índice está dentro do intervalo válido
        if 0 <= index < total_lines:
            # Obtendo o valor da célula na linha e coluna especificadas
            cell_value = df_map.at[index, col]
            return str(cell_value)
        else:
            return total_lines
    except Exception as e:
            print("index does not exist")
            
def getCell_status(index):
    # Ajustando o índice para começar do zero
    index -= 1
    # Verificando se o índice está dentro do intervalo válido
    if 0 <= index < total_lines:
        # Obtendo o valor da célula na linha e coluna especificadas
        cell_value = df_map.at[index, col_status]
        return str(cell_value)
    else:
        return str(cell_value)

def getCell_plan2(index):
    # Ajustando o índice para começar do zero
    index -= 1
    try :
    # Verificando se o índice está dentro do intervalo válido
        if 0 <= index < total_lines_plan2:
            # Obtendo o valor da célula na linha e coluna especificadas
            cell_value2 = df_map_plan2.at[index, col_plan2]
            return str(cell_value2)
        else:
            return total_lines_plan2
    except Exception as e:
            print("index does not exist")
            
def getCell_plan2_status(index):
    # Ajustando o índice para começar do zero
    index -= 1
    # Verificando se o índice está dentro do intervalo válido
    if 0 <= index < total_lines_plan2:
        # Obtendo o valor da célula na linha e coluna especificadas
        cell_value2 = df_map_plan2.at[index, col_plan2_status]
        return str(cell_value2)
    else:
        return str(cell_value2)
            
def getCell_copy_plan2(index):
    # Ajustando o índice para começar do zero
    index -= 1
    try :
    # Verificando se o índice está dentro do intervalo válido
        if 0 <= index < total_lines_plan2:
            # Obtendo o valor da célula na linha e coluna especificadas
            cell_value2 = df_map_plan2.at[index, col_plan2_copy]
            return str(cell_value2)
        else:
            return total_lines_plan2
    except Exception as e:
            print("index does not exist")
            
# def getCell_curso(index):
#     # Ajustando o índice para começar do zero
#     index -= 1
#     try :
#     # Verificando se o índice está dentro do intervalo válido
#         if 0 <= index < total_lines_plan3:
#             # Obtendo o valor da célula na linha e coluna especificadas
#             cell_value = df_map_plan3.at[index, col_plan3_curso]
#             return str(cell_value)
#         else:
#             return total_lines
#     except Exception as e:
#             print("index does not exist")
            
# def filter_GA(GA):
    
#     cursos_filtrados = df_map_plan3.loc[df_map_plan3[col_plan3_GA] == GA, 'CURSO']
    
#     return str(cursos_filtrados)
    
    
            
def writeOnExcel_Plan2(index, return_status):
    # Load an existing Excel workbook
    workbook = openpyxl.load_workbook(arq_excel)

    # Select the active sheet
    sheet = workbook['salaCopia']
    
    col_status_plan2 = 'C' #COLUNA DE STATUS deve ser atribuida pela letra da coluna

    # Write data to the Excel sheet
    sheet[f'{col_status_plan2}{index+1}'] = return_status

    # Save the changes to the existing file
    workbook.save(arq_excel)
    
def writeOnExcel_Plan1(index, return_status):
    # Load an existing Excel workbook
    workbook = openpyxl.load_workbook(arq_excel)

    # Select the active sheet
    sheet = workbook['salas']
    
    col_status_plan1 = 'B' #COLUNA DE STATUS deve ser atribuida pela letra da coluna

    # Write data to the Excel sheet
    sheet[f'{col_status_plan1}{index+1}'] = return_status

    # Save the changes to the existing file
    workbook.save(arq_excel)
            
# index = 1
# for index in range(total_lines_plan2) :
#     index +=1
#     cell = getCell_plan2(index)
#     cell_copy = getCell_copy_plan2(index)
#     print(f'o número presente na celula é :{cell} na linha: {index+1} da cóluna : {col_plan2} e na coluna : {col_plan2_copy} está o ID de copia {cell_copy}')

# print(filter_GA(GA='COMUNICAÇÃO'))