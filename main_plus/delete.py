
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

def delete(inpt, tits):
    while True:
        id = int(input(f'Insira {tit[tits][0]} que deseja modificar:'))
        savecli = []
        with open(inpt) as file:
            for num, line in enumerate(file, 1):
                if num > 1:
                    chcliline = line.rstrip().split(',')
                    if int(id) != int(chcliline[0].replace('"', '')):
                        savecli.append(chcliline)

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

        if input(f'Deseja eliminar mais {names[tits]}? (s/n)') == 'n':
            break

def deletedet(inpt, tits):
    while True:
        id1 = int(input(f'Insira {tit[tits][0]} que deseja modificar:'))
        id2 = int(input(f'Insira {tit[tits][1]} que deseja modificar:'))

        with open('dados/encomendas.csv') as file:
            ctrl = 0
            for num, line in enumerate(file, 1):
                if num > 1:
                    controlline = line.rstrip().split(',')
                    if int(id1) == int(controlline[0].replace('"', '')):
                        ctrl += 1
                    else:
                        ctrl += 0

        if int(ctrl) == 0:
            savecli = []
            with open(inpt) as file:
                for num, line in enumerate(file, 1):
                    if num > 1:
                        chcliline = line.rstrip().split(',')
                        if int(id1) != int(chcliline[0].replace('"', '')) or int(id2) != int(
                                chcliline[1].replace('"', '')):
                            savecli.append(chcliline)

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

            if input(f'Deseja eliminar mais {names[tits]}? (s/n)') == 'n':
                break

        else:
            print('ERROR! Nao é possivel eliminar este registo pois a encomenda encontra se em vias de ser entregue ao cliente')
            input('Voltar: [ENTER]')
            break