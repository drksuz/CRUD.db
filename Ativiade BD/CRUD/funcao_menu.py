def menu():
    print("------------------------- MENU LOJA EXCELFORM'S -------------------------")
    print("Seja bem vindo ao nosso cadastro de clientes, o que deseja fazer?")
    print("Insira abaixo:")
    print("1:Cadastrar Cliente | \n2:Exibir Clientes | \n3:Consultar Cliente pelo CPF | \n4:Alterar Dados Cadastrais | \n5:Excluir Cliente | \n6:Sair | ")
    global painel 
    painel = input()
    return painel