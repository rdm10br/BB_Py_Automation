import spacy
from spacy.matcher import Matcher

# Load the English model
# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("pt_core_news_sm")

# Define your pattern
# pattern = [{"TEXT": "start_token"}, {"OP": "*"}, {"TEXT": "end_token"}]

# pattern_questions = [{"TEXT": "Questão"}, {"IS_DIGIT": True}]
# pattern_choices = [{"TEXT": "a"}, {"IS_PUNCT": True}, {"IS_UPPER": True}]

pattern = [{"TEXT": "Questão"}, {"IS_DIGIT": True},
           {"OP": "?"},
           {"TEXT": "a"}, {"IS_PUNCT": True}, {"IS_UPPER": True}]

# Initialize the Matcher with the pattern
matcher = Matcher(nlp.vocab)
matcher.add("Question_Statment_Pattern", [pattern])

# Your text
# text = '''This is some text
# start_token that I want to capture
# end_token this part.'''

text = '''Questão 1
Há uma comparação do Big Data com as soluções de BI (Business Intelligence)
, e podemos afirmar que existem semelhanças, mas é importante o entendimento do
que caracteriza e diferencia as soluções de Big Data de outras. Com relação à caracterização
das soluções de Big Data, assinale a alternativa correta:
a) A Veracidade caracteriza a fonte original dos dados e de como são armazenados
, aumentando a confiabilidade na solução.
b) O Valor está ligado à grande quantidade de dados processados nas soluções de Big Data.
c) A Variedade é a propriedade que dá agilidade para na análise de dados mesmo com quantidades
enormes de dados.
d) A Velocidade diz respeito aos diferentes tipos de dados que o Big Data pode processar
, indo de textos, áudios, vídeos até bancos de dados.
e) O Volume associa às soluções de Big Data aos processos de negócio, que justificam os esforços
de implantação.'''

# Parse the text
doc = nlp(text)

# Find matches
matches = matcher(doc)

# Extract text between matches
for match_id, start, end in matches:
    
    # Get the text between start and end tokens
    # captured_text = doc[start:end].text
    captured_text = doc[start+2:end-3].text
    # captured_text = doc[start+1:end-1].text
    # captured_text = doc[start+1:end-1].root.pos_
    
    # Output the captured text
    print("Captured text:", captured_text)