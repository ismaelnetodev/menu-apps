#Bibliotecas
from tkinter import *
import os

#define as cores
c_bg = "#c9d1c9"
white_color = "#000"

#cria e configura a janela
janela = Tk()
janela.geometry("500x500")
janela.configure(bg=c_bg)
janela.title("Formulário")
janela.overrideredirect(1) #remove as molduras da janela, tal como as opções de fechar, minimizar e maximizar

titulo = Label(janela, text="Formulário de Inscrição", font="Arial 18", bg=c_bg, fg=white_color)
titulo.pack() #Cria um label para o título

#Esse método pega as informações do formulário e salva em um arquivo chamado nome.txt
#Ele é executado ao clicar no botão enviar e também fecha a janela e abre o menu.
def informacoes():
    nome_info = nome.get()
    senha_info = senha.get()
    lang_info = lang.get()

    with open("nome.txt", "w") as file:
        file.write(nome_info)
    janela.destroy()
    os.system("menu.py")

#Esse é método é executado ao clicar no "X" e somente fecha a janela
def fechar():
    janela.destroy()

#Aqui são as labels
lbNome = Label(janela, text="Digite seu nome: ", font="Arial 14", bg=c_bg, fg=white_color)
lbSenha = Label(janela, text="Crie uma Senha", font="Arial 14", bg=c_bg, fg=white_color)
lbLinguagem = Label(janela, text="Selecione a linguagem que você quer aprender:", font="Arial 14", bg=c_bg, fg=white_color)

lbNome.place(x=15, y=70)
lbSenha.place(x=15, y=140)
lbLinguagem.place(x=15, y=210)

#Aqui salva as informaçõs do formulário em variavéis
nome = StringVar()
senha = StringVar()
lang = IntVar()

#Aqui são os campos de texto e o RadioButton, as informações aqui são salvas nas variaveis acima
eNome = Entry(janela, textvariable=nome, width=30)
eSenha = Entry(janela, textvariable=senha, show='*', width=30)
eLinguagem1 = Radiobutton(janela, text="Python", variable=lang, value=1, bg=c_bg, fg=white_color)
eLinguagem2 = Radiobutton(janela, text="Java", variable=lang, value=2, bg=c_bg, fg=white_color)
eLinguagem3 = Radiobutton(janela, text="C/C++", variable=lang, value=3, bg=c_bg, fg=white_color)

eNome.place(x=15, y=100)
eSenha.place(x=15, y=180)
eLinguagem1.place(x=15, y=240)
eLinguagem2.place(x=80, y=240)
eLinguagem3.place(x=130, y=240)

#Aqui é o botão de enviar
submit = Button(janela, text="Enviar!", width="20", height="2", command=informacoes, font="Arial 14")
submit.place(x=15, y=290)

#E aqui o botão de sair
sair = Button(janela, text="X", command=fechar, width=2, font="Arial 18").place(x="462", y="3")

janela.mainloop()