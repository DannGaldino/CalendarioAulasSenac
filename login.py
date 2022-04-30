import this
import calendario
import cadastrarProfessor

this.email = ""
this.senha = 0
this.opcao = 0
def loginFuncionario():
    print('Informe o email: ')
    this.email = (input())

    print('Informe a senha: ')
    this.senha = input()


def mostrar():
    cadastrarProfessor
    loginFuncionario()
    print("Conectado com sucesso")

    calendario.coletar()