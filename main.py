from time import sleep
from functions.helpers import Friend
from pathlib import Path

friends_list: list = []
arch = Path("/home/bruna/Development/projeot_crud/LISTA_VIP.txt")

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

    friend_class: Friend = Friend(name, cpf)
    friend: dict = {'Identificador': friend_class.identifier, 'Convidado': str(friend_class)}
    friends_list.append(friend)

    with open('LISTA_VIP.txt', 'a') as archive:
        archive.write(f'{friend["Identificador"]} | {friend["Convidado"]} \n')

    print(f'O convidado(a) {friend_class.name} com adicionado(a) com sucesso!')
    sleep(1)
    menu()

def exhibt_friend() -> None:

    if arch.is_file():
        identifier: int = input('\nPor favor digite o identificador do convidado que você quera exibir. ')

        with open('LISTA_VIP.txt', 'r') as archive:
            for line in archive:
                if line[0] == identifier:
                    print(line)
                    sleep(1)
                    menu()
            else:
                print('\nEste usuário não existe ou foi removido da lista.')
                sleep(2)
                menu()
    else:
        print('A lista vip ainda não existe.')
        sleep(2)
        menu()

def list_vip() -> None:
    if arch.is_file():
        with open('LISTA_VIP.txt', 'r') as archive:
            for line in archive:
                print(line)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                sleep(1)
            sleep(1)
            menu()
    else:
        print('A lista vip ainda não existe.')
        sleep(2)
        menu()

def change_friend() -> None:

    identifier: int = input('\nPor favor digite o identificador do convidado que você quera exibir. ')

    name: str = input('Informe o nome atualizado do convidado: ')
    cpf: str = input('Informe o CPF atualizado do convidado. (ex. 000.000.000-00): ')
    friend_class: Friend = Friend(name, cpf)

    for f in friends_list:
        for key, value in f.items():
            if key == identifier:
                f[key] == friend_class
            print(friends_list)

def remove_friend() -> None:

    if arch.is_file():
        list_copy = ''

        with open('LISTA_VIP.txt', 'r') as archive:

            identifier: str = str(input('Por favor digite o identificador do convidado que você quer exibir: '))
            for friend in archive:
                if friend[0] != identifier:
                    list_copy += friend

        with open('LISTA_VIP.txt', 'w+') as archive2:
            for friend in list_copy:
                archive2.write(friend)
            print('Convidado removido com sucesso.')
            sleep(1)
            menu()

    else:
        print('Ainda não existe lista vip')
        sleep(2)
        menu()


if __name__ == '__main__':
    main()