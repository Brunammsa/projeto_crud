class Friend:

    def __init__(self: object, name: str, cpf: str, id: int) -> None:
        self.__name: str = name
        self.__cpf: str = cpf
        self.__id: int = id
    
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

    @property
    def id(self: object) -> int:
        return self.__id

    def to_csv(self: object) -> str:
        return f'{self.__id}, {self.__name}, {self.__cpf}'

    def __str__(self) -> str:
        return self.name, self.cpf, self.id
