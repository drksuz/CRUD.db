import sqlite3
import funcao_conexao
import funcao_selectCliente



def alterarDados():
    funcao_conexao.conectar()
    print("------------------- Alteração de Dados -------------------")
    global cpfPesquisar
    cpfPesquisar = funcao_selectCliente.consultarCliente()
    #print("CPF Pesquisar")
    if(cpfPesquisar != []):
        print("-------------------------------------------------")
        dado_update = input("O que deseja alterar?\nNome\nSobrenome\nIdade\nTelefone\nEndereco\nCidade\nEstado\n").lower()
        atualizacao(dado_update)

def atualizacao (dado_update):  
    funcao_conexao.conectar()
    if dado_update == 'nome':
        novo_nome = input("Novo Nome: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET nome = '"+novo_nome+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Nome alterado com sucesso !!")
        funcao_conexao.conn.commit()
    elif dado_update == 'sobrenome':
        novo_sobrenome = input("Novo Sobrenome: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET sobrenome = '"+novo_sobrenome+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Sobrenome alterado com sucesso !!")
        funcao_conexao.conn.commit()
    elif dado_update == 'idade':
        nova_idade = input("Nova Idade: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET idade = '"+nova_idade+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Idade alterada com sucesso !!")
        funcao_conexao.conn.commit()
    elif dado_update == 'telefone':
        novo_telefone = input("Novo Telefone: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET telefone = '"+novo_telefone+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Telefone alterado com sucesso !!")
        funcao_conexao.conn.commit()
    elif dado_update == 'endereco':
        novo_endereco = input("Novo Endereço: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET endereco = '"+novo_endereco+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Endereço alterado com sucesso !!")
        funcao_conexao.conn.commit()
    elif dado_update == 'cidade':
        nova_cidade = input("Nova Cidade: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET cidade = '"+nova_cidade+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Cidade alterado com sucesso !!")
        funcao_conexao.conn.commit()
    elif dado_update == 'estado':
        novo_estado = input("Novo Estado: ")
        funcao_conexao.cursor.execute("UPDATE cliente SET estado = '"+novo_estado+"' WHERE cpf = ?",(cpfPesquisar,))
        print("Telefone alterado com sucesso !!")
        funcao_conexao.conn.commit()
    else:
        print("Não deu! ;( ")
    funcao_conexao.conn.close()