from classes.Friend import Friend

class LeituraETratamento:
    def __init__(self: object, texto, id: list, friends: list):
        self.__texto = texto
        self.__id = id
        self.__friends = friends

    def leitura_e_tratamento_da_lista_csv(self: object):

        friends: list = [self.__friends]
        id: list = [self.__id]

        with open(self.__texto, 'r') as file:
            friends_lists = file.readlines()
            for line in friends_lists[1:]:
                line_striped = line.strip()
                line_splited = line_striped.split(',')

                for index, valor in enumerate(line_splited):
                    line_splited[index] = valor.strip()
                
                friend: Friend = Friend(line_splited[1], line_splited[2], int(line_splited[0]))

                id.append(friend.id)
                friends.append(friend)
    
    @property
    def puxa_id(self: object) -> list:
        return self.__id

    @property
    def puxa_friends(self: object) -> list:
        return self.__friends




