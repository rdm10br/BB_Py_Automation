import tkinter as tk
from tkinter import ttk

# set icon null
import tempfile, base64, zlib
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
 
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
    
# Função para receber credenciais
def get_data():
    # Criando a janela
    # global janela
    janela = tk.Tk()
    
    #Setting Variables
    grey = '#001A33'
    # lightGrey = '#DCDEE0'
    darkBlue = '#393D5C'
    width = 220
    height = 110
    # button_width = int(window_width*0.0125) #win10
    button_width = int(width*0.07) #win11
    
    # Definindo janela
    # janela.wm_attributes('-toolwindow', 'True')
    janela.geometry(f"{width}x{height}")  # Largura x Altura
    janela.title(" Data")
    janela.attributes('-alpha',0.9)
    janela.attributes('-topmost',True)
    janela.iconbitmap(default=ICON_PATH)
    janela.configure(bg=grey)
    
    # Estilizando a janela
    style = ttk.Style()
    style.theme_use('clam')  # Escolha o tema que desejar

    # Criando os campos de entrada (entry)
    label_login = tk.Label(janela, text="Mostrar Data : ", padx=5, bg=grey, fg='white')
    label_login.grid(row=0, column=0, sticky=tk.E+tk.W, pady=5, padx=5)
    entry_dataShow = tk.Entry(janela, width=button_width)
    entry_dataShow.grid(row=0, column=1)

    label_senha = tk.Label(janela, text="Ocultar Data : ", padx=5, bg=grey, fg='white')
    label_senha.grid(row=1, column=0, sticky=tk.E+tk.W, pady=5, padx=5)
    entry_dataHide = tk.Entry(janela, width=button_width)  # O parâmetro show="*" esconde os caracteres digitados
    entry_dataHide.grid(row=1, column=1)

    # Botão para submeter o login e senha
    def data_click():
        global dataShow, dataHide
        dataShow = entry_dataShow.get()
        dataHide = entry_dataHide.get()
        janela.destroy()
        
    # Ligando o evento de pressionar Enter ao botão de login
    def on_enter_pressed(event):
        data_click()
        
    botao_login = tk.Button(janela, text="OK", command=data_click, width=button_width, bg=darkBlue, fg='white')
    botao_login.grid(row=2, column=1, padx=5, pady=5)
    janela.bind('<Return>', on_enter_pressed)

    # Executando a interface
    janela.mainloop()
    
    return dataShow, dataHide

# Function Test
# dataShow, dataHide = get_data()
# print(dataShow)
# print(dataHide)