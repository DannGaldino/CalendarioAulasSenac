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
    mes = input()
    print("Informe o dia")
    dia = input()
    print("Informe o nome do professor")
    professor = input()
    inserir(mes, dia, professor)

def inserir(mes,dia,professor):
    meses()
    if mes == 1:
        this.janeiro.pop((dia - 1))
        this.janeiro.pop((dia - 1), str(professor))
        print(this.janeiro)
    elif mes == 2:
        this.fevereiro.pop((dia - 1))
        this.fevereiro.pop((dia - 1), str(professor))
    elif mes == 3:
        this.marco.pop((dia - 1))
        this.marco.pop((dia - 1), str(professor))
    elif mes == 4:
        this.abril.pop((dia - 1))
        this.abril.pop((dia - 1), str(professor))
    elif mes == 5:
        this.maio.pop((dia - 1))
        this.maio.pop((dia - 1), str(professor))
    elif mes == 6:
        this.junho.pop((dia - 1))
        this.junho.pop((dia - 1), str(professor))
    elif mes == 7:
        this.julho.pop((dia - 1))
        this.julho.pop((dia - 1), str(professor))
    elif mes == 8:
        this.agosto.pop((dia - 1))
        this.agosto.pop((dia - 1), str(professor))
    elif mes == 9:
        this.setembro.pop((dia - 1))
        this.setembro.pop((dia - 1), str(professor))
    elif mes == 10:
        this.outubro.pop((dia - 1))
        this.outubro.pop((dia - 1), str(professor))
    elif mes == 11:
        this.novembro.pop((dia - 1))
        this.novembro.pop((dia - 1), str(professor))
    elif mes == 12:
        this.dezembro.pop((dia - 1))
        this.dezembro.pop((dia - 1), str(professor))
    else:
        print("Opção inválida")
