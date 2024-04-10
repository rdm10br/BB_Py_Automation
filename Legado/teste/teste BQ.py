from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd
import regex as re
from docx import Document

# import sys

# sys.path.append(r'C:\Users\rafad\Documents\VS_proj\BB_Py_Automation')

# from Metodos.API import getPlanilha


# cell = getPlanilha.getCell(index=1)

#python -m playwright codegen

# regex_Enunciado = r'(?ms)(?<=\d[.]\s).*(?=^\s[a][)]\s|^\s[a][.]\s)'
regex_Enunciado = r'(?<=\d[.]\s).*(?=\s+[a][)])'

regex_Alternativa_A = r'(?<=[a][)]\s|\s[a][)]\s|[a][.]\s).*(?=[b][)]|\s+[b][)]|[b][.]\s+|\s+[b][.]\s+)'
regex_Alternativa_B = r'(?<=[b][)]\s|\s[b][)]\s|[b][.]\s).*(?=[c][)]|\s+[c][)]|[c][.]\s+|\s+[c][.]\s+)'
regex_Alternativa_C = r'(?<=[c][)]\s|\s[c][)]\s|[c][.]\s).*(?=[d][)]|\s+[d][)]|[d][.]\s+|\s+[d][.]\s+)'
regex_Alternativa_D = r'(?<=[d][)]\s|\s[d][)]\s|[d][.]\s).*(?=[e][)]|\s+[e][)]|[e][.]\s+|\s+[e][.]\s+)'
regex_Alternativa_E = r'(?<=[e][)]\s|[e][.]\s|[e][.]).*(?=\s+\d[.]|[.]|\z)'

regex_alternativas = r"(?ms)(?<=[[][']).*(?=['][]])"

teste = '''1.	É sabido que os termos ética e moral referem-se, de acordo com Chauí (2016, p. 321), ao “[...] conjunto de costumes de uma sociedade, considerados como valores e obrigações para seus membros”. Apesar de semelhantes, ambas as palavras precisam ser diferenciadas conceitualmente, pois apresentam uma relação complementar entre elas. Dito isso, os termos ética e moral dizem respeito, respectivamente, a:
a)	Comportamento coletivo adotado a partir de uma reflexão individual sobre um conjunto de normas sociais; costume 
de um povo em um período determinado.
b)	Comportamento individual adotado a partir de uma reflexão desse indivíduo sobre um conjunto de normas pré-
determinadas pela sociedade; costume de um povo em um período determinado.
c)	Conjunto de regras impostas pela sociedade; conjunto de regras definido pelo próprio indivíduo inserido em uma
população.
d)	Regras de conduta adotadas pelo indivíduo frente às exigências sociais; regras de conduta pré-estabelecidas 
socialmente.
e)	Costume de uma sociedade em tempos específicos; comportamento               individual adotado a partir de uma 
reflexão sobre as normas sociais.

2. Qual é a capital do Brasil?
a) Rio de Janeiro
b) São Paulo
c) Brasília
d) Salvador
e) Belo Horizonte

3. Em que ano foi fundada a Microsoft?
a) 1975
b) 1985
c) 1995
d) 2005
e) 2015

4. Quem é o autor de "Dom Quixote"?
a) Miguel de Cervantes
b) William Shakespeare
c) Charles Dickens
d) Fyodor Dostoevsky
e) Jane Austen'''

def main() -> None:
    
    index = 0
    
    enunciado = re.search(pattern = regex_Enunciado , string = teste)
    print(f'\n{enunciado.captures()[index]}')
    
    alternativa_a = re.findall(pattern = regex_Alternativa_A , string = teste)
    print(f'\n{alternativa_a.copy()[index]}')
    
    # teste de remoção de carcteres especiais alternativas
    # alternativas = re.search(pattern = regex_alternativas , string = str(alternativa_a))
    # print(f'\n{alternativas.group()}')
    
    # teste de importação e novo metodo de path planilha
    # print(f'\n{cell}')

if __name__ == '__main__':
    main()