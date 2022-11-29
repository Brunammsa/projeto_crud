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

    last_id: str = '0'
    with open('LISTA_VIP.txt', 'r') as archread:
        for line in archread:
            last_id = str(line[0])

    friend: dict = {'Identificador': int(last_id) + 1, 'Convidado': str(friend_class)}
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

    if arch.is_file():

        identifier: int = int(input('\nPor favor digite o identificador do convidado que você queira modificar. '))
        name: str = input('Informe o nome atualizado do convidado: ')
        cpf: str = input('Informe o CPF atualizado do convidado. (ex. 000.000.000-00): ')
        friend_class: Friend = Friend(name, cpf)

        with open('LISTA_VIP.txt', 'r') as archive:
            list_friends = archive.readlines()

        list_friends[identifier-1]= f'{identifier} | {friend_class} \n'
        print('Convidado modificado')

        with open('LISTA_VIP.txt', 'w') as archive2:
            for line in list_friends:
                archive2.write(line)
        sleep(1)
        menu()
    else:
        print('Lista não existe ainda')
        sleep(2)
        menu()

def remove_friend() -> None:

    if arch.is_file():
    
        identifier: int = int(input('Por favor digite o identificador do convidado que você quer exibir: '))
        with open('LISTA_VIP.txt', 'r') as archive:
            list_friends = archive.readlines()

        list_friends.remove(list_friends[identifier-1])
        print('Convidado removido')

        with open('LISTA_VIP.txt', 'w') as archive2:
            for line in list_friends:
                archive2.write(line)

        sleep(1)
        menu()

    else:
        print('Ainda não existe lista vip')
        sleep(2)
        menu()

if __name__ == '__main__':
    main()