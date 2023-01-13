from classes.Friend import Friend
from pathlib import Path
from classes.friend_repository import FriendRepository
from validate_docbr import CPF
import csv


def main() -> None:
    print('~~~~~~~~~~~~~~ Bem vindo(a) a NOX ~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~ LISTA VIP ~~~~~~~~~~~~~~~~~~\n\n')
    menu()


def menu() -> None:
    option = None

    while option != 6 or option is None:

        print('Selecione uma das opções abaixo:')
        print(
            '1 - Adicionar\n2 - Exibir\n3 - Listar\n4 - Alterar\n5 - Remover\n6 - Sair'
        )

        valid_options = ['1', '2', '3', '4', '5', '6']
        option: str = input()

        if option not in valid_options:
            print('Opção inválida')
        if option == '1':
            add()
        elif option == '2':
            show()
        elif option == '3':
            list()
        elif option == '4':
            update()
        elif option == '5':
            remove()
        elif option == '6':
            exit(0)


def add() -> None:
    print('Adicionar nome a lista')
    print('~~~~~~~~~~~~~~~~~~~~~~\n')

    friend_repository: FriendRepository = FriendRepository()
    validacao = CPF()
    option = False

    while option != True:
        cpf: str = input('Informe o CPF do usuário: ')
        if validacao.validate(cpf) == False:
            print('CPF inválido')
            continue
        
        name: str = input('Informe o nome do usuário: ')
        if name == '':
            print('Nome inválido')
        else:
            friend = friend_repository.store(name, cpf)
            print(
                f'\nO usuário(a) {name} com adicionado(a) com sucesso!\n'
            )
            option = True


def show() -> None:

    friend_repository: FriendRepository = FriendRepository()
    option = False

    while option != True:
        ID: int = input('Digite o ID do usuário: ')
        if ID.isnumeric() == False:
            print('ID inválido')
            continue
        friend = friend_repository.show(int(ID))
        if friend is None:
            print('Não existe usuário com este ID')
        else:
            print(f'{friend}\n')
        option = True


def list() -> None:

    friend_repository: FriendRepository = FriendRepository()
    friends = friend_repository.index()

    for friend in friends:
        print(friend)


def update() -> None:
    friend_repository: FriendRepository = FriendRepository()
    option = False

    while option != True:
        ID: int = input('Digite o ID do usuário para atualizar: ')
        if ID.isnumeric() == False:
            print('ID inválido')
            continue

        friend = friend_repository.show(int(ID))
        if friend is None:
            print('Não existe usuário com este ID\n')
            continue

        name: str = input('Informe o nome atualizado do usuário: ')
        if name == '':
            print('Nome inválido')
            continue

        cpf: str = input('Informe o CPF do usuário: ')
        if validacao.validate(cpf) == False:
            print('CPF inválido')
            continue

        updated = friend_repository.update(friend)
        if updated == True:
            print('Usuário atualizado\n')
            option = True


def remove() -> None:

    friend_repository: FriendRepository = FriendRepository()
    option = False

    while option != True:
        ID: int = input(
            '\nDigite o identificador do usuário que você queira remover: '
        )
        if ID.isnumeric() == False:
            print('ID inválido')
            continue

        removed = friend_repository.remove(int(ID))
        if removed == False:
            print('Não existe usuário com este ID')
        else:
            print('Usuário removido\n')
            option = True


if __name__ == '__main__':

    main()
