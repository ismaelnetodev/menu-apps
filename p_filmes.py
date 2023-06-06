import tkinter as tk
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
import subprocess

api = '46ebbd3a' #this api might be unavailable \\ Essa API pode estar esgotada

def search_movie():
    search_query = entry.get()
    if search_query:
        try:
            response = requests.get(f"http://www.omdbapi.com/?apikey={api}&s={search_query}")
            data = response.json()
            
            if data["Response"] == "True":
                movies = data["Search"]
                movie_listbox.delete(0, tk.END)
                for movie in movies:
                    movie_title = movie["Title"]
                    movie_year = movie["Year"]
                    movie_listbox.insert(tk.END, f"{movie_title} ({movie_year})")
            else:
                if data["Error"] == "Invalid API Key!":
                    messagebox.showinfo("Erro", "Chave API inválida ou Esgotada")
                messagebox.showinfo("Erro", "Nenhum filme encontrado.")
        except requests.exceptions.RequestException:
            messagebox.showinfo("Erro", "Erro na solicitação.")
    else:
        messagebox.showinfo("Erro", "Digite um filme para pesquisar.")

def show_movie_info():
    selected_movie_index = movie_listbox.curselection()
    if selected_movie_index:
        selected_movie = movie_listbox.get(selected_movie_index)
        movie_title = selected_movie.split(" (")[0]
        try:
            response = requests.get(f"http://www.omdbapi.com/?apikey={api}&t={movie_title}")
            data = response.json()
            if data["Response"] == "True":
                messagebox.showinfo("Informações do Filme", f"Título: {data['Title']}\nAno: {data['Year']}\nGênero: {data['Genre']}\nDiretor: {data['Director']}\nAtores: {data['Actors']}\nSinopse: {data['Plot']}")
            else:
                messagebox.showinfo("Erro", "Falha ao obter informações do filme.")
        except requests.exceptions.RequestException:
            messagebox.showinfo("Erro", "Erro na solicitação.")
    else:
        messagebox.showinfo("Erro", "Selecione um filme da lista.")


def voltar_menu():
    window.destroy()
    subprocess.call(['python', 'menu.py'])

# Criar a janela principal
window = tk.Tk()
window.title("Pesquisar Filmes")
window.configure(bg="#3f4e51")
window.geometry("600x300")
window.resizable(False, False)
window.iconbitmap("imgs\icon_movie.ico")

#ícone
search_icon = ImageTk.PhotoImage(Image.open("imgs\search_icon.png"))

# Criar rótulo e entrada de texto para pesquisa
search_label = tk.Label(window, text="Digite o nome do filme:", bg="#3f4e51", fg="#fff", font="Arial 14")
search_label.grid(row=0, column=0, padx=20, pady=20)
entry = tk.Entry(window, width=30, borderwidth=0)
entry.grid(row=0, column=1, padx=0, pady=0)

# Criar botão de pesquisa
search_button = tk.Button(window, text="Pesquisar", command=search_movie, bg="#d06f4c", fg="white", padx=10, pady=10, image=search_icon, compound=tk.LEFT)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Criar lista para exibir resultados da pesquisa
movie_listbox = tk.Listbox(window, width=50, borderwidth=0, bg='#3f4e51', fg="white")
movie_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Criar botão para exibir informações do filme selecionado
info_button = tk.Button(window, text="Mostrar Informações", bg="#d06f4c", fg="white", border=0, command=show_movie_info, padx=5, pady=10)
info_button.grid(row=2, column=0, columnspan=4, padx=100, pady=20, sticky='nsew')

# Configurar o layout da grade
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

window.protocol("WM_DELETE_WINDOW", voltar_menu)

# Executar o loop principal da janela
window.mainloop()