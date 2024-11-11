import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmab"
)
print(banco)

#meucursor = banco.cursor()
#pesquisa = 'select * from alunos;'
#meucursor.execute(pesquisa)
#resultado = meucursor.fetchall()
#for x in resultado:
    #print(f"{x}")
#meucursor.close()
#banco.close()

#nome1 = input("Digite seu nome: ")
#telefone1 = input("Digite seu telefone: ")
#sql = "insert into alunos (nome, telefone) values (%s,%s)"
#data = (nome1, telefone1)
#meucursor.execute(sql, data)
#banco.commit()
#print()

meucursor = banco.cursor()

while True:
    menu = int(input("Digite 1 para pesquisar todos os dados da Database"
                 "\n Digite 2 para inserir um novo nome e telefone"
                 "\n Digite 3 para sair do sistema: "))

    if menu == 1:
        pesquisa = 'select * from alunos;'
        meucursor.execute(pesquisa)
        resultado = meucursor.fetchall()
        for z in resultado:
            print(z)

    elif menu == 2:
        nome1 = input("Digite seu nome: ")
        telefone1 = input("Digite seu telefone: ")

    elif menu == 3:
        meucursor.close()
        banco.close()
        print("Sistema encerrado!")
        break

#1 - pesquisar
#2 - inserir
#3 - sair