import sqlite3
import tkinter as tk
from tkinter import messagebox


# Função para conectar ao banco de dados (ou criar se não existir)
def conectar_banco():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    return conn, cursor


# Função para inserir dados no banco de dados
def inserir_cliente():
    nome = entry_nome.get()
    email = entry_email.get()

    if not nome or not email:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos!")
        return

    try:
        conn, cursor = conectar_banco()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        limpar_campos()
        listar_clientes()  # Atualiza a lista de clientes
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao adicionar cliente: {e}")


# Função para listar clientes no Listbox
def listar_clientes():
    try:
        conn, cursor = conectar_banco()
        cursor.execute("SELECT id, nome, email FROM clientes")
        clientes = cursor.fetchall()
        conn.close()

        # Limpar a lista antes de repopular
        listbox_clientes.delete(0, tk.END)

        for cliente in clientes:
            listbox_clientes.insert(tk.END, f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao listar clientes: {e}")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Cadastro de Clientes")

# Definir o layout da interface
frame = tk.Frame(root)
frame.pack(pady=10)

label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(frame, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1, padx=10, pady=5)

btn_inserir = tk.Button(frame, text="Inserir Cliente", command=inserir_cliente)
btn_inserir.grid(row=2, columnspan=2, pady=10)

# Listbox para exibir os clientes
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

label_lista = tk.Label(listbox_frame, text="Clientes Cadastrados:")
label_lista.pack()

listbox_clientes = tk.Listbox(listbox_frame, width=50, height=10)
listbox_clientes.pack()

# Botão para atualizar a lista de clientes
btn_atualizar = tk.Button(root, text="Atualizar Lista", command=listar_clientes)
btn_atualizar.pack(pady=10)

# Carregar a lista inicial de clientes
listar_clientes()

# Iniciar a interface
root.mainloop()