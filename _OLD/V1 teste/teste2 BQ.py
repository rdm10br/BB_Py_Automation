# [13:51] Matheus Felipe Rosa Ferreira
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd

import re
from docx import Document

# arq_excel = 'MAPEAMENTOS.xlsx'
# df_map = pd.read_excel(arq_excel, sheet_name='Plan1')

#python -m playwright codegen

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://sereduc.blackboard.com/")
#     page.get_by_role("button", name="OK").click()
#     page.get_by_text("Nome de usuário").click()
#     page.get_by_label("Nome de usuário").fill("matheus.rosa")
#     page.get_by_label("Senha").click()
#     page.get_by_label("Senha").fill("matheus013191095")
#     page.get_by_role("button", name="Fazer login").click()
    
# with sync_playwright () as playwright:
#     run(playwright)

regex_Enunciado = '(?ms)(?<=\\d[.]\\s).*(?=\\s[a][)]\\s|\\s[a][.]\\s)'
regex_Alternativa_A = '(?ms)(?<=[a][)]\\s|\\s[a][)]\\s|[a][.]\\s).*(?=[b][)]|\\s[b][)]|[b][.]\\s)'
regex_Alternativa_B = '(?ms)(?<=[b][)]\\s|\\s[b][)]\\s|[b][.]\\s).*(?=[c][)]|\\s[c][)]|[c][.]\\s)'
regex_Alternativa_C = '(?ms)(?<=[c][)]\\s|\\s[c][)]\\s|[c][.]\\s).*(?=[d][)]|\\s[d][)]|[d][.]\\s)'
regex_Alternativa_D = '(?ms)(?<=[d][)]\\s|\\s[d][)]\\s|[d][.]\\s).*(?=[e][)]|\\s[e][)]|[e][.]\\s)'
regex_Alternativa_E = '(?ms)(?<=[e][)]|[e][[)]\\s|\\s[e][)]\\s|\\s[e][)]\\s|\\s[e]\\.\\s|[e]\\.\\s).*(?=\\s\\d[.]|[.]\\s|\\z)'

teste = '''1.	É sabido que os termos ética e moral referem-se, de acordo com Chauí (2016, p. 321), ao “[...] conjunto de 
costumes de uma sociedade, considerados como valores e obrigações para seus membros”. Apesar de semelhantes, ambas as 
palavras precisam ser diferenciadas conceitualmente, pois apresentam uma relação complementar entre elas. Dito isso, 
os termos ética e moral dizem respeito, respectivamente, a:

a)	Comportamento coletivo adotado a partir de uma reflexão individual sobre um conjunto de normas sociais; costume 
de um povo em um período determinado.
b)	Comportamento individual adotado a partir de uma reflexão desse indivíduo sobre um conjunto de normas pré-
determinadas pela sociedade; costume de um povo em um período determinado.
c)	Conjunto de regras impostas pela sociedade; conjunto de regras definido pelo próprio indivíduo inserido em uma
população.
d)	Regras de conduta adotadas pelo indivíduo frente às exigências sociais; regras de conduta pré-estabelecidas 
socialmente.
e)	Costume de uma sociedade em tempos específicos; comportamento               individual adotado a partir de uma 
reflexão sobre as normas sociais.'''

enunciado = re.search(regex_Enunciado,teste)
alternativa_a = re.findall(regex_Alternativa_A,teste,re.MULTILINE)
print(enunciado.group())
print(alternativa_a)

# txt = "The rain in Spain"
# regex1 = "^The.*Spain$"
# x = re.search(regex1, txt)
# print(x.string)