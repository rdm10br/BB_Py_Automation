import tkinter as tk
from tkinter import messagebox, ttk
import regex as re
import tempfile, base64, zlib
from datetime import datetime

# set icon null
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
 
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

# Função para validar a data no formato DD/MM/AAAA
def validar_data(data):
    padrao_data = r"^\d{2}/\d{2}/\d{4}$"
    if re.match(padrao_data, data):
        try:
            # Tenta converter a string em um objeto datetime
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            # Se der erro na conversão, a data não é válida
            return False
    else:
        return False

# Função para receber credenciais
def get_data():
    # Criando a janela
    janela = tk.Tk()
    
    # Definindo variáveis de estilo
    grey = '#001A33'
    darkBlue = '#393D5C'
    width = 220
    height = 110
    button_width = int(width * 0.07)
    
    # Definindo janela
    janela.geometry(f"{width}x{height}")  # Largura x Altura
    janela.title(" Data")
    janela.attributes('-alpha', 0.9)
    janela.attributes('-topmost', True)
    janela.iconbitmap(default=ICON_PATH)
    janela.configure(bg=grey)
    
    # Estilizando a janela
    style = ttk.Style()
    style.theme_use('clam')

    # Função para verificar se os campos possuem datas válidas
    def data_click():
        global dataShow, dataHide
        dataShow = entry_dataShow.get()
        dataHide = entry_dataHide.get()
        
        if validar_data(dataShow) and validar_data(dataHide):
            janela.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, insira uma data válida no formato DD/MM/AAAA.")

    # Ligando o evento de pressionar Enter ao botão de login
    def on_enter_pressed(event):
        data_click()
        
    # Criando os campos de entrada (entry)
    label_login = tk.Label(janela, text="Mostrar Data : ", padx=5, bg=grey, fg='white')
    label_login.grid(row=0, column=0, sticky=tk.E + tk.W, pady=5, padx=5)
    entry_dataShow = tk.Entry(janela, width=button_width)
    entry_dataShow.grid(row=0, column=1)

    label_senha = tk.Label(janela, text="Ocultar Data : ", padx=5, bg=grey, fg='white')
    label_senha.grid(row=1, column=0, sticky=tk.E + tk.W, pady=5, padx=5)
    entry_dataHide = tk.Entry(janela, width=button_width)
    entry_dataHide.grid(row=1, column=1)

    # Botão para submeter o login e senha
    botao_login = tk.Button(janela, text="OK", command=data_click, width=button_width, bg=darkBlue, fg='white')
    botao_login.grid(row=2, column=1, padx=5, pady=5)
    janela.bind('<Return>', on_enter_pressed)

    # Executando a interface
    janela.mainloop()
    
    return dataShow, dataHide

# Function Test
def main ():
    dataShow, dataHide = get_data()
    print(dataShow)
    print(dataHide)
    return dataShow, dataHide

if __name__ == "__main__":
    main()