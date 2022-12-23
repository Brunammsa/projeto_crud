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


    def update(self, friend: Friend) -> None:
        pass