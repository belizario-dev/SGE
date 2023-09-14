import tkinter as tk
from datetime import datetime, timedelta

class Estoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_item(self, item, quantidade):
        if item in self.estoque:
            self.estoque[item]['quantidade'] += quantidade
        else:
            self.estoque[item] = {'quantidade': quantidade, 'ultima_operacao': self.get_current_time(), 'tipo_operacao': 'Adição'}

    def remover_item(self, item, quantidade):
        if item in self.estoque:
            if self.estoque[item]['quantidade'] >= quantidade:
                self.estoque[item]['quantidade'] -= quantidade
                if self.estoque[item]['quantidade'] == 0:
                    del self.estoque[item]
                self.estoque[item]['ultima_operacao'] = self.get_current_time()
                self.estoque[item]['tipo_operacao'] = 'Remoção'
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Item não encontrado no estoque.")

    def get_current_time(self):
        return datetime.now()

def adicionar_item():
    item = item_entry.get()
    quantidade = int(quantidade_entry.get())
    estoque.adicionar_item(item, quantidade)
    update_listbox()

def remover_item():
    item = item_entry.get()
    quantidade = int(quantidade_entry.get())
    estoque.remover_item(item, quantidade)
    update_listbox()

def filtrar_itens(*args):
    search_term = search_var.get().lower()
    if search_term:
        filtered_items = [item for item in estoque.estoque.keys() if search_term in item.lower()]
    else:
        filtered_items = None
    update_listbox(filtered_items)

def update_listbox(items=None):
    listbox.delete(0, tk.END)
    if items is None:
        items = estoque.estoque.keys()
    for item in items:
        quantidade = estoque.estoque[item]['quantidade']
        ultima_operacao = estoque.estoque[item]['ultima_operacao']
        tipo_operacao = estoque.estoque[item]['tipo_operacao']
        listbox.insert(tk.END, f"{item}: {quantidade} unidades ({tipo_operacao}: {ultima_operacao.strftime('%Y-%m-%d %H:%M:%S')})")

estoque = Estoque()

app = tk.Tk()
app.title("Sistema de Gerenciamento de Estoque")

app.geometry("500x400")
app.configure(bg="#f0f0f0")

title_label = tk.Label(app, text="Sistema de Gerenciamento de Estoque", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

frame = tk.Frame(app, bg="#f0f0f0")
frame.pack()

item_label = tk.Label(frame, text="Item:", bg="#f0f0f0")
item_label.grid(row=0, column=0, padx=10, pady=5)

item_entry = tk.Entry(frame)
item_entry.grid(row=0, column=1, padx=10, pady=5)

quantidade_label = tk.Label(frame, text="Quantidade:", bg="#f0f0f0")
quantidade_label.grid(row=1, column=0, padx=10, pady=5)

quantidade_entry = tk.Entry(frame)
quantidade_entry.grid(row=1, column=1, padx=10, pady=5)

adicionar_button = tk.Button(frame, text="Adicionar Item", command=adicionar_item, bg="#008CBA", fg="white")
adicionar_button.grid(row=2, columnspan=2, padx=10, pady=10)

remover_button = tk.Button(frame, text="Remover Item", command=remover_item, bg="#D33F49", fg="white")
remover_button.grid(row=3, columnspan=2, padx=10, pady=5)

search_label = tk.Label(app, text="Pesquisar Item:", bg="#f0f0f0")
search_label.pack(pady=5)

search_var = tk.StringVar()
search_var.trace("w", filtrar_itens)
search_entry = tk.Entry(app, textvariable=search_var)
search_entry.pack()

listbox_frame = tk.Frame(app)
listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

listbox = tk.Listbox(listbox_frame, bg="white", selectbackground="#f0f0f0", selectmode=tk.SINGLE)
listbox.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

update_listbox()

app.mainloop()
