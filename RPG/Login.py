from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.janela()
        self.button()
        self.widgets()
        root.mainloop()
    
    def janela(self):
        self.root.title("RPG")
        self.root.configure(background="#1C1C1C", )
        self.root.geometry("290x450")
        self.root.resizable(False,False)

    def button(self):
        #Botão Login
        self.login_btn = Button(self.root, text="Login", border= 0, bg="#00BFFF")
        self.login_btn.place(relx= 0.27, rely= 0.67, relwidth= 0.2, relheight= 0.1)
        #Botão Cadastrar
        self.cadastrar_btn = Button(self.root, text="Cadastro", border= 0, bg="#00FF7F")
        self.cadastrar_btn.place(relx= 0.52, rely= 0.67, relwidth= 0.2, relheight= 0.1)

    def widgets(self):
        #Nome de usuario
        self.lb_login = Label(self.root, text="Login:", bg="#FFFFF0", font= ("Berlin Sans FB", 13))
        self.lb_login.place(relx= 0.42, rely= 0.2)
        self.entry_login = Entry(self.root)
        self.entry_login.place(relx= 0.28, rely= 0.26, height= 35)
        #Senha
        self.lb_senha = Label(self.root, text="Senha:", bg="#FFFFF0", font= ("Berlin Sans FB", 13))
        self.lb_senha.place(relx= 0.42, rely= 0.4)
        self.entry_senha = Entry(self.root)
        self.entry_senha.place(relx= 0.28, rely= 0.46, height= 35)
        #
        
        
        
Application()