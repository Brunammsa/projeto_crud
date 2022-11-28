class Friend:
    count = 1
    def __init__(self: object, name: str, cpf: str) -> None:
        self.__get_last_id: int = Friend.count
        self.__name: str = name
        self.__cpf: str = cpf
        Friend.count += 1
    
    @property
    def get_last_id(self: object) -> int:
        return self.__get_last_id

    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, name: str) -> None:
        self.__name = name

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self: object, cpf: str) -> None:
        self.__cpf = cpf

    def __str__(self) -> str:
        return f'Nome: {self.name},  CPF: {self.cpf}'
