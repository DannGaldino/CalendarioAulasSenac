import this
import calendario
import cadastrarProfessor
import conexao
import menu

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.email = ""
this.senha = ""
this.user = ""


def loginProfessor():
    print("Informe o seu email: ")
    this.email = input()
    print("Informe a sua senha: ")
    this.senha = input()

    msg = "Acesso negado! Preencha os campos corretamente."

    try:
        sql = "select senha from Professor where email = '{}';".format(this.email)
        con.execute(sql)#Prepara o comando para ser executado

        for (senha) in con:

            if this.senha == senha[0]:
                print("Acesso Liberado")
                menu.menu2()

    except Exception as erro:
      print(erro)

    print(msg)

def loginAdm():
    print("Informe o usuário: ")
    this.user = input()
    print("Informe a sua senha: ")
    this.senha = input()

    msg = "Acesso negado! Preencha os campos corretamente."

    try:
        sql = "select senha from Administrador where usuario = '{}';".format(this.user)
        con.execute(sql)#Prepara o comando para ser executado

        for (senha) in con:
            se = senha[0]
            if this.senha == se:
                print("Acesso Liberado")
                cadastrarProfessor.coletarDados()

    except Exception as erro:
      print(erro)

    print(msg)
