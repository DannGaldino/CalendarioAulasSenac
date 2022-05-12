import this
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.data = ""
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

def convertDate(texto):
    separate = texto.split('/')
    day = separate[0]
    month = separate[1]
    year = separate[2]
    return '{}-{}-{}'.format(year, month, day)


def coletar():
    print("Agendar Aula")
    print("Informe a data da aula: (dia/mês/ano)")
    this.data = input()

    print("Informe o turno: (Manhã, tarde ou noite)")
    this.turno = input()

    print("Informe a matéria: ")
    this.materia = input()

    print("Informe o nome do professor: ")
    this.professor = input()

    codigo = (convertDate(this.data) + this.turno)

    separado = this.data.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]



    inserir(codigo, dia, mes, ano, this.turno, this.materia, this.professor)


def inserir(codigo, dia, mes, ano, turno, materia, professor):
    try:
        sql = "insert into calendario(codigo, dia, mes, ano, turno, materia, professor) values('{}','{}','{}','{}','{}','{}','{}')".format(codigo, dia, mes, ano, turno, materia, professor)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()  # Executa o comando no banco de dados
        print("Aula agendada!")
    except Exception as erro:
      print(erro)


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