from typing import List, Dict
from time import sleep
from pathlib import Path

from functions.helpers import Friend


def main() -> None:
    menu()


def menu() -> None:
    print('~~~~~~~~~~~~~~ Bem vindo(a) a NOX ~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~ LISTA VIP ~~~~~~~~~~~~~~~~~~\n\n')
    print('Selecione uma das opções abaixo:\n')
    print('1- Adicionar\n2- Exibir\n3- Listar\n4- Alterar\n5- Remover\n6- Encerrar lista')

    option: int = int(input())

    if option == 1:
        add_friend()
    elif option == 2:
        exhibt_friend()
    elif option == 3:
        list_vip()
    elif option == 4:
        change_friend()
    elif option == 5:
        remove_friend()
    elif option == 6:
        print('Lista encerrada')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()

def add_friend() -> None:
    print('Adicionar nome a lista')
    print('~~~~~~~~~~~~~~~~~~~~~~\n')

    name: str = input('Informe o nome do convidado: ')
    cpf: str = input('Informe o CPF do convidado. (ex. 000.000.000-00): ')

    friend: friend = Friend(name, cpf)

    with open('LISTA_VIP.txt', 'a+') as archive:
        archive.write(f'{friend}\n')

    print(f'O convidado(a) {friend.name} com adicionado com sucesso!')
    sleep(2)
    menu()

def exhibt_friend() -> None:

    arch = Path("/home/bruna/Development/projeot_crud/LISTA_VIP.txt")

    if arch.is_file():

        with open('LISTA_VIP.txt', 'r') as archive:

            identifier: int = int(input('\nPor favor digite o identificador do convidado que você quera exibir. '))
            list_vip = archive.readlines()

            for line in list_vip:
                if line[0] == identifier:
                    print(line)
                    sleep(2)
                    menu()
                else:
                    print('Não existe convidado com este identificador')
                    sleep(2)
                    menu()
    else:
        print('Este usuário não existe ou foi removido da lista.')
        sleep(2)
        menu()


def list_vip() -> None:
    arch = Path("/home/bruna/Development/projeot_crud/LISTA_VIP.txt")

    if arch.is_file():   
        with open('LISTA_VIP.txt', 'r') as archive:
            print('     Lista VIP:')
            print('~~~~~~~~~~~~~~~~~~~~')

            for line in archive:
                print('_____________________________________________')
                print(line)
                sleep(1)
            sleep(2)
            menu()
    else:
        print('Ainda não existe uma lista VIP')
        sleep(2)
        menu()
    
def change_friend() -> None:

    arch = Path("/home/bruna/Development/projeot_crud/LISTA_VIP.txt")

    if arch.is_file():

        with open('LISTA_VIP.txt', 'a') as archive:

            identifier: int = int(input('Por favor digite o identificador do convidado que você quera exibir: '))

            new_name: str = input('Digite o nome do novo convidado para troca: ')
            new_cpf: str = input('Digite o CPF do novo convidado: (ex. 111.111.111-11). ')

            for line in archive:
                if line == identifier:
                    line_splited = linhe.rsplit(' ')
                    
                    print(line_splited)
                    sleep(2)
                    menu()
    else:
        print('Ainda não existe lista vip')
        sleep(2)
        menu()

def remove_friend() -> None:
    pass


if __name__ == '__main__':
    main()