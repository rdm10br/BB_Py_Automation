import getBQ, spacy
import regex as re
from spacy.matcher import Matcher

# nlp = spacy.load("en_core_web_sm")
# nlp = spacy.load("pt_core_news_sm")
nlp = spacy.load("pt_core_news_lg")
matcher = Matcher(nlp.vocab)
texto = getBQ.read_document(r'C:\Users\rafad\Downloads\Questionário_Legislação e Rotina Trabalhista e Previdenciária _unidade 1_DIGITAL PAGES_ORIGINAL (revisado).docx')
doc = nlp(texto)
pattern = [{"TEXT": "Questão"}, {"IS_DIGIT": True}]
matcher.add("Questions", [pattern])
matches = matcher(doc)


# def string_para_txt(string, nome_arquivo):
    # with open(nome_arquivo, 'w') as arquivo:
        # arquivo.write(string)


# nome_do_arquivo = "exemplo.txt"
# string_para_txt(texto, nome_do_arquivo)


# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.head.text)


# for match_id, start, end in matches:
#     # Get the matched span
#     matched_span = doc[start:end]
#     print(matched_span.text)

print(len(matches))
# print(doc)