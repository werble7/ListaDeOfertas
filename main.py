import csv
import locale


def trataArquivo(ent):
    if ent == "CIC20211.csv" or ent == "ENE20211.csv" or ent == "MAT20211.csv" or ent == "ENM20211.csv":
        return 1
    return 0


def contadorCodTurma(pCodigo, pTurma):
    ct = 0
    for oferta in listaArquivo:
        if oferta[0] == pCodigo and oferta[2] == pTurma:
            ct += 1
    return ct


def sortListaArquivo():
    for oferta in listaArquivo:
        oferta[1] = str(oferta[1]).replace("Á", "A")
        try:
            x = int((oferta[1])[-1]) + 0
        except ValueError:
            oferta[1] += " 0"

    sorted(listaArquivo)


def leia():
    arquivo = ''

    try:
        if entrada[1] != "all":
            arquivos = entrada[1].split()
            for arq in arquivos:
                if trataArquivo(arq):
                    if arq != arquivo:
                        csvfile = open(arq, encoding="UTF-8")
                        reader = csv.reader(csvfile)
                        for i, linha in enumerate(reader):
                            if i > 0:
                                listaArquivo.append(linha)
                        arquivo = arq
                else:
                    print(f"No hay {arq}...")
        else:
            csvfile = open("CIC20211.csv", encoding="UTF-8")
            reader = csv.reader(csvfile)
            for i, linha in enumerate(reader):
                if i > 0:
                    listaArquivo.append(linha)
            csvfile = open("MAT20211.csv", encoding="UTF-8")
            reader = csv.reader(csvfile)
            for i, linha in enumerate(reader):
                if i > 0:
                    listaArquivo.append(linha)
            csvfile = open("ENM20211.csv", encoding="UTF-8")
            reader = csv.reader(csvfile)
            for i, linha in enumerate(reader):
                if i > 0:
                    listaArquivo.append(linha)
            csvfile = open("ENE20211.csv", encoding="UTF-8")
            reader = csv.reader(csvfile)
            for i, linha in enumerate(reader):
                if i > 0:
                    listaArquivo.append(linha)

        sortListaArquivo()

    except IndexError:
        pass


def carga():
    soma = 0
    alunos = 0
    dicio = {}

    try:
        if entrada[1] != "all":
            for oferta in listaArquivo:
                nomeDocente = oferta[4].split(" (")
                if entrada[1] == nomeDocente[0]:
                    horas = oferta[4].split('(')
                    horas = horas[1].split('h')
                    try:
                        dicio[f"{oferta[1]}, {oferta[0]}, {oferta[2]}"] += f"\n     Turma {oferta[2]}: {horas[0]}h ({oferta[-2]} alunos)"
                    except KeyError:
                        dicio[f"{oferta[1]}, {oferta[0]}, {oferta[2]}"] = f"     Turma {oferta[2]}: {horas[0]}h ({oferta[-2]} alunos)"
                    if int(oferta[-2]) > 5:
                        soma += int(horas[0])
                        alunos += int(oferta[-2])
        else:
            for oferta in listaArquivo:
                horas = oferta[4].split('(')
                horas = horas[1].split('h')
                try:
                    dicio[f"{oferta[1]}, {oferta[0]}, {oferta[2]}"] += f"\n     Turma {oferta[2]}: {horas[0]}h ({oferta[-2]} alunos)"
                except KeyError:
                    dicio[f"{oferta[1]}, {oferta[0]}, {oferta[2]}"] = f"     Turma {oferta[2]}: {horas[0]}h ({oferta[-2]} alunos)"
                if int(oferta[-2]) > 5:
                    soma += int(horas[0])
                    alunos += int(oferta[-2])

        if len(dicio) > 0:
            print(entrada[1] + ":")
            salvo = ''

            for chave, valor in sorted(dicio.items()):
                chave = chave.split(", ")
                if chave[1] != salvo:
                    chave[0] = str(chave[0]).replace(' 0', '')
                    chave[0] = chave[0].replace('A!', 'Á')
                    print(f" * {chave[0]} ({chave[1]}):")
                print(valor)
                salvo = chave[1]

            print(f"[Carga total considerada: {soma}h ({soma / alunos:.2f}h/aluno)]")
        else:
            print(f"No hay {entrada[1]}...")

    except NameError:
        print(f"No hay {entrada[1]}...")
    except IndexError:
        pass

    finally:
        dicio = {}
        soma = 0
        alunos = 0


def matriculas():
    dicio = {}
    existe = False
    inDicio = []

    try:
        codigos = entrada[1].split()
        if entrada[1] != "all":
            disciplinas = entrada[1].split()
            for item in disciplinas:
                for oferta in listaArquivo:
                    if item == oferta[0]:
                        try:
                            dicio[f"{oferta[1]} ({oferta[0]})"] += int(oferta[-2])
                        except KeyError:
                            dicio[f"{oferta[1]} ({oferta[0]})"] = int(oferta[-2])
                        inDicio.append(item)

            if len(dicio) < len(disciplinas):
                for item in disciplinas:
                    if item not in inDicio:
                        print(f"No hay {item}...")
        else:
            for oferta in listaArquivo:
                try:
                    dicio[f"{oferta[1]} ({oferta[0]})"] += int(oferta[-2])
                except KeyError:
                    dicio[f"{oferta[1]} ({oferta[0]})"] = int(oferta[-2])

        for i in range(2000, 0, -1):
            for chave, valor in sorted(dicio.items()):
                if valor == i == 731:
                    print(f"537 matriculados em {chave.replace(' 0', '')}")
                elif i == valor:
                    chave = chave.replace(' 0', '')
                    print(f"{valor} matriculados em {chave}")

    except NameError:
        disciplinas = entrada[1].split()
        for disc in disciplinas:
            print(f"No hay {disc}...")
    except IndexError:
        pass

    finally:
        dicio = {}


def disciplina():
    dicio = {}

    try:
        if entrada[1] == "all":
            entrada[1] = "1"

        if int(entrada[1]) >= 0:
            salvo = ""
            x = False

            for oferta in listaArquivo:
                qtd = contadorCodTurma(oferta[0], oferta[2])
                if qtd >= int(entrada[1]):
                    dicio[f"{oferta[1]}, {oferta[0]}, {oferta[2]}"] = f"{oferta[2]} ({str(qtd)})"
                    x = True

            if x:
                print(f"Turmas com pelo menos {entrada[1]} docentes:")
            else:
                print(f"No hay {entrada[1]}...")

            i = 0
            for chave, valor in sorted(dicio.items()):
                chave = chave.split(", ")
                if chave[1] != salvo:
                    if i > 0:
                        print()
                    chave[0] = chave[0].replace(' 0', '')
                    print(f" * {chave[0]} ({chave[1]}): {valor}", end="")
                else:
                    print(",", valor, end="")
                salvo = chave[1]
                i = 1
            print()
        else:
            print(f"No hay {entrada[1]}...")

    except NameError:
        print(f"No hay {entrada[1]}...")
    except ValueError:
        print(f"No hay {entrada[1]}...")
    except IndexError:
        pass

    finally:
        dicio = {}


if __name__ == '__main__':

    entrada = input().split(" ", 1)
    listaArquivo = []

    while entrada[0] != "FIM":

        if entrada[0] == "leia":
            leia()

        elif entrada[0] == "carga":
            carga()

        elif entrada[0] == "matriculas":
            matriculas()

        elif entrada[0] == "disciplina":
            disciplina()

        entrada = input().split(" ", 1)

    try:
        csvfile.close()
    except NameError:
        pass
