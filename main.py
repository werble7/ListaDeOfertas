import csv


def trataArquivo(ent):
    if ent == "CIC20211.csv" or ent == "ENE20211.csv" or ent == "MAT20211.csv" or ent == "ENM20211.csv":
        return 1
    return 0


if __name__ == '__main__':

    entrada = input().split(" ", 1)
    soma = 0
    alunos = 0
    listaArquivo = []
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

                for oferta in reader:
                    listaArquivo.append(oferta)

                for oferta in listaArquivo:
                    if entrada[1] in oferta[4]:
                        horas = oferta[4].split('(')
                        horas = horas[1].split(')')
                        try:
                            dicio[f"* {oferta[1]} ({oferta[0]})"] += f"\n\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)"
                        except KeyError:
                            dicio[f"* {oferta[1]} ({oferta[0]})"] = f"\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)"
                        if int(oferta[-2]) > 5:
                            soma += int((horas[0])[0:2])
                            alunos += int(oferta[-2])

                for chave, valor in sorted(dicio.items()):
                    print(chave)
                    print(valor)

                print(f"[Carga total considerada: {soma}h ({soma/alunos:.2f}/aluno)]")

            except NameError:
                print(f"No hay {entrada[1]}")
                break
            finally:
                dicio = {}
                listaArquivo = []

        if entrada[0] == "matriculas":

            codigos = entrada[1].split()
            existe = False

            try:
                csvfile = open(arquivo, encoding="UTF-8")
                reader = csv.reader(csvfile)

                for oferta in reader:
                    listaArquivo.append(oferta)

                disciplinas = entrada[1].split()
                for item in disciplinas:
                    for oferta in listaArquivo:
                        if item == oferta[0]:
                            try:
                                dicio[f"{oferta[1]} ({oferta[0]})"] += int(oferta[-2])
                            except KeyError:
                                dicio[f"{oferta[1]} ({oferta[0]})"] = int(oferta[-2])

                for i in range(1000, 0, -1):
                    for chave, valor in sorted(dicio.items()):
                        if i == valor:
                            print(f"{valor} matriculados em {chave}")

            except NameError:
                print(f"No hay {entrada[1]}")
                break
            finally:
                dicio = {}
                listaArquivo = []

        if entrada[0] == "disciplina":

            try:
                csvfile = open(arquivo, encoding="UTF-8")
                reader = csv.reader(csvfile)

                for oferta in reader:
                    listaArquivo.append(oferta)

            except NameError:
                print(f"No hay {entrada[1]}")

        entrada = input().split(" ", 1)

    try:
        csvfile.close()
        print("Arquivo fechado")
    except NameError:
        pass
