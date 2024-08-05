def attdados():
    import sqlite3

    banco = sqlite3.connect('primeiro_banco.db') #criação do objeto (BANCO) com o método connect

    cursor = banco.cursor() #criando outro objeto que recebe o objeto banco junto ao metodo

    cursor.execute("UPDATE pessoas SET nome = 'joao' WHERE idade = 38") #troca o nome da pessoa que tenha a idade declarada na condição WHERE

    banco.commit()