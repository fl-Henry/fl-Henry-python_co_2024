from flask import Flask


def create_app():
    app = Flask(__name__)

    # Здесь можно добавить настройки конфигурации
    # app.config.from_object('config.Config')

    # Импортировать маршруты
    from . import routes
    app.register_blueprint(routes.bp)

    return app
