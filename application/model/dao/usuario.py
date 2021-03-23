from application.model.entity.usuario import Usuario
from typing import List

class UsuarioDAO:

    def listar_todos(self) -> List[Usuario]:
        pass

    def buscar_por_nome(self, nome:str) -> List[Usuario]:
        pass

    def inserir(self, usuario: Usuario) -> bool:
        pass

    def atualizar(self, usuario: Usuario) -> bool:
        pass

    def excluir(self, usuario_id:int) -> bool:
        pass