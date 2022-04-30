import this


this. email = 0
this.senha = 0
def coletarDados():
    this.email = []
    this.senha = []

    print('Informe o e-mail do professor: ')
    this.email = input()

    print('informe a senha de login do(a) professor(a)')
    this.senha = input()

def  mostrarDados():
    coletarDados()
    print(f'\n\n\n E-mail: {this.email}.\n Senha: {this.senha}')

    print('Cadastrado com sucesso!!')