painel = print ("---------------PAINEL BANCO DE DADOS---------------")

inserirl = input("Insira 1:Criar / 2:Inserir / 3:Deletar / 4:Atualizar: ")

if painel==1:
    import Funcao_CriarBanco
    Funcao_CriarBanco.criar()

elif painel==2:
    import Funcao_Inserindo_Dados_Por_Variável
    Funcao_Inserindo_Dados_Por_Variável.inserirbd()

elif painel==3:
    import Funcao_Deletar_Dados
    Funcao_Deletar_Dados.deletarb()

elif painel==4:
    import Funcao_Atualizar_Dados
    Funcao_Atualizar_Dados.attdados()

else:
    StopIteration