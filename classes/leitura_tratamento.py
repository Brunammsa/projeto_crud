from classes.Friend import Friend
from typing import Optional

class ListRepository:
    def __init__(self: object):
        self.__file = Path("list.csv")
        self.__friends = []


    def show(self, id: int) -> Optional[Friend]:

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))

                if friend.id == identifier:
                    return friend
            return None
    

    def index(self) -> list[Friend]:
        
        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                self.__friends.append(friend)

            return self.__friends


    def update(self):
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