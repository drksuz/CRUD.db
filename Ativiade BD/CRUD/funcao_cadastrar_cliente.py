import sqlite3 
import funcao_conexao

#Criando uma função para coletar dados do cliente;
def cadastrarCliente():
    try:
        funcao_conexao.conectar()
        nome = input("Informe o seu nome: ")
        sobrenome = input("Informe o seu sobrenome: ")
        idade = int(input("Informe a sua idade: "))
        cpf = int(input("Informe o seu CPF: "))
        telefone = input("Informe o seu N* de telefone: ")
        endereco = input("Digite o seu endereço: ")
        cidade = input("Informe a cidade que você reside: ")
        estado = input("Informe o estado que você reside: ")

        inserir_cliente = "INSERT INTO cliente VALUES ('"+nome+"','"+sobrenome+"','"+str(idade)+"','"+str(cpf)+"','"+str(telefone)+"','"+endereco+"','"+cidade+"','"+estado+"')"
        funcao_conexao.cursor.execute(inserir_cliente)
        funcao_conexao.conn.commit()
        funcao_conexao.conn.close()
        print("O cliente foi cadastrado com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar o cliente",erro)