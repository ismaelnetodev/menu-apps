from tkinter import *
import os
from PIL import ImageTk, Image

with open("nome.txt", "r") as file:
    nome_salvo = file.read()


janela = Tk()
janela.geometry("800x600")
janela.title("Menu Principal")
janela.overrideredirect(1)

def abrir_jogo():
    janela.destroy()
    os.system("jogo.py")

def abrir_filmes():
    janela.destroy()
    os.system("p_filmes.py")

def abrir_chat():
    janela.destroy()
    os.system('solvix.py')

def fechar():
    janela.destroy()
    os.system('form.py')

userIcon = ImageTk.PhotoImage(Image.open("imgs\\user.png"))
jogoIcon = ImageTk.PhotoImage(Image.open("imgs\\jogo.png"))
filmeIcon = ImageTk.PhotoImage(Image.open("imgs\\filme.png"))
chatIcon = ImageTk.PhotoImage(Image.open("imgs\\icone.png"))

lbNome = Label(janela, compound=LEFT, text="Olá, " + nome_salvo, image=userIcon)
lbNome.place(x=0, y=0)

btn_Jogo = Button(janela, command=abrir_jogo, image=jogoIcon, width=180, height=128)
btn_Jogo.place(x=100, y=100)
lbJogo = Label(janela, text="Jogar Jogo-da-Velha", font="Arial 16").place(x=100, y=240)

btn_Filme = Button(janela, command=abrir_filmes, image=filmeIcon, width=180, height=128)
btn_Filme.place(x=400, y=100)

lbJogoFilme = Label(janela, text="Pesquisar Filmes", font="Arial 16").place(x=420, y=240)

btn_chat = Button(janela, command=abrir_chat, image=chatIcon, width=180, height=128)
btn_chat.place(x=280, y=350)

lbChat = Label(janela, text="Solvix", font="Arial 16").place(x=350, y=490)

sair = Button(janela, text="X", command=fechar, width=2, height=1, font="Arial 16").place(x="760", y="5")

janela.mainloop()