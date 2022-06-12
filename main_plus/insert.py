import os

tit = [
    ['IDCLIENTE', 'NOME', 'MORADA', 'CPOSTAL', 'LOCALIDADE', 'TELEFONE'],
    ['IDPRODUTO', 'NOME', 'CUSTO', 'STOCK', 'ENCOMENDAS', 'MINIMO'],
    ['IDTRANSPORTE', 'NOME'],
    ['IDEncomenda', 'IDCliente', 'Data', 'IDTransporte'],
    ['IDEncomenda', 'IDProduto', 'Quantidade', 'Preco']
]

tip = [
    ['nome do cliente', 'morada do cliente', 'codigo postal do cliente', 'localidade do cliente', 'telefone do cliente'],
    ['nome do produto', 'custo do produto', 'stock do produto', 'nº de encomendas do produto', 'minimo de stock + encomendas do produto'],
    ['nome da transportadora'],
    ['ID do cliente', 'data', 'ID da transportadora'],
    ['ID da encomenda', 'ID do produto', 'quantidade']
]

names = ['Clientes', 'Produtos', 'Transportadoras', 'Encomendas', 'Detalhes de encomenda']

def insert(inpt, tits):
    while True:
        if int(tits) != 4:
            cliline = []
            M = 0
            with open(inpt) as file:
                for num, line in enumerate(file, 1):
                    if num > 1:
                        cliline = line.rstrip().split(',')
                        if int(str(cliline[0].replace('"', ''))) > int(M):
                            M = int(str(cliline[0].replace('"', '')))
                if int(len(cliline)) > 0:
                    id = int(M)
                else:
                    id = 0

        cliline = []
        if int(tits) != 4:
            id += 1
            cliline.append(id)
            os.system('clear')
            for x in range(len(tip[tits])):
                cliline.append(str(input(f'Inserir {tip[tits][x]}:').replace(',', '.')))
        else:
            os.system('clear')
            for x in range(len(tip[tits])):
                if int(x) < 2:
                    cliline.append(input(f'Inserir {tip[tits][x]}:'))
                else:
                    with open('dados/produtos.csv') as file:
                        for num, line in enumerate(file, 1):
                            if num > 1:
                                proline = line.rstrip().split(',')
                                if int(cliline[1]) == int(str(proline[0].replace('"', ''))):
                                    qmax = int(str(proline[3].replace('"', ''))) + int(str(proline[4].replace('"', '')))
                                    price = float(str(proline[2].replace('"', '')))
                    while True:
                        y = input(f'Inserir {tip[tits][x]}')
                        if int(y) <= int(qmax):
                            cliline.append(y)
                            break
                        else:
                            print(f'ERROR! Quantidade maxima deste produto existente em stock e em encomenda é {qmax}')
                            input(f'Altere valor de quantidade. [ENTER]')
                    cliline.append(int(y)*float(price))

        savecli = []
        with open(inpt) as file:
            for num, line in enumerate(file, 1):
                if num > 1:
                    savecli.append(line.rstrip().split(','))

        with open(inpt, 'w') as file:
            tmp = ''
            for x in range(len(tit[tits])):
                if int(x) == 0:
                    tmp = '"' + str(tit[tits][x]) + '"'
                else:
                    tmp += ',"' + str(tit[tits][x]) + '"'
            file.write(tmp + '\n')

        with open(inpt, 'a') as file:
            for x in range(len(savecli)):
                tmp = ''
                for y in range(len(savecli[x])):
                    if int(y) == 0:
                        tmp = savecli[x][y]
                    else:
                        tmp += ',' + savecli[x][y]
                file.write(tmp + '\n')
            tmp = ''
            for x in range(len(cliline)):
                if int(x) == 0:
                    tmp = '"' + str(cliline[x]) + '"'
                else:
                    tmp += ',"' + str(cliline[x]) + '"'
            file.write(tmp + '\n')

        if input(f'Deseja inserir mais {names[tits]}? (s/n)') == 'n':
            break