from flask import Blueprint, render_template, redirect
from model.model import usuarios
from flask.views import MethodView
from flask_login import login_user


exemplo = Blueprint('login',__name__, template_folder='templates',
                    static_folder='staticExemplo')




class exemploClass(MethodView):


    def get(self):
        return render_template('template')



    def post(self):
        """
        logica de request
        user = Usuarios.query.filter_by(email=emailUser).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home.home'))
        """


exemplo.add_url_rule('/exemplo',view_func=exemploClass.as_views('exemploPage'),methods=['GET', 'POST'])