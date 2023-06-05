from tkinter import *
import os
from PIL import ImageTk, Image

with open("nome.txt", "r") as file:
    nome_salvo = file.read()

def abrir_jogo():
    os.system("jogo.py")

janela = Tk()
janela.geometry("500x300")
janela.title("Menu Principal")

userIcon = ImageTk.PhotoImage(Image.open("imgs\\user.png"))

lbNome = Label(janela, compound=LEFT, text="Olá, " + nome_salvo, image=userIcon)
lbNome.place(x=0, y=0)

btn_Jogo = Button(janela, text="Jogo da Velha", command=abrir_jogo)
btn_Jogo.place(x=500/4, y=300/2)


janela.mainloop()