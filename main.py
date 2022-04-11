import csv


def verificaEntrada(ent, ent2):
    if ent == "leia":
        if ent2 == "CIC20211.csv" or ent2 == "ENE20211.csv" or ent2 == "MAT20211.csv" or ent2 == "ENM20211.csv":
            return 0
    if ent == "carga" or ent == "matriculas":
        return 0
    if ent == "disciplina":
        try:
            int(ent2)
            return 0
        except ValueError:
            return 1
    return 1


if __name__ == '__main__':

    try:
        acao, acionado = input().split(" ", 1)
    except ValueError:
        acao, acionado = "FIM", ""

    while acao != "FIM":
        if verificaEntrada(acao, acionado):
            print("erro")
        else:
            print("certo")

        try:
            acao, acionado = input().split(" ", 1)
        except ValueError:
            break
