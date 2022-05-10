import this

this.data = 0
this.turno = ""
this.materia = ""
this.professor = ""

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
    print("Agendar Aula")
    print("Informe a data da aula: (dia/mês/ano)")
    this.data = int(input())

    print("Informe o turno: (Manhã, tarde ou noite)")
    this.turno = int(input())
    print("Informe o dia")

    print("Informe a matéria: ")
    this.materia = int(input())

    inserir(this.data, this.turno, this.materia)


def inserir():
    print("bem vindo!")


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