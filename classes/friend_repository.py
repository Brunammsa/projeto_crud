from classes.Friend import Friend
from typing import Optional
from pathlib import Path

class FriendRepository:
    def __init__(self: object):
        self.__file = Path("list.csv")
        self.__friends = []
        self.__ids = []


    def show(self, id: int) -> Optional[Friend]:

        friend_found = None
        
        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                self.__friends.append(friend)

                if friend.id == id:
                    friend_found = friend
            return friend_found
    

    def index(self) -> list[Friend]:

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                self.__friends.append(friend)

            return self.__friends


    def update(self, name: str, cpf: str, id: int) -> None:

        with open('list.csv', 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for friend in self.__friends:
                if friend.id == id:
                    friend.name = name
                    friend.cpf = cpf
                file.write(f'{friend.to_csv()}\n')


    def remove(self, id: int) -> bool:
        
        with open('list.csv', 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')

                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))

                self.__ids.append(friend.id)
                self.__friends.append(friend)

        if id not in self.__ids:
            return False
            
        with open('list.csv', 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for friend in self.__friends:
                if friend.id != id:
                    file.write(f'{friend.to_csv()}\n')
        return True
