import pandas as pd
import os, pyarrow, openpyxl

class getSpreadSheet():
    def __init__(self) -> None:
        super().__init__()
        # print(os.getcwd())

        # Acessando o arquivo
        self.arq_excel = os.path.join(os.getcwd(),r'Planilhas\SALAS.xlsx')

        # Lendo o arquivo
        self.col_id = "ID"
        self.col_status = 'STATUS'
        self.plan_1 = 'salas'
        self.col_status_plan1 = 'B'
        self.col_plan1_result = 'C'
        self.col_plan1_forum = 'D'
        self.col_plan1_desmp = 'E'
        self.col_plan1_sofia = 'F'
        self.col_plan1_fale = 'G'
        self.col_plan1_desafio = 'H'
        self.col_plan1_u1 = 'I'
        self.col_plan1_u2 = 'J'
        self.col_plan1_u3 = 'K'
        self.col_plan1_u4 = 'L'
        self.col_plan1_result = 'M'
        self.col_plan1_result = 'N'
        self.col_plan1_result = 'O'
        self.col_plan1_m4 = 'P'
        self.col_plan1_result = 'Q'
        self.col_plan1_result = 'R'
        self.col_plan1_result = 'S'
        self.col_plan1_v4 = 'T'
        self.col_plan1_result = 'U'
        self.col_plan1_result = 'V'
        self.col_plan1_result = 'W'
        self.col_plan1_b4 = 'X'
        self.col_plan1_result = 'Y'
        self.col_plan1_result = 'Z'
        self.col_plan1_result = 'AA'
        self.col_plan1_a4 = 'AB'
        self.col_plan1_result = 'AC'
        self.col_plan1_result = 'AD'
        self.col_plan1_aol4 = 'AE'
        self.col_plan1_aol4 = 'AF'
        self.col_plan1_avaliacao = 'AG'
        self.col_plan1_web = 'AH'
        self.col_plan1_solicite = 'AI'
        self.col_plan1_ser = 'AJ'
        self.df_map_plan1 = pd.read_excel(arq_excel, sheet_name=self.plan_1)
        self.total_lines = len(df_map)

        self.col_plan2_origin = "ID_ORIGIN"
        self.col_plan2_copy = 'ID_DESTINY'
        self.col_plan2_status = 'STATUS'
        self.col_status_plan2 = 'C'
        self.plan_2 = 'salaCopia'
        self.df_map_plan2 = pd.read_excel(arq_excel, sheet_name=self.plan_2)
        self.total_lines_plan2 = len(df_map_plan2)

        self.col_plan3_curso = "CURSO"
        self.col_plan3_GA = 'GRANDE ÁREA'
        self.plan_3 = 'atividades'
        self.df_map_plan3 = pd.read_excel(arq_excel, sheet_name=self.plan_3)
        self.total_lines_plan3 = len(df_map_plan3)

    def getCell(self, index: int, df_map, column: str):
        index -= 1
        try :
        # Verificando se o índice está dentro do intervalo válido
            if 0 <= index < total_lines:
                # Obtendo o valor da célula na linha e coluna especificadas
                cell_value = self.df_map.at[index, column]
                return str(cell_value)
            else:
                return total_lines
        except Exception as e:
                print("index does not exist")
    
    def writeOnExcel(self, index, return_status, _workbook, column_return):
        # Load an existing Excel workbook
        workbook = openpyxl.load_workbook(self.arq_excel)

        # Select the active sheet
        sheet = workbook[_workbook]

        # Write data to the Excel sheet
        sheet[f'{column_return}{index+1}'] = return_status

        # Save the changes to the existing file
        workbook.save(arq_excel)
    
    def getCell_id(self, index: int):
        return self.getCell(index, self.df_map_plan1, self.col_id)
                
    def getCell_status(self, index: int):
        return self.getCell(index, col_status)
                
    def getCell_plan2_status(self, index: int):
        return self.getCell(index, self.df_map_plan2, self.col_plan2_status)
                
    def getCell_copy_plan2(self, index: int):
        return self.getCell(index, self.df_map_plan2, self.col_plan2_status)
    
    def writeOnExcel_Plan2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_2, self.col_status_plan2)
        
    def writeOnExcel_Plan1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_status_plan1)
        
    def writeOnExcel_Plan1_Result(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_result)
        
    def writeOnExcel_Plan1_Forum(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_Desemp(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_SOFIA(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_FALE(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_DESAFIO(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_U1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_U2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_U3(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_U4(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_M1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)

    def writeOnExcel_Plan1_M2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_M3(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_M4(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_V1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_V2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_V3(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_V4(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_B1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_B2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)

    def writeOnExcel_Plan1_B3(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_B4(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_A1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_A2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_A3(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_A4(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_AOL1(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_AOL2(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_AOL3(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)

    def writeOnExcel_Plan1_AOL4(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)

    def writeOnExcel_Plan1_AVALICAO(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_WEB(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_SOLICITE(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
    def writeOnExcel_Plan1_SER(self, index, return_status):
        self.writeOnExcel(index, return_status, self.plan_1, self.col_plan1_forum)
        
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