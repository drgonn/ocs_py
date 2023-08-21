from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

from config import config, Config


db = SQLAlchemy()
celery = Celery(__name__, broker=Config.BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    celery.conf.update(app.config)

    # 附加路由
    from app.apiv1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    @app.cli.command("mycommand")
    def mycommand():
        print("这是用来自定义命令的!")
    
    @app.cli.command("shell", help="Run the interactive shell")
    def shell():
        import code
        code.interact(local=globals())


    return app