from classes.Friend import Friend
from typing import Optional
from pathlib import Path

class FriendRepository:
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
        list_friends = []

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                list_friends.append(friend)

            return list_friends


    def update(self, id: int) -> bool:
        list_friends = []
        list_ids = []

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                list_friends.append(friend)
                list_ids.append(friend.id)
        
        if id not in list_ids:
            return False

        with open(self.__file, 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for temp_friend in list_friends:
                if temp_friend.id == id:
                    temp_friend.name = friend.name
                    temp_friend.cpf = friend.cpf
                file.write(f'{temp_friend.to_csv()}\n')
        return True


    def remove(self, id: int) -> bool:
        list_friends = []
        list_ids = []

        with open(self.__file, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))
                list_friends.append(friend)
                list_ids.append(friend.id)
        
        if id not in list_ids:
            return False
        
        with open(self.__file, 'w+') as file:
            file.write('ID, NOME, CPF\n')
            for friend in list_friends:
                if friend.id != id:
                    file.write(f'{friend.to_csv()}\n')
        return True
