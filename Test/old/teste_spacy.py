from spacy_llm.util import assemble

nlp = assemble(r'Test\config.cfg')
doc = nlp("You look gorgeous!")
print(doc.cats)