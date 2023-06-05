from tkinter import *
import os
from PIL import ImageTk, Image

with open("nome.txt", "r") as file:
    nome_salvo = file.read()

def abrir_jogo():
    os.system("jogo.py")

def abrir_filmes():
    os.system("p_filmes.py")

janela = Tk()
janela.geometry("800x600")
janela.title("Menu Principal")

userIcon = ImageTk.PhotoImage(Image.open("imgs\\user.png"))
jogoIcon = ImageTk.PhotoImage(Image.open("imgs\\jogo.png"))
filmeIcon = ImageTk.PhotoImage(Image.open("imgs\\filme.png"))

lbNome = Label(janela, compound=LEFT, text="Olá, " + nome_salvo, image=userIcon)
lbNome.place(x=0, y=0)

btn_Jogo = Button(janela, command=abrir_jogo, image=jogoIcon, width=180, height=128)
btn_Jogo.place(x=100, y=100)
lbJogo = Label(janela, text="Jogar Jogo-da-Velha", font="Arial 16").place(x=100, y=240)

btn_Filme = Button(janela, command=abrir_filmes, image=filmeIcon, width=180, height=128)
btn_Filme.place(x=400, y=100)

lbJogoFilme = Label(janela, text="Pesquisar Filmes", font="Arial 16").place(x=420, y=240)


janela.mainloop()