from flask import Flask
from configuracao.configuracao import config, static_blueprint, login_manager
from configuracao.banco import db
from flask_migrate import Migrate
import os
from aplicacao.views.exemploViews.exemplo import exemplo


def appFlask():

    app = Flask(__name__)
    app.config.from_object(config)
    login_manager.__init__(app)


    # criar banco de dados pelo model
    db.__init__(app)
    migrate = Migrate(app, db)


    #criando templates includes
    app.jinja_loader.searchpath.append(os.path.join(app.root_path, app.config['TEMPLATE_FOLDER']))
    app.register_blueprint(static_blueprint)



    # criando rotas
    routes = [(exemplo,None),
              #(teste, '/teste') pode ser esse tipo tbm, passa um prefix
              ]
    for blueprint, prefix in routes:
        app.register_blueprint(blueprint, url_prefix=prefix)



    ## codigo para criar a tabela automaticamente
    with app.app_context():
        try:
            db.create_all()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")

    return app


#iniciando a aplicação
app = appFlask()
if __name__ == '__main__':
    app.run(debug=True)