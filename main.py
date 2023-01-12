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
        cpf: int = input('Informe o CPF do convidado: ')
        if validacao.validate(cpf):
            name: str = input('Informe o nome do convidado: ')
            if name != '':
                friend = friend_repository.store(name, cpf)
                print(
                    f'\nO convidado(a) {name} com adicionado(a) com sucesso!\n'
                )
                return True
            else:
                print('Nome inválido')
        else:
            print('CPF inválido')


def show() -> None:

    friend_repository: FriendRepository = FriendRepository()
    option = False

    while option != True:
        identifier: int = input('Digite o ID do convidado: ')
        friend = friend_repository.show(identifier)

        if identifier.isnumeric() and identifier != None:
            if friend is None:
                print('Não existe usuário com este ID')
            else:
                print(f'{friend}\n')
            return True
        print('ID inválido')


def list() -> None:

    friend_repository: FriendRepository = FriendRepository()
    friends = friend_repository.index()

    for friend in friends:
        print(friend)


def update() -> None:
    friend_repository: FriendRepository = FriendRepository()
    option = False

    while option != True:
        identifier: int = input('Digite o ID do convidado para atualizar: ')
        friend = friend_repository.show(identifier)

        if identifier.isnumeric() and identifier != None:
            if friend is None:
                print('Não existe usuário com este ID\n')
            else:
                name: str = input('Informe o nome atualizado do convidado: ')
                if name != '':
                    cpf: str = input('Informe o CPF atualizado do convidado: ')

                    if validacao.validate(cpf):
                        friend.name = name
                        friend.cpf = cpf
                        updated = friend_repository.update(friend)

                        if updated == True:
                            print('Usuário atualizado\n')
                            return True
                    else:
                        print('CPF inválido')
                else:
                    print('Nome inválido')
        else:
            print('ID inválido')


def remove() -> None:

    friend_repository: FriendRepository = FriendRepository()
    option = False

    while option != True:
        identifier: int = input(
            '\nPor favor digite o identificador do convidado que você queira remover: '
        )
        removed = friend_repository.remove(identifier)

        if identifier.isnumeric() and identifier != None:
            if removed == False:
                print('Não existe usuário com este ID')
            else:
                print('Usuário removido\n')
                return True
        else:
            print('ID inválido')


if __name__ == '__main__':

    main()
