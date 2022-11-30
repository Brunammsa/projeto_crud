from time import sleep
from pathlib import Path
from functions.helpers import Friend

guest_list: list = []
absolute_path = Path("/home/bruna/Development/projeot_crud/LISTA_VIP.txt")

def main() -> None:
    menu()

def menu() -> None:
    print('~~~~~~~~~~~~~~ Bem vindo(a) a NOX ~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~ LISTA VIP ~~~~~~~~~~~~~~~~~~\n\n')
    print('Selecione uma das opções abaixo:\n')
    print('1- Adicionar\n2- Exibir\n3- Listar\n4- Alterar\n5- Remover\n6- Encerrar lista')

    option: int = int(input())

    if option == 1:
        add_guest()
    elif option == 2:
        exhibt_guest()
    elif option == 3:
        list_vip()
    elif option == 4:
        change_guest()
    elif option == 5:
        remove_guest()
    elif option == 6:
        print('Lista encerrada')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()

def add_guest() -> None:
    print('Adicionar nome a lista')
    print('~~~~~~~~~~~~~~~~~~~~~~\n')

    name: str = input('Informe o nome do convidado: ')
    cpf: str = input('Informe o CPF do convidado. (ex. 000.000.000-00): ')

    class_of_guests: Friend = Friend(name, cpf)

    number_last_id = '0'
    with open('last_id', 'r+') as arch_read:
        for line in arch_read:
            number_last_id = line

    guest: dict = {'Identificador': int(number_last_id) + 1, 'Convidado': str(class_of_guests)}
    guest_list.append(guest)

    with open('LISTA_VIP.txt', 'a') as archive:
        archive.write(f'{guest["Identificador"]} | {guest["Convidado"]} \n')
    
    with open('LISTA_VIP.txt', 'r') as arch_read:
        for line in arch_read:
            line_list = line.split(' ')
            last_id = str(line_list[0])

        with open('last_id', 'w+') as arch_id:
            arch_id.write(last_id)

    print(f'O convidado(a) {class_of_guests.name} com adicionado(a) com sucesso!')
    sleep(1)
    menu()

def exhibt_guest() -> None:

    if absolute_path.is_file():
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
    if absolute_path.is_file():
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

def change_guest() -> None:

    if absolute_path.is_file():

        identifier: int = int(input('\nPor favor digite o identificador do convidado que você queira modificar. '))
        name: str = input('Informe o nome atualizado do convidado: ')
        cpf: str = input('Informe o CPF atualizado do convidado. (ex. 000.000.000-00): ')
        class_of_guests: Friend = Friend(name, cpf)

        with open('LISTA_VIP.txt', 'r') as archive:
            guest_list = archive.readlines()

        guest_list[identifier-1]= f'{identifier} | {class_of_guests} \n'
        print('Convidado modificado')

        with open('LISTA_VIP.txt', 'w') as archive2:
            for line in guest_list:
                archive2.write(line)
        sleep(1)
        menu()
    else:
        print('Lista não existe ainda')
        sleep(2)
        menu()

def remove_guest() -> None:

    if absolute_path.is_file():
    
        identifier: str = str(input('Por favor digite o identificador do convidado que você quer exibir: '))
        with open('LISTA_VIP.txt', 'r') as archive:
            guest_list = archive.readlines()

            for line in guest_list:
                line_guest = line.split(' ')
                first_position = str(line_guest[0])

                if first_position == identifier:
                    guest_list.remove(line)
                    print('Convidado removido')

        with open('LISTA_VIP.txt', 'w') as archive2:
            for line in guest_list:
                archive2.write(line)

        sleep(1)
        menu()

    else:
        print('Ainda não existe lista vip')
        sleep(2)
        menu()

if __name__ == '__main__':
    main()