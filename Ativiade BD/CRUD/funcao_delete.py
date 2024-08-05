import sqlite3
import funcao_conexao
def deletarb():
    cpf = input("Informe o CPF do cliente que deseja deletar: ")
    try:
        resultado = funcao_conexao.conn.execute('''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado!")
        else:
            banco = sqlite3.connect('cadastro.db') 

            cursor = banco.cursor() 

            cursor.execute("DELETE from cliente WHERE cpf = '"+cpf+"'")

            banco.commit()
            banco.close
            print("Cadastro deletado do banco de dados!!")

    except sqlite3.Error as erro:
        print("Erro ao excluir: ",erro)