from pyflowchart import Flowchart
# with open('src\Main_ATividades_Praticas.py') as f:
# 	code = f.read()
with open(r'C:\Users\013190873\Downloads\Pessoal\VS\BB_Py_Automation\src\Main_ATividades_Praticas.py') as f:
    code = f.read()
fc = Flowchart.from_code(code, field='Bar.buzz.g', inner=False)
print(fc.flowchart())



# flowchart = Flowchart.from_code(code)
# print(flowchart.flowchart())
