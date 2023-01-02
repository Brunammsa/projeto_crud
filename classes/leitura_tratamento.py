from classes.Friend import Friend
from typing import Optional
from pathlib import Path

class ListRepository:
    def __init__(self: object):
        self.__file = Path("list.csv")


    def show(self, id: int) -> Optional[Friend]:

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))

                if friend.id == id:
                    return friend
            return None
    

    def index(self) -> list[Friend]:
        self.__friends = []

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                self.__friends.append(friend)

            return self.__friends


    def remove(self, id: int) -> Optional[Friend]:
        self.__friends = []
        ids: list = []

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')

                for index, valor in enumerate(line_splited):
                    line_splited[index] = valor.strip()

                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                self.__friends.append(friend)
                ids.append(friend.id)

        if id not in ids:
            print('Usuário não encontrado')
            return

        with open('list.csv', 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for friend in self.__friends:
                if friend.id != id:
                    file.write(f'{friend.to_csv()}\n')
            print('Usuário removido')
