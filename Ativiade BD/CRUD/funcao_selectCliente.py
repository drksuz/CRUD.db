import funcao_conexao
import sqlite3

def exibirCliente():
    funcao_conexao.conectar()
    resultado = funcao_conexao.cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("------------------------------------------------------------")
        print("Nome: ",result[0])
        print("Sobrenome: ",result[1])
        print("Idade: ",result[2])
        print("CPF: ",result[3])
        print("Telefone: ",result[4])
        print("Endereço: ",result[5])
        print("Cidade: ",result[6])
        print("Estado: ",result[7])
        #funcao_conexao.conn.close()

def consultarCliente():
    #funcao_conexao.conectar()
    cpf = input("Informe o CPF do cliente que deseja consultar: ")
    try:
        resultado = funcao_conexao.conn.execute('''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado!")
        else:
            for result in resultado:
                print("------------------------------------------------")
                print("Nome: ",result[0])
                print("Sobrenome: ",result[1])
                print("Idade: ",result[2])
                print("CPF: ",result[3])
                print("Telefone: ",result[4])
                print("Endereço: ",result[5])
                print("Cidade: ",result[6])
                print("Estado: ",result[7])
        return cpf
    except sqlite3.Error as erro:
        print("Erro ao encontrar Cliente",erro)
    funcao_conexao.conn.close()