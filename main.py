from pathlib import Path
from classes.Friend import Friend
import csv

relative_path = Path("list.csv")


def main() -> None:
    print('~~~~~~~~~~~~~~ Bem vindo(a) a NOX ~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~ LISTA VIP ~~~~~~~~~~~~~~~~~~\n\n')
    menu()


def menu() -> None:
    option = None

    while (option != 6 or option is None):

        print('Selecione uma das opções abaixo:')
        print("1 - Adicionar\n2 - Exibir\n3 - Listar\n4 - Alterar\n5 - Remover\n6 - Sair")

        valid_options = ["1","2","3","4","5","6"]
        option: str = input()

        if (option not in valid_options):
            print('Opção inválida')
        if option == "1":
            add()
        elif option == "2":
            show()
        elif option == "3":
            list()
        elif option == "4":
            update()
        elif option == "5":
            remove()
        elif option == "6":
            exit(0)


def add() -> None:
    print('Adicionar nome a lista')
    print('~~~~~~~~~~~~~~~~~~~~~~\n')

    name: str = input('Informe o nome do convidado: ')
    cpf: str = input('Informe o CPF do convidado. (ex. 000.000.000-00): ')

    with open('last_inserted_id.txt', 'r+') as file_read:
        for line in file_read:
            number_last_id = line

    friend: Friend = Friend(name, cpf, int(number_last_id) + 1)

    with open('list.csv', 'a') as file:
        file.write(friend.to_csv())
        file.write('\n')

    with open('last_inserted_id.txt', 'w+') as file_id:
        file_id.write(str(friend.id))

    print(f'\nO convidado(a) {friend.name} com adicionado(a) com sucesso!\n')


def show() -> None:
    if relative_path.is_file():

        identifier: str = input('Por favor digite o identificador do convidado que você quera exibir: ')

        with open('list.csv', 'r') as file:
            for line in file:
                if line[0] == identifier:
                    print(line)
            else:
                print('\nEste usuário não existe ou foi removido da lista.')
    else:
        print('A lista vip ainda não existe.')


def list() -> None:
    if relative_path.is_file():
        with open('list.csv', 'r') as file:
            print('\n')
            for line in file:
                print(str(line))
        print('\n')
    else:
        print('A lista vip ainda não existe.')


def update() -> None:
    if relative_path.is_file():

        identifier: int = int(input('\nPor favor digite o identificador do convidado que você queira modificar. '))

        friends = []
        ids = []

        with open('list.csv', 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')

                for index, valor in enumerate(line_splited):
                    line_splited[index] = valor.strip()
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))

                ids.append(friend.id)
                friends.append(friend)

        if identifier not in ids:
            print('Este ID não existe')
            return

        name: str = input('Informe o nome atualizado do convidado: ')
        cpf: str = input('Informe o CPF atualizado do convidado. (ex. 000.000.000-00): ')

        with open('list.csv', 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for friend in friends:
                if friend.id == identifier:
                    friend.name = name
                    friend.cpf = cpf
                file.write(f'{friend.to_csv()}\n')
    else:
        print('Não existe arquivo')


def remove() -> None:
    if relative_path.is_file():
        identifier: str = str(input('Por favor digite o identificador do convidado que você quer exibir: '))

        with open('list.csv', 'r') as file:
            guest_list = file.readlines()

            for line in guest_list:
                line_guest = line.split(' ')
                first_position = str(line_guest[0])

                if first_position == identifier:
                    guest_list.remove(line)

                    print('Convidado removido')

        with open('list.csv', 'w') as file2:
            for line in guest_list:
                file2.write(line)
    else:

        print('Ainda não existe lista vip')


if __name__ == '__main__':

    main()