import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app.validators import somente_letras, somente_numeros


class App:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Flight Monitor")
        self.janela.geometry("400x300")
        self.janela.resizable(False, False)


        self.criar_widgets()
        self.janela.mainloop()

    def criar_widgets(self):
        tk.Label(self.janela, text="Origem").pack(pady=(10, 0))
        self.entry_origem = tk.Entry(self.janela, width=30)
        self.entry_origem.pack()

        tk.Label(self.janela, text="Destino").pack(pady=(10, 0))
        self.entry_destino = tk.Entry(self.janela, width=30)
        self.entry_destino.pack()

        tk.Label(self.janela, text="Qtd Pessoas").pack(pady=(10, 0))
        
        self.combo_pessoas = ttk.Combobox(
            self.janela,
            values=[str(i) for i in range(1, 11)],
            state="readonly",
            width=5
        )
        self.combo_pessoas.pack()
        self.combo_pessoas.current(0)

        tk.Button(
            self.janela,
            text="Pesquisar",
            command=self.pesquisar
        ).pack(pady=20)

    def pesquisar(self):
        origem = self.entry_origem.get()
        destino = self.entry_destino.get()
        pessoas = self.combo_pessoas.get()

        if not somente_letras(origem):
            messagebox.showerror("Erro", "Origem deve conter apenas letras!")
            return
        
        if not somente_letras(destino):
            messagebox.showerror("Erro", "Destino deve conter apenas letras!")
            return
        
        if not somente_numeros(pessoas):
            messagebox.showerror("Erro", "Quantidade deve ser numérica!")
            return
        
        messagebox.showinfo(
            "Ok",
            f"Buscando voo de {origem} para {destino} para ({pessoas} pessoas)"
        )
