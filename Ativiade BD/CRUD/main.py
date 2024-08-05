import sqlite3
from funcao_menu import menu
import funcao_update
import funcao_criar_tabela
import funcao_cadastrar_cliente
import funcao_selectCliente
import funcao_delete

#Criando a tabela Cliente
funcao_criar_tabela.criar()

painel = menu()
while (painel !='6'):

    if(painel == '1'):
        funcao_cadastrar_cliente.cadastrarCliente()
    elif(painel == '2'):
        funcao_selectCliente.exibirCliente()
    elif(painel == '3'):
        funcao_selectCliente.consultarCliente()
    elif(painel == '4'):
        funcao_update.alterarDados()
    elif(painel == '5'):
        funcao_delete.deletarb()
    painel = menu()
