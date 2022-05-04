import this

this.mes = 0
this.dia = 0
this.professor = 0

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
    this.mes = int(input())
    print("Informe o dia")
    this.dia = int(input())
    print("Informe o nome do professor")
    this.professor = str(input())
    inserir(this.mes, this.dia, this.professor)


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
    print("Consultar professor por data")
    print("Informe o mês:")
    mes = int(input())
    print("Informe o dia:")
    dia = int(input())
    if mes == 1:
        print("entrei")
        print(this.janeiro[(dia - 1)])
    elif mes == 2:
        print(this.fevereiro[(dia - 1)])
    elif mes == 3:
        print(this.marco[(dia - 1)])
    elif mes == 4:
        print(this.abril[(dia - 1)])
    elif mes == 5:
        print(this.maio[(dia - 1)])
    elif mes == 6:
        print(this.junho[(dia - 1)])
    elif mes == 7:
        print(this.julho[(dia - 1)])
    elif mes == 8:
        print(this.agosto[(dia - 1)])
    elif mes == 9:
        print(this.setembro[(dia - 1)])
    elif mes == 10:
        print(this.outubro[(dia - 1)])
    elif mes == 11:
        print(this.novembro[(dia - 1)])
    elif mes == 12:
        print(this.dezembro[(dia - 1)])
    else:
        print("Opção inválida")