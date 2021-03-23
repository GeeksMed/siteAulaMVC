from application.model.dao.usuario import UsuarioDAO
from flask import render_template, request

#Administrador solicita visualizar todos os usuários (HTTP REQUEST)
#Controlador receber essa solicitação (entry-point) (HTTP REQUEST)
#Controlador solicita ao Model os usuários que o administrador pode visualizar.
#Model manusear os dados, lidar e aplicar com as regras e retornar os usuários.
#Controlador solicita que a View formate os dados dos usuários.
#View aplica princípios de UX e retorna os dados formatados
#Controlador retorna os dados formatados para o administrador visualizar (HTTP RESPONSE)

@app.route('/')
def exibir_todos():
    usuario_list = UsuarioDAO().listar_todos()
    return render_template('home.html', usuario_list = usuario_list)
    