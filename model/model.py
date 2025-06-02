from configuracao.banco import db
import bcrypt


class exemplo(db.Model):

    __tablename__ = 'exemplo'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(240),nullable=False)


    def __init__(self, nome, password):
        self.nome = nome
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')


    """
       Metodo importante, usado pelo decorador load_user para obter o id do usuario ativo na sessão
    """
    def get_id(self):
        return self.id
    

    
    """
       Metodo de verificação de senha para login
       ele verifica a senha, se for igual, ira retornar True, se não, retorna False
    """
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))