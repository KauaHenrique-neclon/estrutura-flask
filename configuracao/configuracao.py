import secrets
from flask import Blueprint, send_from_directory
from flask_login import LoginManager
from model.model import exemplo


static_blueprint = Blueprint('static', __name__)
login_manager = LoginManager()


class config:


    """
     configuração do banco de dados, onde ele ira se conectar
    """
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:senha@localhost/database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



    # chave secreta 
    SECRET_KEY = secrets.token_hex(16)

   

    """
       Serve templates e statis do include
    """
    TEMPLATE_FOLDER = 'aplicacao/include/templates'
    @static_blueprint.route('/include/static/<path:filename>')
    def serveStatic(filename):
        return send_from_directory('aplicacao/include/static/', filename)
    


    """
        Essa função é usada pelo Flask-Login para carregar o usuário atual a partir do ID do usuário armazenado na sessão.
        é chamada no views e passado o objeto completo do usuario
    """
    @login_manager.user_loader
    def load_user(user_id):
        return exemplo.query.get(int(user_id))
  