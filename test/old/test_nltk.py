import regex as re
import docx, spacy
from spacy.matcher import Matcher
def read_document(path):
    """
    Function to read a docx file and return its content as a string.
    """
    doc = docx.Document(path)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return "\n".join(content)

def extract_text_between_markers(text, start_marker, end_marker):
    """
    Function to extract text between two markers using regular expressions.
    """
    pattern = re.compile(rf'{re.escape(start_marker)}(.*?)\s*{re.escape(end_marker)}', re.DOTALL)
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    else:
        return ""
    
def enunciado_count (path: str) -> int:
    """
    Return how many statments on the file

    Args:
        path (str): Doc Path to the Questionary

    Returns:
        int: mathes - how many Statements this questionary have
    """
    nlp = spacy.load("pt_core_news_sm")
    matcher = Matcher(nlp.vocab)
    texto = read_document(path)
    doc = nlp(texto)
    
    pattern = [{"TEXT": "Questão"}, {"IS_DIGIT": True}]
    matcher.add("Questions", [pattern])
    
    matches = len(matcher(doc))
    
    return matches

def get_enunciados (filename: str):
    text = read_document(filename)
    q = enunciado_count(filename)
    question = []
    
    for i in range(q):
        i+=1
        start_marker = f'Questão {i}'
        end_marker = 'a)'
        extracted_text = extract_text_between_markers(text, start_marker, end_marker)
        question.append(extracted_text)
    return question

if __name__ == '__main__':
    filename = r'C:\Users\013190873\Downloads\teste.docx'
    question =get_enunciados(filename=filename)
    print(f'\n{question[0]}')