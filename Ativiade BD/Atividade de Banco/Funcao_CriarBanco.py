def criar():
    import sqlite3
    
    banco = sqlite3.connect('') #criação do objeto (BANCO) com o método connect

    cursor = banco.cursor() #criando outro objeto que recebe o objeto banco junto ao metodo


    cursor.execute("INSERT INTO pessoas VALUES('Darick',13,'darick_souza3@gmail.com')") #inserindo os dados

    banco.commit()