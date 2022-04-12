import csv


def trataArquivo(ent):
    if ent == "CIC20211.csv" or ent == "ENE20211.csv" or ent == "MAT20211.csv" or ent == "ENM20211.csv":
        return 1
    return 0


def insereCodigo(pCodigo):
    posicao = achaCodigo(pCodigo)
    if posicao == -1:
        listaOfertas.append([pCodigo, 1])
    else:
        listaOfertas[posicao][1] = int(listaOfertas[posicao][1]) + 1


def achaCodigo(pCodigo):
    for i, x in enumerate(listaOfertas):
        if x[0] == pCodigo:
            return i
    return -1


if __name__ == '__main__':

    entrada = input().split(" ", 1)
    soma = 0
    alunos = 0
    listaOfertas = []
    listaCarga = []
    dicio = {}

    while entrada[0] != "FIM":

        if entrada[0] == "leia":
            if trataArquivo(entrada[1]):
                arquivo = entrada[1]
                csvfile = open(arquivo, encoding="UTF-8")
                reader = csv.reader(csvfile)

        if entrada[0] == "carga":

            try:
                csvfile = open(arquivo, encoding="UTF-8")
                reader = csv.reader(csvfile)

                '''
                for oferta in reader:
                    if entrada[1] in oferta[4]:
                        print(f"* {oferta[1]} ({oferta[0]})")
                        horas = oferta[4].split('(')
                        horas = horas[1].split(')')
                        print(f"\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)")
                        if int(oferta[-2]) > 5:
                            soma += int((horas[0])[0:2])
                            alunos += int(oferta[-2])
                '''
                ''' 
                for i, oferta in enumerate(reader):
                    if i > 0 and entrada[1] in oferta[4]:
                        insereCodigo(oferta[0])

                print(listaOfertas)
                '''
                '''
                for oferta in reader:
                    listaOfertas.append(oferta)

                for oferta in listaOfertas:
                    if entrada[1] in oferta[4]:
                        print(f"* {oferta[1]} ({oferta[0]})")
                        horas = oferta[4].split('(')
                        horas = horas[1].split(')')
                        print(f"\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)")
                        if int(oferta[-2]) > 5:
                            soma += int((horas[0])[0:2])
                            alunos += int(oferta[-2])
                '''

                for oferta in reader:
                    listaOfertas.append(oferta)

                for oferta in listaOfertas:
                    if entrada[1] in oferta[4]:
                        horas = oferta[4].split('(')
                        horas = horas[1].split(')')
                        try:
                            dicio[f"* {oferta[1]} ({oferta[0]})"] += f"\n\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)"
                        except KeyError:
                            dicio[f"* {oferta[1]} ({oferta[0]})"] = f"\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)"

                for chave, valor in sorted(dicio.items()):
                    print(chave)
                    print(valor)

                # print(f"[Carga total considerada: {soma}h ({soma/alunos:.2f}/aluno)]")

            except NameError:
                print(f"No hay {entrada[1]}")
                break

        if entrada[0] == "matriculas":

            codigos = entrada[1].split()
            existe = False

            try:
                csvfile = open(arquivo, encoding="UTF-8")
                reader = csv.reader(csvfile)

                for oferta in reader:
                    listaOfertas.append(oferta)

                for oferta in listaOfertas:
                    print(oferta)

                '''
                for codigo in codigos:

                    for oferta in reader:
                        if codigo == oferta[0]:
                            existe = True

                    if existe:
                        print(codigo)
                        existe = False
                '''

            except NameError:
                print(f"No hay {entrada[1]}")
                break

        # if entrada[0] == "disciplina":

        entrada = input().split(" ", 1)

    try:
        csvfile.close()
        print("Arquivo fechado")
    except NameError:
        pass
