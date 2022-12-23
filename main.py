from pathlib import Path
from classes.Friend import Friend
from classes.leitura_tratamento import ListRepository
import csv


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

    identifier: int = int(input('Por favor digite o identificador do convidado que você quera exibir: '))
    list_repository: ListRepository = ListRepository()

    friend = list_repository.show(identifier)

    if friend is None:
        print('Não existe usuário com este ID')
    else:
        print(friend.to_csv())


def list() -> None:

    list_repository: ListRepository = ListRepository()
    friends = list_repository.index()
    
    for friend in friends:
        print(friend.to_csv())


def update() -> None:

    identifier: int = int(input('Por favor digite o identificador do convidado que você quera exibir: '))
    list_repository: ListRepository = ListRepository()

    friend = list_repository.show(identifier)

    if friend is None:
        print('Não existe usuário com este ID')
        return

    name: str = input('Informe o nome atualizado do convidado: ')
    cpf: str = input('Informe o CPF atualizado do convidado. (ex. 000.000.000-00): ')

    friend.name = name
    friend.cpf = cpf

    list_repository.update(friend)
    

def remove() -> None:
    if relative_path.is_file():

        identifier: int = int(input('\nPor favor digite o identificador do convidado que você queira modificar. '))

        friends: list = []
        ids: list = []

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
            print('Este ID não existe\n')
            return

        with open('list.csv', 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for friend in friends:
                if friend.id != identifier:
                    file.write(f'{friend.to_csv()}\n')
            print('Convidado removido\n!')
    else:
        print('Não existe arquivo\n')

if __name__ == '__main__':

    main()