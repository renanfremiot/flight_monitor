import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from app.validators import somente_letras, somente_numeros


class App:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Flight Monitor")
        self.janela.geometry("400x400")
        self.janela.resizable(False, False)


        self.criar_widgets()
        self.janela.mainloop()

    def atualizar_campos_data(self):
        if self.tipo_viagem.get() == "ida_volta":
            self.label_volta.grid(row=6, column=0, pady=(10, 0))
            self.data_volta.grid(row=7, column=0)
        else:
            self.label_volta.grid_remove()
            self.data_volta.grid_remove()

    def criar_widgets(self):

        # Origem
        tk.Label(self.janela, text="Origem").grid(row=0, column=0, pady=(10, 0))
        self.entry_origem = tk.Entry(self.janela, width=30)
        self.entry_origem.grid(row=1, column=0)

        # Destino
        tk.Label(self.janela, text="Destino").grid(row=2, column=0, pady=(10, 0))
        self.entry_destino = tk.Entry(self.janela, width=30)
        self.entry_destino.grid(row=3, column=0)

        # Tipo viagem
        self.tipo_viagem = tk.StringVar(value="ida")

        tk.Label(self.janela, text="Data de Ida").grid(row=4, column=0, pady=(10, 0))

        self.data_ida = DateEntry(
            self.janela,
            date_pattern="yyyy-mm-dd",
            width=12
        )
        self.data_ida.grid(row=5, column=0)

        # Data Volta (começa escondido)
        self.label_volta = tk.Label(self.janela, text="Data de Volta")
        self.data_volta = DateEntry(
            self.janela,
            date_pattern="yyyy-mm-dd",
            width=12
        )

        # Radio buttons
        frame_tipo = tk.Frame(self.janela)
        frame_tipo.grid(row=8, column=0, pady=10)

        tk.Radiobutton(
            frame_tipo,
            text="Somente ida",
            variable=self.tipo_viagem,
            value="ida",
            command=self.atualizar_campos_data
        ).grid(row=0, column=0, padx=10)

        tk.Radiobutton(
            frame_tipo,
            text="Ida e volta",
            variable=self.tipo_viagem,
            value="ida_volta",
            command=self.atualizar_campos_data
        ).grid(row=0, column=1, padx=10)

        # Pessoas
        tk.Label(self.janela, text="Qtd Pessoas").grid(row=9, column=0, pady=(10, 0))

        self.combo_pessoas = ttk.Combobox(
            self.janela,
            values=[str(i) for i in range(1, 11)],
            state="readonly",
            width=5
        )
        self.combo_pessoas.grid(row=10, column=0)
        self.combo_pessoas.current(0)

        # Botão
        tk.Button(
            self.janela,
            text="Pesquisar",
            command=self.pesquisar
        ).grid(row=11, column=0, pady=20)

        self.atualizar_campos_data()


    def pesquisar(self):
        origem = self.entry_origem.get()
        destino = self.entry_destino.get()
        pessoas = self.combo_pessoas.get()
        data = self.data_ida.get()
        data_volta = None
        
        if self.tipo_viagem.get() == "ida_volta":
            data_volta = self.data_volta.get()

        if not somente_letras(origem):
            messagebox.showerror("Erro", "Origem deve conter apenas letras!")
            return
        
        if not somente_letras(destino):
            messagebox.showerror("Erro", "Destino deve conter apenas letras!")
            return
        
        if not somente_numeros(pessoas):
            messagebox.showerror("Erro", "Quantidade deve ser numérica!")
            return
        
        mensagem = (
            f"Buscando voo de {origem} para {destino}\n"
            f"Data de ida: {data}\n" 
            f"Pessoas: {pessoas}"
        )

        if data_volta:
            mensagem += f"\nVolta: {data_volta}"

        messagebox.showinfo("Busca", mensagem)
