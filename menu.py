import cadastrarProfessor
import login
import this
import calendario

this.opcao = -2


def mostrarMenu():
    print('Escolha uma das opçôes abaixo: ' +
          '\n\n\n1. Cadastrar Professor' +
          '\n2. Calendário' +
          '\n3. Login' +
          '\n4. Sair')

    this.opcao = int(input())

def operacoes():
    while this.opcao != 4:
        mostrarMenu()
        if this.opcao == 1:
            cadastrarProfessor.coletarDados()
        elif this.opcao == 2:
            calendario.consultar()
        elif this.opcao == 3:
            login.loginProfessor()
        else:
            print('Opção inválida! Tente novamente')
