import pandas as pd
import openpyxl
import pyarrow
from functools import lru_cache

# Acessando o arquivo
arq_excel = r'Planilhas\SALAS.xlsx'

col = "ID"
col_status = 'STATUS'
df_map = pd.read_excel(arq_excel, sheet_name='salas')
total_lines = len(df_map)

def getCell_status(index: int):
    index -= 1
    if 0 <= index < total_lines:
        cell_value = df_map.at[index, col_status]
        return str(cell_value)
    else:
        return str(cell_value)

@lru_cache
def main():
    for index in range(total_lines):
        index+=1
        cell_status_read = getCell_status(index=index)
        
        if cell_status_read == 'nan':
            print(index)
        else:
            print(f'index: {index} já preenchido')
        
if __name__ == '__main__':
    main()