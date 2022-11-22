from time import sleep
from functions.helpers import Friend

friends_dict: dict = {}
friends_list: list = []

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
    friends_dict = {friend_class.identifier: str(friend_class)}
    friends_list.append(friends_dict)

    with open('LISTA_VIP.txt', 'a') as archive:
        archive.write(friends_dict)

    print(f'O convidado(a) {friend_class.name} com adicionado(a) com sucesso!')
    sleep(2)
    menu()

def exhibt_friend() -> None:

    if friends_list:
        identifier: int = int(input('\nPor favor digite o identificador do convidado que você quera exibir. '))

        for friend in friends_list:
            if friend[0] == identifier:
                print(friend)
        else:
            print('\nEste usuário não existe ou foi removido da lista.')
            sleep(2)
            menu()
    else:
        print('A lista vip ainda não existe.')
        sleep(2)
        menu()


def list_vip() -> None:

    if friends_list:   
        for friend in friends_list:
            print('_____________________________________________')
            print(friend)
            sleep(1)
        print('\n')
        sleep(1)
        menu()
    else:
        print('Ainda não existe uma lista VIP')
        sleep(2)
        menu()
    
def change_friend() -> None:

    if arch.is_file():

        with open('LISTA_VIP.txt', 'a+') as archive:

            identifier: str = str(input('Por favor digite o identificador do convidado que você quera exibir: '))

            new_name: str = input('Digite o nome do novo convidado para troca: ')
            new_cpf: str = input('Digite o CPF do novo convidado: (ex. 111.111.111-11). ')

            for line in archive:
                if line[0] == identifier:
                    line = linhe.rsplit(' ')
                    line[3] = new_name
                    line[-1] = new_cpf
                    sleep(2)
                    menu()
                else:
                    print('Este usuário não existe ou foi removido da lista.')
                    sleep(2)
                    menu()

    else:
        print('Ainda não existe lista vip')
        sleep(2)
        menu()

def remove_friend() -> None:

    if arch.is_file():

        with open('LISTA_VIP.txt', 'r') as archive:
            lines = archive.readlines()
            identifier: int = int(input('Por favor digite o identificador do convidado que você quera exibir: '))
            for index, i in enumerate(lines):
                pass

    else:
        print('Ainda não existe lista vip')
        sleep(2)
        menu()


if __name__ == '__main__':
    main()