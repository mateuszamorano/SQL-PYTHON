import requests
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmab"
)
meucursor = banco.cursor()

cep = input("Digite o CEP: ")

if len(cep) == 8:
    link = f"https://viacep.com.br/ws/53439490/json"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    sql = "insert into endereco(cep, complemento, logradouro) values (%s,%s,%s)"
    complemento = dic_requisicao["complemento"]
    cep = dic_requisicao["cep"]
    logradouro = dic_requisicao["logradouro"]
    uf = dic_requisicao["uf"]
    cidade = dic_requisicao["localidade"]
    bairro = dic_requisicao["bairro"]
    data = (cep, logradouro, complemento)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()
    banco.close()
    print(dic_requisicao)

else:
    print("CEP inválido!")