from tkinter import*

janela = Tk()

janela.title("botao")

janela.geometry ("600x600")


def enter_menu():
    janela.destroy()
    with open("menu.py", 'r') as menu:
        code = menu.read()
        exec(code)


'''
img = PhotoImage(file="divertidamente-removebg-preview.png")
area_img= Label(janela,image=img)
area_img.pack()'''


usuario= Label(janela,text="Usuário")
usuario.pack()
campo_usuario= Entry(janela)
campo_usuario.pack()

senha = Label(janela, text="Senha")
senha.pack()
campo_senha= Entry(janela)
campo_senha.pack()

nomeUser = campo_usuario.get()

btn1 = Button(janela, text="Entrar!", command=enter_menu)
btn1.pack(side=TOP)

janela.mainloop()