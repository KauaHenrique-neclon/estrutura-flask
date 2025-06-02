from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

# criando os varificador, ele verificará se o usuario está logado
def verificar(f):
    @wraps(f)
    def decorarAdm(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Voce precisa esta logado para acessar")
            return redirect(url_for('')) # redireciona para alguma pagina ser n estiver logado
        return f(*args, **kwargs)
    return decorarAdm