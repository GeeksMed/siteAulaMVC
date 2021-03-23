class Usuario():

    __id: int
    __nome: str
    __sobrenome: str
    __idade: int

    def __init__(self):
        pass
    
    def get_id(self) -> int:
        return self.__id
        
    def get_nome(self) -> str:
        return self.__nome

    def get_sobrenome(self) -> str:
        return self.__sobrenome

    def get_idade(self) -> int:
        return self.__idade

    def set_id(self, id:int) -> None:
        self.__id = id
    
    def set_nome(self, nome:str) -> None:
        self.__nome = nome

    def set_sobrenome(self, sobrenome:str) -> None:
        self.__sobrenome = sobrenome
    
    def self_idade(self, idade:int) -> None:
        self.__idade = idade
    