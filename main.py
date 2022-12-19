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
            change_guest()
        elif option == "5":
            remove_guest()
        elif option == "6":
            exit(0)


def add() -> None:
    print('Adicionar nome a lista')
    print('~~~~~~~~~~~~~~~~~~~~~~\n')

    name: str = input('Informe o nome do convidado: ')
    cpf: str = input('Informe o CPF do convidado. (ex. 000.000.000-00): ')

    with open('last_inserted_id.txt', 'r+') as arch_read:
        for line in arch_read:
            number_last_id = line

    friend: Friend = Friend(name, cpf, int(number_last_id) + 1)

    with open('list.csv', 'a') as archive:
        archive.write(friend.to_csv())
        archive.write('\n')

    with open('last_inserted_id.txt', 'w+') as arch_id:
        arch_id.write(str(friend.id))

    print(f'\nO convidado(a) {friend.name} com adicionado(a) com sucesso!\n')


def show() -> None:
    if relative_path.is_file():

        identifier: int = input('Por favor digite o identificador do convidado que você quera exibir: ')

        with open('list.csv', 'r') as archive:
            archive_csv = csv.reader(archive, delimiter=',')
            for i, line in enumerate(archive_csv):
                    
                print(line[i])
            else:
                print('\nEste usuário não existe ou foi removido da lista.')
    else:
        print('A lista vip ainda não existe.')


def list() -> None:
    if relative_path.is_file():
        with open('list.csv', 'r') as archive:
            archive_csv = csv.reader(archive, delimiter=',')
            print('\n')
            for line in archive_csv:
                print(str(line))
            print('\n')
    else:
        print('A lista vip ainda não existe.')


def change_guest() -> None:
    if relative_path.is_file():
        identifier: int = int(input('\nPor favor digite o identificador do convidado que você queira modificar. '))
        name: str = input('Informe o nome atualizado do convidado: ')
        cpf: str = input('Informe o CPF atualizado do convidado. (ex. 000.000.000-00): ')
        class_of_guests: Friend = Friend(name, cpf)

        with open('list.csv', 'r') as archive:
            guest_list = archive.readlines()

        guest_list[identifier-1]= f'{identifier} | {class_of_guests} \n'

        print('Convidado modificado')

        with open('list.csv', 'w') as archive2:
            for line in guest_list:
                archive2.write(line)
    else:
        print('Lista não existe ainda')


def remove_guest() -> None:
    if relative_path.is_file():
        identifier: str = str(input('Por favor digite o identificador do convidado que você quer exibir: '))

        with open('list.csv', 'r') as archive:
            guest_list = archive.readlines()

            for line in guest_list:
                line_guest = line.split(' ')
                first_position = str(line_guest[0])

                if first_position == identifier:
                    guest_list.remove(line)

                    print('Convidado removido')

        with open('list.csv', 'w') as archive2:
            for line in guest_list:
                archive2.write(line)
    else:

        print('Ainda não existe lista vip')


if __name__ == '__main__':

    main()