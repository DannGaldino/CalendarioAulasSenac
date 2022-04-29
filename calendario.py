import this


def meses():
    this.janeiro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.fevereiro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.marco = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.abril = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.maio = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.junho = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.julho = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.agosto = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.setembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.outubro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.novembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.dezembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def coletar():
    print("Informe o mês")
    mes = int(input())
    print("Informe o dia")
    dia = int(input())
    print("Informe o nome do professor")
    professor = str(input())
    inserir(mes, dia, professor)


def inserir(mes, dia, professor):
    meses()
    if mes == 1:
        this.janeiro.pop((dia - 1))
        this.janeiro.insert((dia - 1), str(professor))
        print(this.janeiro)
    elif mes == 2:
        this.fevereiro.pop((dia - 1))
        this.fevereiro.insert((dia - 1), str(professor))
        print(this.fevereiro)
    elif mes == 3:
        this.marco.pop((dia - 1))
        this.marco.insert((dia - 1), str(professor))
        print(this.marco)
    elif mes == 4:
        this.abril.pop((dia - 1))
        this.abril.insert((dia - 1), str(professor))
        print(this.abril)
    elif mes == 5:
        this.maio.pop((dia - 1))
        this.maio.insert((dia - 1), str(professor))
        print(this.maio)
    elif mes == 6:
        this.junho.pop((dia - 1))
        this.junho.insert((dia - 1), str(professor))
        print(this.junho)
    elif mes == 7:
        this.julho.pop((dia - 1))
        this.julho.insert((dia - 1), str(professor))
        print(this.julho)
    elif mes == 8:
        this.agosto.pop((dia - 1))
        this.agosto.insert((dia - 1), str(professor))
        print(this.agosto)
    elif mes == 9:
        this.setembro.pop((dia - 1))
        this.setembro.insert((dia - 1), str(professor))
        print(this.setembro)
    elif mes == 10:
        this.outubro.pop((dia - 1))
        this.outubro.insert((dia - 1), str(professor))
        print(this.outubro)
    elif mes == 11:
        this.novembro.pop((dia - 1))
        this.novembro.insert((dia - 1), str(professor))
        print(this.novembro)
    elif mes == 12:
        this.dezembro.pop((dia - 1))
        this.dezembro.insert((dia - 1), str(professor))
        print(this.dezembro)
    else:
        print("Opção inválida")
    print(str(dia) + " de " + str(mes) + ": " + str(professor))


def consultar():
    meses()
    print("Consultar professor por data")
    print("Informe o mês")
    mes = int(input())
    print("Informe o dia")
    dia = int(input())
    if mes == 1:
        print(this.janeiro[dia])
    elif mes == 2:
        print(this.fevereiro[dia])
    elif mes == 3:
        print(this.marco[dia])
    elif mes == 4:
        print(this.abril[dia])
    elif mes == 5:
        print(this.maio[dia])
    elif mes == 6:
        print(this.junho[dia])
    elif mes == 7:
        print(this.julho[dia])
    elif mes == 8:
        print(this.agosto[dia])
    elif mes == 9:
        print(this.setembro[dia])
    elif mes == 10:
        print(this.outubro[dia])
    elif mes == 11:
        print(this.novembro[dia])
    elif mes == 12:
        print(this.dezembro[dia])
    else:
        print("Opção inválida")
