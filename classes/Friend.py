from validate_docbr import CPF

class Friend:

    def __init__(self: object, name: str, cpf: str, id) -> None:
        self.__name: str = name.strip()
        self.__cpf: str = cpf.strip()
        self.__id: int = int(id)
    
    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, name: str) -> None:
        self.__name = name

    @property
    def cpf(self: object) -> str:
        mascara = CPF()
        cpf_masked = mascara.mask(self.__cpf)
        return cpf_masked

    @cpf.setter
    def cpf(self: object, cpf: str) -> None:
        self.__cpf = cpf


    def cpf_without_mask(self: object) -> str:
        return self.__cpf

    @property
    def id(self: object) -> int:
        return self.__id

    def to_csv(self: object) -> str:
        return f'{self.__id}, {self.__name}, {self.__cpf}'

    def __str__(self) -> str:
        return """
        ID: {}, Name: {}, CPF: {}
        """.format(self.id, self.name, self.cpf)
