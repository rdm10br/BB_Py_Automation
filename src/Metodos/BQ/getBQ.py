import regex as re
import docx, spacy
from spacy.matcher import Matcher
from functools import lru_cache

nlp = spacy.load("pt_core_news_sm")
matcher = Matcher(nlp.vocab)

# regex_Enunciado = r'(?<=Questão\s\d\n\n)?.*(?=\n+\s+[a][)])'

# regex_Alternativa_A = r'(?<=[a][)]\s|\s[a][)]\s|[a][.]\s).*'\
# r'(?=[b][)]|\s+[b][)]|[b][.]\s+|\s+[b][.]\s+)'

# regex_Alternativa_B = r'(?<=[b][)]\s|\s[b][)]\s|[b][.]\s).*'\
# r'(?=[c][)]|\s+[c][)]|[c][.]\s+|\s+[c][.]\s+)'

# regex_Alternativa_C = r'(?<=[c][)]\s|\s[c][)]\s|[c][.]\s).*'\
# r'(?=[d][)]|\s+[d][)]|[d][.]\s+|\s+[d][.]\s+)'

# regex_Alternativa_D = r'(?<=[d][)]\s|\s[d][)]\s|[d][.]\s).*'\
# r'(?=[e][)]|\s+[e][)]|[e][.]\s+|\s+[e][.]\s+)'

# regex_Alternativa_E = r'(?<=[e][)]\s|[e][.]\s|[e][.]).*'\
# r'(?=\s+\d[.]|[.]|\z)'

# regex_alternativas = r"(?ms)(?<=[[][']).*(?=['][]])"

#(?<=Questão\s\d\n)(?ms).*(?=\s+[a][)])
#(?<=Questão\s\d\n).*(?=\s+[a][)])
#(?<=Questão\s\d\n\n)(?ms).*(?=\n+\s+[a][)])
#(?<=Questão\s\d\n\n)?.*(?=\n+\s+[a][)])

#(?<=\d[.]\s).*(?=\s+[a][)])
#(?ms)(?<=\d[.]\s).*(?=^\s[a][)]\s|^\s[a][.]\s)
@lru_cache
def read_document(path) -> str:
    '''
    Return the file content
    
    Function to read a docx file, given the file path in the ```path```
    variable, and store in a variable
    '''
    doc = docx.Document(docx=path)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return "\n".join(content)

def enunciado_count (path: str) -> int:
    """
    Return how many statments on the file

    Args:
        path (str): Doc Path to the Questionary

    Returns:
        int: mathes - how many Statements this questionary have
    """
    texto = read_document(path)
    doc = nlp(texto)
    
    pattern = [{"LEMMA": "Questão"}, {"IS_DIGIT": True}]
    matcher.add("Questions", [pattern])
    
    matches = len(matcher(doc))
    
    return matches

def extract_text_between_markers(text, start_marker, end_marker):
    """
    Function to extract text between two markers using regular expressions.
    """
    # pattern = re.compile(rf'{re.escape(start_marker)}(.*?)\s*{re.escape(end_marker)}', re.DOTALL)
    pattern = re.compile(rf'{re.escape(start_marker)}(.*?)(?=^\s*{re.escape(end_marker)})', re.DOTALL | re.MULTILINE)
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    else:
        return ""

@lru_cache
def get_enunciados (filename: str):
    text = read_document(filename)
    q = enunciado_count(filename)
    question = []
    
    for i in range(q):
        i+=1
        start_marker = f'Questão {i}'
        end_marker = r'a)'
        extracted_text = extract_text_between_markers(text, start_marker, end_marker)
        question.append(extracted_text)
    return question

def get_Enunciado(index: int, path: str) -> str:
    '''
    Return question statement
    
    Function to get the statement from the ```path``` file you get
    the ```index```+1 question
    '''
    # doc = read_document(path=path)
    # enunciado = re.findall(pattern=regex_Enunciado, string=doc).copy()[index]
    # return enunciado
    question = get_enunciados(filename=path)
    return question[index]

@lru_cache
def get_Alternativa(index: int, path: str, choices: str) -> str:
    '''
    Return question choices
    
    Function to get the choices from the ```path``` file you get
    the ```index```+1 question and ```choices``` given in the method
    '''
    doc = read_document(path=path)
    match choices.upper():
        case 'A':
            start_marker = get_Enunciado(index=index, path=path)
            end_marker = r'b)'
            match = extract_text_between_markers(text=doc, start_marker=start_marker, end_marker=end_marker)
            if match:
                cleaned_text = re.sub(r'^[a-e]\)\s*', '', match, flags=re.MULTILINE)
                return cleaned_text
        case 'B':
            start_marker = get_Alternativa(index=index, path=path, choices='a')
            end_marker = r'c)'
            # verificar casos de alternativas repetidas e v ou f
            match = extract_text_between_markers(text=doc, start_marker=start_marker, end_marker=end_marker)
            if match:
                cleaned_text = re.sub(r'^[a-e]\)\s*', '', match, flags=re.MULTILINE)
                return cleaned_text
        case 'C':
            start_marker = get_Alternativa(index=index, path=path, choices='b')
            end_marker = r'd)'
            match = extract_text_between_markers(text=doc, start_marker=start_marker, end_marker=end_marker)
            if match:
                cleaned_text = re.sub(r'^[a-e]\)\s*', '', match, flags=re.MULTILINE)
                return cleaned_text
        case 'D':
            start_marker = get_Alternativa(index=index, path=path, choices='c')
            end_marker = r'e)'
            match = extract_text_between_markers(text=doc, start_marker=start_marker, end_marker=end_marker)
            if match:
                cleaned_text = re.sub(r'^[a-e]\)\s*', '', match, flags=re.MULTILINE)
                return cleaned_text
        case 'E':
            start_marker = get_Alternativa(index=index, path=path, choices='d')
            # end_marker = r'Justificativa|Gabarito|Questão|\d\.|\d+\.'
            end_marker = r'Justificativa'
            match = extract_text_between_markers(text=doc, start_marker=start_marker, end_marker=end_marker)
            if match:
                cleaned_text = re.sub(r'^[a-e]\)\s*', '', match, flags=re.MULTILINE)
                return cleaned_text
        case _ :
            print('''Por favor verifique a chamada da função get_Alternativa,
                  tipo de alternativa desejada não esperada pela função''')


def main() -> None:
    path = r"C:\Users\013190873\Downloads\Questionário_ UNID 1_ Transformação Digital , Sistemas Computacionais e o Futuro da Tecnologia_ REV_Parâmetros_DI Carlos_com Orto.docx"
    teste = enunciado_count(path=path)
    index = 11
    teste2 = get_Enunciado(index=index, path=path)
    teste3 = get_Alternativa(index=index, path=path, choices='e')
    print(f'\n Enunciado count: {teste}')
    print(f'\n Question:\n{teste2}')
    print(f'\n Choices:\n{teste3}')

if __name__ == "__main__":
    main()