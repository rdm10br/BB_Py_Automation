# from playwright.sync_api import Playwright, sync_playwright, expect
# import time
# import pandas as pd
import regex as re
# from docx import Document

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

# teste = '''1.	É sabido que os termos ética e moral referem-se, de acordo com Chauí (2016, p. 321), ao “[...] conjunto de costumes de uma sociedade, considerados como valores e obrigações para seus membros”. Apesar de semelhantes, ambas as palavras precisam ser diferenciadas conceitualmente, pois apresentam uma relação complementar entre elas. Dito isso, os termos ética e moral dizem respeito, respectivamente, a:
# a)	Comportamento coletivo adotado a partir de uma reflexão individual sobre um conjunto de normas sociais; costume 
# de um povo em um período determinado.
# b)	Comportamento individual adotado a partir de uma reflexão desse indivíduo sobre um conjunto de normas pré-
# determinadas pela sociedade; costume de um povo em um período determinado.
# c)	Conjunto de regras impostas pela sociedade; conjunto de regras definido pelo próprio indivíduo inserido em uma
# população.
# d)	Regras de conduta adotadas pelo indivíduo frente às exigências sociais; regras de conduta pré-estabelecidas 
# socialmente.
# e)	Costume de uma sociedade em tempos específicos; comportamento               individual adotado a partir de uma 
# reflexão sobre as normas sociais.

# 2. Qual é a capital do Brasil?
# a) Rio de Janeiro
# b) São Paulo
# c) Brasília
# d) Salvador
# e) Belo Horizonte

# 3. Em que ano foi fundada a Microsoft?
# a) 1975
# b) 1985
# c) 1995
# d) 2005
# e) 2015

# 4. Quem é o autor de "Dom Quixote"?
# a) Miguel de Cervantes
# b) William Shakespeare
# c) Charles Dickens
# d) Fyodor Dostoevsky
# e) Jane Austen'''

teste = '''Questão 1. Há uma comparação do Big Data com as soluções de BI (Business Intelligence), e podemos afirmar que existem semelhanças, mas é importante o entendimento do que caracteriza e diferencia as soluções de Big Data de outras. Com relação à caracterização das soluções de Big Data, assinale a alternativa correta:
a) A Veracidade caracteriza a fonte original dos dados e de como são armazenados, aumentando a confiabilidade na solução.

b) O Valor está ligado à grande quantidade de dados processados nas soluções de Big Data.
c) A Variedade é a propriedade que dá agilidade para na análise de dados mesmo com quantidades enormes de dados.

d) A Velocidade diz respeito aos diferentes tipos de dados que o Big Data pode processar, indo de textos, áudios, vídeos até bancos de dados.

e) O Volume associa às soluções de Big Data aos processos de negócio, que justificam os esforços de implantação.

Questão 2. A utilização de Big Data cresceu nos últimos anos com base no aumento da utilização comercial da Internet e a democratização do seu uso pelo mundo todo. A sociedade tem se tornado cada vez mais conectada. Com base no contexto exposto acima e no conteúdo estudado, assinale a alternativa correta.

a) A complexidade dos dados em formatos não estruturados fez com que as soluções buscassem alternativas ao modelo tradicional de processamento de dados. Os volumes saíram de Terabytes para Petabytes e Exabytes.

b) Os buscadores na web foram os primeiros a necessitar de grandes armazenamentos de dados para guardar de forma estruturada os dados da Internet e utilizaram os padrões existentes para processar seus dados.

c) As páginas em HTML possuem uma estrutura interna avançada e muito mais fácil de ser armazenada em bases de dados relacionais, e a forma padronizada dos websites permitiram que buscadores como Google e Yahoo catalogassem o conteúdo web.

d) Apesar das soluções de Big Data serem desenvolvidas para obter velocidade processando grandes volumes de dados, elas são ideais para outras formas de utilização com baixo volume de dados, obtendo excelente desempenho.

e) As soluções de Big Data são muito utilizadas por buscadores Web, deixando a desejar no que diz respeito à sua utilização para armazenamento de informações de redes sociais.

Questão 3. O ciclo de processo de soluções de Data Science e Big Data são: Fontes de Dados, Aquisição, Armazenamento & Transformação, Análise & Modelagem, Visualização & Compartilhamento. Para cada fase, há soluções diferentes para cada tipo de necessidade, flexibilizando, mas também tornando as integrações mais complexas. Com base nessas informações e no conteúdo estudado, assinale a alternativa correta.

a) Os algoritmos de Machine Learning são usados na fase de Análise & Modelagem. 

b) É na fase de compartilhamento e visualização dos dados que existe a integração dos dados externos necessários ao modelo.

c) Os dados devem ser tratados para armazenamento na fase de análise e modelagem dos dados.

d) O enriquecimento dos dados acontece na fase de visualização dos dados.

e) A fase de análise & modelagem é a responsável pela carga de dados das fontes externas.
'''

def main() -> None:
    
    index = 2
    
    enunciado = re.findall(pattern = regex_Enunciado , string = teste)
    print(f'\nEnunciado:\n\n{enunciado.copy()[index]}')
    
    alternativa_A = re.findall(pattern = regex_Alternativa_A , string = teste)
    print(f'\nAlternativa:\n\n{alternativa_A.copy()[index]}\n')
    
    # teste de remoção de carcteres especiais alternativas
    # alternativas = re.search(pattern = regex_alternativas , string = str(alternativa_a))
    # print(f'\n{alternativas.group()}')
    
    # teste de importação e novo metodo de path planilha
    # print(f'\n{cell}')

if __name__ == '__main__':
    main()