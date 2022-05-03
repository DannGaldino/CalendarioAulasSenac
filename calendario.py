import this
import login

this.opcao = 0

def mostrarMenu():
    print("     Menu     ")
    print("Escolha uma das opções abaixo:")
    print("1. Consultar data")
    print("2. Login")
    print("3. Sair")
    this.opcao = int(input())


def menu():
    meses()
    while this.opcao != 3:
        mostrarMenu()
        if this.opcao == 1:
            consultar()
        elif this.opcao == 2:
            login.mostrar()
        elif this.opcao == 3:
            print("")
        else:
            print("Opção Escolhida Inválida, tente outro número!")


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
    if mes == 1:
        if this.janeiro[(dia - 1)] == "":
            this.janeiro.pop((dia - 1))
            this.janeiro.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de janeiro: " + (this.janeiro[(dia - 1)]))
    elif mes == 2:
        if this.fevereiro[(dia - 1)] == "":
            this.fevereiro.pop((dia - 1))
            this.fevereiro.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de fevereiro: " + (this.fevereiro[(dia - 1)]))
    elif mes == 3:
        if this.marco[(dia - 1)] == "":
            this.marco.pop((dia - 1))
            this.marco.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de marco: " + (this.marco[(dia - 1)]))
    elif mes == 4:
        if this.abril[(dia - 1)] == "":
            this.abril.pop((dia - 1))
            this.abril.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de abril: " + (this.abril[(dia - 1)]))
    elif mes == 5:
        if this.maio[(dia - 1)] == "":
            this.maio.pop((dia - 1))
            this.maio.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de maio: " + (this.maio[(dia - 1)]))
    elif mes == 6:
        if this.junho[(dia - 1)] == "":
            this.junho.pop((dia - 1))
            this.junho.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de junho: " + (this.junho[(dia - 1)]))
    elif mes == 7:
        if this.julho[(dia - 1)] == "":
            this.julho.pop((dia - 1))
            this.julho.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de julho: " + (this.julho[(dia - 1)]))
    elif mes == 8:
        if this.agosto[(dia - 1)] == "":
            this.agosto.pop((dia - 1))
            this.agosto.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de agosto: " + (this.agosto[(dia - 1)]))
    elif mes == 9:
        if this.setembro[(dia - 1)] == "":
            this.setembro.pop((dia - 1))
            this.setembro.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de setembro: " + (this.setembro[(dia - 1)]))
    elif mes == 10:
        if this.outubro[(dia - 1)] == "":
            this.outubro.pop((dia - 1))
            this.outubro.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de outubro: " + (this.outubro[(dia - 1)]))
    elif mes == 11:
        if this.novembro[(dia - 1)] == "":
            this.novembro.pop((dia - 1))
            this.novembro.insert((dia - 1), str(professor))
        else:
            print("Dia de aula já preenchido!")
            print(str(dia) + " de novembro: " + (this.novembro[(dia - 1)]))
    elif mes == 12:
        this.dezembro.pop((dia - 1))
        this.dezembro.insert((dia - 1), str(professor))
    else:
        print("Opção inválida")


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
