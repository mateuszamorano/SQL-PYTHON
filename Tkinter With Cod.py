import tkinter as tk
from tkinter import messagebox
import mysql.connector


# Função para conectar ao banco de dados MySQL
def conectar_banco():
    try:
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="turmab"
        )
        return banco
    except mysql.connector.Error as err:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {err}")
        return None


# Função para inserir novo aluno no banco de dados
def inserir_aluno():
    nome = entry_nome.get()
    telefone = entry_telefone.get()

    if not nome or not telefone:
        messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos!")
        return

    try:
        banco = conectar_banco()
        if banco:
            cursor = banco.cursor()
            sql = "INSERT INTO alunos (nome, telefone) VALUES (%s, %s)"
            data = (nome, telefone)
            cursor.execute(sql, data)
            banco.commit()
            cursor.close()
            banco.close()
            messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
            limpar_campos()
            listar_alunos()  # Atualiza a lista de alunos
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao adicionar aluno: {err}")


# Função para listar alunos no Listbox
def listar_alunos():
    try:
        banco = conectar_banco()
        if banco:
            cursor = banco.cursor()
            cursor.execute("SELECT id, nome, telefone FROM alunos")
            alunos = cursor.fetchall()
            cursor.close()
            banco.close()

            # Limpar a lista antes de repopular
            listbox_alunos.delete(0, tk.END)

            for aluno in alunos:
                listbox_alunos.insert(tk.END, f"ID: {aluno[0]} | Nome: {aluno[1]} | Telefone: {aluno[2]}")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao listar alunos: {err}")


# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)


# Configuração da interface Tkinter
root = tk.Tk()
root.title("Cadastro de Alunos")

# Definir o layout da interface
frame = tk.Frame(root)
frame.pack(pady=10)

label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_telefone = tk.Label(frame, text="Telefone:")
label_telefone.grid(row=1, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(frame)
entry_telefone.grid(row=1, column=1, padx=10, pady=5)

btn_inserir = tk.Button(frame, text="Inserir Aluno", command=inserir_aluno)
btn_inserir.grid(row=2, columnspan=2, pady=10)

# Listbox para exibir os alunos cadastrados
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

label_lista = tk.Label(listbox_frame, text="Alunos Cadastrados:")
label_lista.pack()

listbox_alunos = tk.Listbox(listbox_frame, width=50, height=10)
listbox_alunos.pack()

# Botão para atualizar a lista de alunos
btn_atualizar = tk.Button(root, text="Atualizar Lista", command=listar_alunos)
btn_atualizar.pack(pady=10)

# Carregar a lista inicial de alunos
listar_alunos()

# Iniciar a interface
root.mainloop()
