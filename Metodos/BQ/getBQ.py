import regex as re
import docx

regex_Enunciado = r'(?<=\d[.]\s).*(?=\s+[a][)])'
# regex_Enunciado = r'(?ms)(?<=\d[.]\s).*(?=^\s[a][)]\s|^\s[a][.]\s)'
regex_Alternativa_A = r'(?<=[a][)]\s|\s[a][)]\s|[a][.]\s).*(?=[b][)]|\s+[b][)]|[b][.]\s+|\s+[b][.]\s+)'
regex_Alternativa_B = r'(?<=[b][)]\s|\s[b][)]\s|[b][.]\s).*(?=[c][)]|\s+[c][)]|[c][.]\s+|\s+[c][.]\s+)'
regex_Alternativa_C = r'(?<=[c][)]\s|\s[c][)]\s|[c][.]\s).*(?=[d][)]|\s+[d][)]|[d][.]\s+|\s+[d][.]\s+)'
regex_Alternativa_D = r'(?<=[d][)]\s|\s[d][)]\s|[d][.]\s).*(?=[e][)]|\s+[e][)]|[e][.]\s+|\s+[e][.]\s+)'
regex_Alternativa_E = r'(?<=[e][)]\s|[e][.]\s|[e][.]).*(?=\s+\d[.]|[.]|\z)'
regex_alternativas = r"(?ms)(?<=[[][']).*(?=['][]])"
#(?<=Questão\s\d\n)(?ms).*(?=\s+[a][)])
#(?<=Questão\s\d\n).*(?=\s+[a][)])

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
    """
    doc = read_document(path=path)
    enunciadosAll = len(re.findall(pattern=regex_Enunciado, string=doc))
    return enunciadosAll

def get_Enunciado(index: int, path: str) -> str:
    '''
    Return question statement
    
    Function to get the statement from the ```path``` file you get
    the ```index```+1 question
    '''
    doc = read_document(path=path)
    enunciado = re.findall(pattern=regex_Enunciado, string=doc).copy()[index]
    return enunciado

def get_Alternativa(index: int, path: str, choices: str) -> str:
    '''
    Return question choices
    
    Function to get the choices from the ```path``` file you get
    the ```index```+1 question and ```choices``` given in the method
    '''
    doc = read_document(path=path)
    match choices.upper():
        case 'A':
            alternativa = re.findall(pattern=regex_Alternativa_A, string=doc).copy()[index]
            return alternativa
        case 'B':
            alternativa = re.findall(pattern=regex_Alternativa_B, string=doc).copy()[index]
            return alternativa
        case 'C':
            alternativa = re.findall(pattern=regex_Alternativa_C, string=doc).copy()[index]
            return alternativa
        case 'D':
            alternativa = re.findall(pattern=regex_Alternativa_D, string=doc).copy()[index]
            return alternativa
        case 'E':
            alternativa = re.findall(pattern=regex_Alternativa_E, string=doc).copy()[index]
            return alternativa
        case _ :
            print('''Por favor verifique a chamada da função get_Alternativa, tipo de alternativa desejada
                  não esperada pela função''')

def main() -> None:
    path = r"C:\Users\rafad\Downloads\Questionário_Legislação e Rotina Trabalhista e Previdenciária _unidade 1_DIGITAL PAGES_ORIGINAL (revisado).docx"
    teste = enunciado_count(path=path)
    # teste2 = get_Enunciado(index=0, path=path)
    print(teste)
    # print(teste2)

if __name__ == "__main__":
    main()