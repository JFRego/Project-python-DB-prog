import os
import insert
import change
import delete
import list

def mainmenu():
    opcs = {
        '1': 'client_menu()',
        '2': 'prod_menu()',
        '3': 'trans_menu()',
        '4': 'order_menu()',
        '5': 'report_menu()',
        '0': 'print("Bye, Bye!")'
    }

    while True:
        os.system('clear')
        print('MENU PRINCIPAL')
        print()
        print('1 - Clientes')
        print('2 - Produtos')
        print('3 - Trasportes')
        print('4 - Encomendas')
        print('5 - Relatórios')
        print('0 - Sair')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 5:
                os.system('clear')
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def client_menu():
    opcs = {
        '1': 'insert.insert("dados/clientes.csv", 0)',
        '2': 'change.change("dados/clientes.csv", 0)',
        '3': 'delete.delete("dados/clientes.csv", 0)',
        '4': 'list.listing("dados/clientes.csv")',
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Clientes')
        print()
        print('1 - Inserir cliente')
        print('2 - Modificar cliente')
        print('3 - Eliminar cliente')
        print('4 - Listar clientes')
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 4:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def prod_menu():
    opcs = {
        '1': 'insert.insert("dados/produtos.csv", 1)',
        '2': 'change.change("dados/produtos.csv", 1)',
        '3': 'delete.delete("dados/produtos.csv", 1)',
        '4': 'list.listing("dados/produtos.csv")',
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Produtos')
        print()
        print('1 - Inserir produto')
        print('2 - Modificar produto')
        print('3 - Eliminar produto')
        print('4 - Listar produtos')
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 4:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def trans_menu():
    opcs = {
        '1': 'insert.insert("dados/transportes.csv", 2)',
        '2': 'change.change("dados/transportes.csv", 2)',
        '3': 'delete.delete("dados/transportes.csv", 2)',
        '4': 'list.listing("dados/transportes.csv")',
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Transportes')
        print()
        print('1 - Inserir transportadora')
        print('2 - Modificar transportadora')
        print('3 - Eliminar transportadora')
        print('4 - Listar transportadoras')
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 4:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def order_menu():
    opcs = {
        '1': 'orders_menu()',
        '2': 'orders_det_menu()',
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Encomendas')
        print()
        print('1 - Manter Encomenda')
        print('2 - Manter detalhe da encomenda')
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 2:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def orders_menu():
    opcs = {
        '1': 'insert.insert("dados/encomendas.csv", 3)',
        '2': 'change.change("dados/encomendas.csv", 3)',
        '3': 'delete.delete("dados/encomendas.csv", 3)',
        '4': 'list.listing("dados/encomendas.csv")',
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Manter Encomendas')
        print()
        print('1 - Inserir encomenda')
        print('2 - Modificar encomenda')
        print('3 - Eliminar encomenda')
        print('4 - Listar encomendas')
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 4:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def orders_det_menu():
    opcs = {
        '1': 'insert.insert("dados/det_enc.csv", 4)',
        '2': 'change.changedet("dados/det_enc.csv", 4)',
        '3': 'delete.deletedet("dados/det_enc.csv", 4)',
        '4': 'list.listing("dados/det_enc.csv")',
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Detalhes Encomendas')
        print()
        print('1 - Inserir detalhe encomenda')
        print('2 - Modificar detalhe encomenda')
        print('3 - Eliminar detalhe encomenda')
        print('4 - Listar encomendas')
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 4:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break

def report_menu():
    opcs = {
        '0': 'print()'
    }

    while True:
        os.system('clear')
        print('MENU Relatorios')
        print()
        print('0 - Voltar')
        while True:
            opc = int(input('Insira o nº correspondente ao q deseja fazer:'))
            if 0 <= opc <= 4:
                eval(opcs.get(str(opc)))
                break
        if opc == 0:
            break