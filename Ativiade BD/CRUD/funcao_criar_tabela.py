import funcao_conexao

#Criando a tabela "Cliente"
funcao_conexao.conectar()
def criar():
    criar_tabela = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, idade integer, cpf integer, telefone integer, endereco string, cidade string, estado string)"
    funcao_conexao.cursor.execute(criar_tabela)