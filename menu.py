from tkinter import *
import form

root = Tk()

getNome = form.nomeUser

lbNome = Label(root, text=getNome).pack()



root.mainloop()