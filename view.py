from model import *
def main():
    print()

if __name__ == "__main__":
    menu_inicial()
    escolha = int(input("Escolha uma opção:\n 1 - Cadastrar\n2 - Listar\n3 - Sair: "))
    

    match escolha:
        case 1:
            nome = input("Digite seu nome\n")
        case _:
            print("opcao invalida")
