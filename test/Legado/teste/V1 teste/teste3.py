import re
from docx import Document
from openpyxl import Workbook
# from teste import Window

# Window.mainloop()


# Identificar texto em negrito
def id_right_alt(alternativa):
    texto_negrito = [run.text for run in alternativa.runs if run.bold]
    return ''.join(texto_negrito)

# Ler e identificar negrito no arquivo DOCX
def ler_right_alt(bq):
    doc = Document(bq)
    data = []
    for para in doc.paragraphs:
        data.append((para.text, id_right_alt(para)))
    return data

def process_data(data):
    questions = []
    options = {'a': [], 'b': [], 'c': [], 'd': [], 'e': []}
    option_keys = list(options.keys())
    current_option_index = 0
    correct_option_index = None

    for line, is_bold in data:
        # regex alternativas a-e   (?<=[a][)]\s|\s[a][)]\s|[a][.]\s).*(?=[b][)]|\s[b][)]|[b][.]\s)|(?<=[b][)]\s|\s[b][)]\s|[b][.]\s).*(?=[c][)]|\s[c][)]|[c][.]\s)|(?<=[c][)]\s|\s[c][)]\s|[c][.]\s).*(?=[d][)]|\s[d][)]|[d][.]\s)|(?<=[d][)]\s|\s[d][)]\s|[d][.]\s).*(?=[e][)]|\s[e][)]|\s[e][.]\s|\S[e]\.\s)|(?<=[e][)]|[e][[)]\s|\S[e][)]\s|\s[e][)]\s|\s[e]\.\s|[e]\.\s).*(?=\s\d[.]|[.]\S|\S)
        # if re.match(r'((?<=\d[.]\s).*|(?<=[1]\s).*)(?=[a][)])', line):  # Identifica uma questão
        if re.search(r'(?<=[a][)]\s|\s[a][)]\s|[a][.]\s).*(?=[b][)]|\s[b][)]|[b][.]\s)|(?<=[b][)]\s|\s[b][)]\s|[b][.]\s).*(?=[c][)]|\s[c][)]|[c][.]\s)|(?<=[c][)]\s|\s[c][)]\s|[c][.]\s).*(?=[d][)]|\s[d][)]|[d][.]\s)|(?<=[d][)]\s|\s[d][)]\s|[d][.]\s).*(?=[e][)]|\s[e][)]|\s[e][.]\s|\S[e]\.\s)|(?<=[e][)]\s|\s[e][)]\s|\s[e]\.\s|[e]\.\s).*(?=\s\d.|\S)', line):  # Identifica uma questão
            questions.append(line)
            current_option_index = 0
            correct_option_index = None
        elif re.search(r'^[a-e]\)', line):  # Identifica uma alternativa
            if current_option_index < len(option_keys):
                if is_bold:
                    correct_option_index = current_option_index
                options[option_keys[current_option_index]].append(line)
                current_option_index += 1

    return questions, options, correct_option_index

def write_to_excel(questions, options, correct_option_index, output_file):
    option_keys = list(options.keys())  # Definindo option_keys aqui
    wb = Workbook()
    ws = wb.active
    ws.append(['Enunciados', 'Alternativa a', 'Alternativa b', 'Alternativa c', 'Alternativa d', 'Alternativa e'])

    for i in range(len(questions)):
        row = [questions[i]]
        for j in range(5):
            if j == correct_option_index:
                row.append(options['a'][i])
            else:
                row.append(options[option_keys[(j+correct_option_index)%5]][i])
        ws.append(row)

    wb.save(output_file)

# Uso do código
data = ler_right_alt('TESTE.docx')
questions, options, correct_option_index = process_data(data)
write_to_excel(questions, options, correct_option_index, 'TESTE.xlsx')