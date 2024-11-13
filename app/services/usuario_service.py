from models.usuario_model import Usuario
from repositories.usuario.repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if usuario_cadastrado:
                print("Usuário já castrado!")
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()