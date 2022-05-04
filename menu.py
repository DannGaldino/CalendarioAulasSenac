import coletarProfessores
import loginProfessor
import this
import calendario

this.opcao = -2


def mostrarMenu():
    print('Escolha uma das opçôes abaixo: ' +
          '\n\n\n1. Coletar Dados do(a) professor(a)' +
          '\n2. Calendário' +
          '\n3. Login' +
          '\n4. Sair')

    this.opcao = int(input())

def operacoes():
    while this.opcao != 4:
        mostrarMenu()
        if this.opcao == 1:
            print(coletarProfessores.mostrarDados())
        elif this.opcao == 2:
            print(calendario.consultar())
        elif this.opcao == 3:
            print(loginProfessor.mostrar())
        else:
            print('Opção inválida! Tente novamente')
