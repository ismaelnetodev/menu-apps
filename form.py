from tkinter import *
import os

c_bg = "#c9d1c9"
white_color = "#000"

janela = Tk()
janela.geometry("500x500")
janela.configure(bg=c_bg)
janela.title("Formulário")
janela.overrideredirect(1)

titulo = Label(janela, text="Formulário de Inscrição", font="Arial 18", bg=c_bg, fg=white_color)
titulo.pack()

def informacoes():
    nome_info = nome.get()
    senha_info = senha.get()
    lang_info = lang.get()

    with open("nome.txt", "w") as file:
        file.write(nome_info)
    janela.destroy()
    os.system("menu.py")

def fechar():
    janela.destroy()

lbNome = Label(janela, text="Digite seu nome: ", font="Arial 14", bg=c_bg, fg=white_color)
lbSenha = Label(janela, text="Crie uma Senha", font="Arial 14", bg=c_bg, fg=white_color)
lbLinguagem = Label(janela, text="Selecione a linguagem que você quer aprender:", font="Arial 14", bg=c_bg, fg=white_color)

lbNome.place(x=15, y=70)
lbSenha.place(x=15, y=140)
lbLinguagem.place(x=15, y=210)

nome = StringVar()
senha = StringVar()
lang = IntVar()


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

submit = Button(janela, text="Enviar!", width="20", height="2", command=informacoes, font="Arial 14")
submit.place(x=15, y=290)

sair = Button(janela, text="X", command=fechar, width=2, height=1, font="Arial 16").place(x="460", y="5")

janela.mainloop()