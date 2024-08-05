def inserirbd(nome,idade,email):
    import sqlite3

    nome = "darick"

    idade = 12

    email = "dede@gmail.com"

    banco = sqlite3.connect('primeiro_banco.db') #criação do objeto (BANCO) com o método connect

    cursor = banco.cursor() #criando outro objeto que recebe o objeto banco junto ao metodo


    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"')") #inserindo os dados

    banco.commit()
