from tkinter import*

janela = Tk()

janela.title("botao")

janela.geometry ("600x600")


img = PhotoImage(file="divertidamente-removebg-preview.png")
area_img= Label(janela,image=img)
area_img.pack()


usuario= Label(janela,text="Usuário")
usuario.pack()
campo_usuario= Entry(janela)
campo_usuario.pack()

senha = Label(janela, text="Senha")
senha.pack()
campo_senha= Entry(janela)
campo_senha.pack()



btn1 = Button(janela, text="Entrar!")
btn1.pack(side=TOP)

janela.mainloop()