import sqlite3
#Criando a função para conectar ao banco de dados
def conectar():
    try:
        global conn
        conn = sqlite3.connect("cadastro.db")
        global cursor
        cursor = conn.cursor()
        print("Conexão com o Banco realizada com sucesso!")
    except sqlite3.Error as erro:
        print("Erro de Conexão com o Banco de Dados")