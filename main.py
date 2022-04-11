import csv


def trataArquivo(ent):
    if ent == "CIC20211.csv" or ent == "ENE20211.csv" or ent == "MAT20211.csv" or ent == "ENM20211.csv":
        return 1
    return 0


if __name__ == '__main__':

    entrada = input().split(" ", 1)
    soma = 0
    alunos = 0

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
                    if entrada[1] in oferta[4]:
                        print(f"* {oferta[1]} ({oferta[0]})")
                        horas = oferta[4].split('(')
                        horas = horas[1].split(')')
                        print(f"\tTurma {oferta[2]}: {horas[0]} ({oferta[-2]} alunos)")
                        if int(oferta[-2]) > 5:
                            soma += int((horas[0])[0:2])
                            alunos += int(oferta[-2])
                print(f"[Carga total considerada: {soma}h ({soma/alunos:.2f}/aluno)]")
            except NameError:
                print(f"No hay {entrada[1]}")
                break

        entrada = input().split(" ", 1)

    try:
        csvfile.close()
        print("Arquivo fechado")
    except NameError:
        pass
