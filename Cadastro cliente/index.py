from tkinter import *
from tkinter import ttk

janela = Tk()

#Classe para função limpar
class Funcs():
    def limpa_tela(self):
        self.entry_codigo.delete(0,END)
        self.entry_nome.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.entry_telefone.delete(0, END)

#Classe para iniciar a janela
class Application(Funcs):
    def __init__(self):
        #Chama a "janela está que está fora da classe para dentro"
        self.janela = janela
        #Chama a função tela que está fora desta função
        self.tela()
        #chama a função que cria a "frame" na tela
        self.frames_na_tela()
        #chama a função com itens do frame 1
        self.widgets_frame1()
        #chama a função com lista do frame 2
        self.lista_frame2()
        #Manten a janela aberta
        janela.mainloop() 

    def tela(self):
        #Titulo da janela
        self.janela.title("Cadastro de cliente")
        #Configurações de backgroud da janela
        self.janela.configure(background= "#008B8B")
        #Configura o tamanho da janela Largura X Altura
        self.janela.geometry("700x400")
        #Respansibilidade: "True" permite responsiibilidade. "False não permite"
        self.janela.resizable(True, True)
        #Configura o tamanho maximo da tela
        self.janela.maxsize(width= 1000, height= 700)
        #Configura o tamanho maximo da tela
        self.janela.minsize(width= 500, height= 200)
    
    #função que cria a "div" na tela
    def frames_na_tela (self):
        #Cria o frame na tela
        #bg: cor do backgoung da frame
        #bd: tamanho da borda
        #highlightbackground: cor da borda
        #highlightthickness: largura da borda
        self.frame1 = Frame(self.janela, bd= 4, bg="#F5F5F5", highlightbackground= "#2F4F4F", highlightthickness= 3)
        #Place: apresenta frame na tela com responsividade. "relwidth e relheight: altura e largura o frame em escala de 0 á 1."
        #"relx e rely: onde o frame vai ser exibido inicialmente.
        #Valor para iniciar o frame: 0 é o lado esquerdo e 1 o lado direito.
        self.frame1.place(relx= 0.05, rely=0.05, relwidth= 0.9, relheight= 0.4)

        self.frame2 = Frame(self.janela, bd= 4, bg="#F5F5F5", highlightbackground= "#2F4F4F",               highlightthickness= 2)
        self.frame2.place(relx= 0.05, rely= 0.5, relwidth= 0.9, relheight= 0.4)

    def widgets_frame1(self):
        #Botão limpar
        self.btn_limpar = Button(self.frame1, text="Limpar", bd=2, bg= "#008B8B", fg= "white",  
                                 font= ("verdana", 8, "bold"), command= self.limpa_tela)
        self.btn_limpar.place(relx= 0.12, rely= 0.15, relwidth= 0.1, relheight= 0.15)
        #Botão busca 
        self.btn_buscar = Button(self.frame1, text="Buscar", bd=2, bg= "#008B8B", fg= "white",  
                                 font= ("verdana", 8, "bold"))
        self.btn_buscar.place(relx= 0.23, rely= 0.15, relwidth= 0.1, relheight= 0.15)
        #Botão novo
        self.btn_novo = Button(self.frame1, text="Novo", bd=2, bg= "#008B8B", fg= "white",  
                                 font= ("verdana", 8, "bold"))
        self.btn_novo.place(relx= 0.63, rely= 0.15, relwidth= 0.1, relheight= 0.15)
        #Botão alterar
        self.btn_alterar = Button(self.frame1, text="Alterar", bd=2, bg= "#008B8B", fg= "white",  
                                 font= ("verdana", 8, "bold"))
        self.btn_alterar.place(relx= 0.74, rely= 0.15, relwidth= 0.1, relheight= 0.15)
        #Botão apagar
        self.btn_apagar = Button(self.frame1, text="Apagar", bd=2, bg= "#008B8B", fg= "white",  
                                 font= ("verdana", 8, "bold"))
        self.btn_apagar.place(relx= 0.85, rely= 0.15, relwidth= 0.1, relheight= 0.15)
        
        #Criação da lebel codigo
        self.lb_codigo = Label(self.frame1, text="Código:", bg= "#F5F5F5", fg="#008B8B")
        self.lb_codigo.place(relx= 0.022, rely= 0.05)
        #Criando Emtry código
        self.entry_codigo = Entry(self.frame1)
        self.entry_codigo.place(relx= 0.023, rely= 0.17, relwidth= 0.08, relheight= 0.12)
        #Criação da lebel nome
        self.lb_nome = Label(self.frame1, text="Nome:", bg= "#F5F5F5", fg="#008B8B")
        self.lb_nome.place(relx= 0.02, rely= 0.5)
        #Criando Emtry nome
        self.entry_nome = Entry(self.frame1)
        self.entry_nome.place(relx= 0.09, rely= 0.51, relwidth= 0.20, relheight= 0.12)
        #Criando lebel cidade
        self.lb_cidade = Label(self.frame1, text="Cidade:", bg= "#F5F5F5", fg="#008B8B")
        self.lb_cidade.place(relx= 0.02, rely= 0.70)
        #Criando Emtry cidade
        self.entry_cidade = Entry(self.frame1)
        self.entry_cidade.place(relx= 0.10, rely= 0.72, relwidth= 0.40, relheight= 0.12)
        #Criando lebel Telefone
        self.lb_telefone = Label(self.frame1, text="Telefone:", bg= "#F5F5F5", fg="#008B8B")
        self.lb_telefone.place(relx= 0.52, rely= 0.7)
        #Criando Emtry Telefone
        self.entry_telefone = Entry(self.frame1)
        self.entry_telefone.place(relx= 0.61, rely= 0.72, relwidth= 0.3, relheight= 0.12)

    def lista_frame2(self):
        self.lista_cli = ttk.Treeview(self.frame2, height= 3, column=("Col1", "Col2", "Col3", "Col4"))
        #Nomeando as colunas da lista
        self.lista_cli.heading("#0", text="")
        self.lista_cli.heading("#1", text= "Código")
        self.lista_cli.heading("#2", text= "Nome")
        self.lista_cli.heading("#3", text= "Telefone")
        self.lista_cli.heading("#4", text= "Cidade")

        #Tamanho das colunas
        self.lista_cli.column("#0", width= 1)
        self.lista_cli.column("#1", width= 50)
        self.lista_cli.column("#2", width= 200)
        self.lista_cli.column("#3", width= 125)
        self.lista_cli.column("#4", width= 125)
        
        #Posição da lista
        self.lista_cli.place(relx= 0.01, rely= 0.05, relwidth= 0.95, relheight= 0.85)

        #criando scroll da lista
        self.scrollLista = Scrollbar(self.frame2, orient="vertical")
        self.lista_cli.configure(yscroll = self.scrollLista.set)
        self.scrollLista.place(relx= 0.96, rely= 0.05, relwidth= 0.04, relheight= 0.85)


Application()