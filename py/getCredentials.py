import tkinter as tk
from tkinter import ttk
    
def get_credentials():
    # Criando a janela
    global janela
    janela = tk.Tk()
    janela.title("Login")
    
    # Definindo o tamanho da janela
    janela.geometry("200x100")  # Largura x Altura
    # janela.configure(bg='black')
    window_width = int(janela.winfo_screenwidth())
    window_height = int(janela.winfo_screenheight())
    
    # Estilizando a janela
    style = ttk.Style()
    style.theme_use('clam')  # Escolha o tema que desejar

    # Criando os campos de entrada (entry)
    label_login = tk.Label(janela, text="Login : ")
    label_login.grid(row=0, column=0, sticky=tk.E+tk.W)
    entry_login = tk.Entry(janela)
    entry_login.grid(row=0, column=1)

    label_senha = tk.Label(janela, text="Senha : ")
    label_senha.grid(row=1, column=0, sticky=tk.E+tk.W)
    entry_senha = tk.Entry(janela, show="*")  # O parâmetro show="*" esconde os caracteres digitados
    entry_senha.grid(row=1, column=1)

    # Botão para submeter o login e senha
    def on_login_click():
        global username, password
        username = entry_login.get()
        password = entry_senha.get()
        janela.destroy()
        
    # Ligando o evento de pressionar Enter ao botão de login
    def on_enter_pressed(event):
        on_login_click()
        
    botao_login = tk.Button(janela, text="Login", command=on_login_click, width=20)#, width=window_width*0.7, height=window_height*0.05)
    botao_login.grid(row=2, columnspan=2)
    janela.bind('<Return>', on_enter_pressed)

    # Executando a interface
    janela.mainloop()
    
    return username, password

# Function Test
# username, password = get_credentials()
# print(username)
# print(password)