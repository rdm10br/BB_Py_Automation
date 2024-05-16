import spacy
import spacy.training
from spacy.training.initialize import init_nlp
import getBQ
from spacy.matcher import Matcher

# nlp = init_nlp(config=r'Metodos\BQ\config.cfg')
nlp = spacy.load("pt_core_news_lg")

# pattern_questions = [{"TEXT": "Questão"}, {"IS_DIGIT": True}]
# pattern_choices = [{"TEXT": "a"}, {"IS_PUNCT": True}, {"IS_UPPER": True}]

pattern_statment = [{'LEMMA': 'Questão'},
           {'IS_DIGIT': True},
           {'OP': '+'},
           {'LEMMA': 'a', 'LENGTH': 1},
           {'IS_PUNCT': True, 'LEMMA': ')'},
           {'IS_UPPER': True}]

# Initialize the Matcher with the pattern
matcher = Matcher(nlp.vocab)
# matcher.add("Question_Pattern", [pattern_questions])
matcher.add("Question_Statment_Pattern", [pattern_statment])
# matcher.add("Choice_Pattern", [pattern_choices])

# text = getBQ.read_document(
#     r'C:\Users\rafad\Downloads\Questionário_Legislação e Rotina Trabalhista '\
#     'e Previdenciária _unidade 1_DIGITAL PAGES_ORIGINAL (revisado).docx')

text = '''Questão 1
Há uma comparação do Big Data com as soluções de BI (Business Intelligence)
, e podemos afirmar que existem semelhanças, mas é importante o entendimento do
que caracteriza e diferencia as soluções de Big Data de outras. Com relação à
caracterização das soluções de Big Data, assinale a alternativa correta:
a) A Veracidade caracteriza a fonte original dos dados e de como são armazenados
, aumentando a confiabilidade na solução.
b) O Valor está ligado à grande quantidade de dados processados nas soluções
 de Big Data.
c) A Variedade é a propriedade que dá agilidade para na análise de dados mesmo
com quantidades enormes de dados.
d) A Velocidade diz respeito aos diferentes tipos de dados que o Big Data pode
processar, indo de textos, áudios, vídeos até bancos de dados.
e) O Volume associa às soluções de Big Data aos processos de negócio,
que justificam os esforços de implantação.

Questão 2

Esta é outra questão com suas alternativas.
Há uma comparação do Big Data com as soluções de BI (Business Intelligence)
, e podemos afirmar que existem semelhanças, mas é importante o entendimento do
que caracteriza e diferencia as soluções de Big Data de outras. Com relação à
caracterização das soluções de Big Data, assinale a alternativa correta:

a) Alternativa A
b) Alternativa B
c) Alternativa C
d) Alternativa D
e) Alternativa E

Questão 3
Esse é um teste
Há uma comparação do Big Data com as soluções de BI (Business Intelligence)
, e podemos afirmar que existem semelhanças, mas é importante o entendimento do
que caracteriza e diferencia as soluções de Big Data de outras. Com relação à
caracterização das soluções de Big Data, assinale a alternativa correta:
a) Alternativa A2
b) Alternativa B2
c) Alternativa C2
d) Alternativa D2
e) Alternativa E2

Questão 4

Esse é um teste2
Há uma comparação do Big Data com as soluções de BI (Business Intelligence)
, e podemos afirmar que existem semelhanças, mas é importante o entendimento do
que caracteriza e diferencia as soluções de Big Data de outras. Com relação à
caracterização das soluções de Big Data, assinale a alternativa correta:
a) Alternativa A2
b) Alternativa B2
c) Alternativa C2
d) Alternativa D2
e) Alternativa E2'''

# Parse the text
doc = nlp(text)

# Find matches
matches = matcher(doc)

# Extract text between matches
for match_id, start, end in matches:
    # Get the text between start and end tokens
    captured_text = doc[start+2:end-3].text
    # captured_text = doc[start:end].text
    # captured_text = doc[start+1:end-1].root.pos_

    # Output the captured text
    print("Captured text:", captured_text)
print(len(matches))

# if matches:
#     match_id, start, end = matches[0]  # Get the first match
#     captured_text = doc[start+2:end-3].text
#     print("Captured text:", captured_text)

# question_matches = matcher(doc, as_spans=True)

# for question_match in question_matches:
#     question_start = question_match.start
#     question_end = question_match.end

#     # Find choice matches within the question's span
#     choice_matches = matcher(doc[question_start:question_end], as_spans=True)

#     # Print the question
#     print("Question:", doc[question_start:question_end].text)

#     # Print each choice
#     for choice_match in choice_matches:
#         choice_start = choice_match.start + question_start
#         choice_end = choice_match.end + question_start
#         print("Choice:", doc[choice_start:choice_end].text)
