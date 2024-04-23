import getBQ

def string_para_txt(string, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(string)


# Exemplo de uso
texto = getBQ.read_document(r'C:\Users\013190873\Downloads\teste.docx') #"Esta é uma string que será gravada em um arquivo de texto."
nome_do_arquivo = "exemplo.txt"

string_para_txt(texto, nome_do_arquivo)