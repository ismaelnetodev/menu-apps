from tkinter import *
import os

janela = Tk()
janela.geometry("500x500")
janela.title("Formulário")

titulo = Label(janela, text="Formulário de Inscrição")
titulo.pack()

def informacoes():
    nome_info = nome.get()
    senha_info = senha.get()
    lang_info = lang.get()

    with open("nome.txt", "w") as file:
        file.write(nome_info)
    janela.destroy()
    os.system("menu.py")
    print(f"Nome: {nome_info}\n Senha: {senha_info}\n Linguagem: {lang_info}")

lbNome = Label(janela, text="Digite seu nome: ")
lbSenha = Label(janela, text="Crie uma Senha")
lbLinguagem = Label(janela, text="Selecione a linguagem que você quer aprender:")

lbNome.place(x=15, y=70)
lbSenha.place(x=15, y=140)
lbLinguagem.place(x=15, y=210)

nome = StringVar()
senha = StringVar()
lang = IntVar()


eNome = Entry(janela, textvariable=nome, width=30)
eSenha = Entry(janela, textvariable=senha, show='*', width=30)
eLinguagem1 = Radiobutton(janela, text="Python", variable=lang, value=1)
eLinguagem2 = Radiobutton(janela, text="Java", variable=lang, value=2)
eLinguagem3 = Radiobutton(janela, text="C/C++", variable=lang, value=3)

eNome.place(x=15, y=100)
eSenha.place(x=15, y=180)
eLinguagem1.place(x=15, y=240)
eLinguagem2.place(x=80, y=240)
eLinguagem3.place(x=130, y=240)

submit = Button(janela, text="Enviar!", width="30", height="2", command=informacoes)
submit.place(x=15, y=290)

janela.mainloop()