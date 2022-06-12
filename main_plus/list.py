
def listing(inpt):
    with open(inpt) as file:
        for num, line in enumerate(file, 0):
            lines = line.rstrip().split(',')
            tmp = ''
            for x in range(len(lines)):
                if int(x) == 0:
                    tmp = "{:<20}".format(lines[x].replace('"', ''))
                else:
                    tmp += "{:<20}".format(lines[x].replace('"', ''))
            print(tmp)
            print()
    input('Voltar: [ENTER]')