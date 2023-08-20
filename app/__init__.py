from flask import Flask, render_template
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 附加路由
    from app.apiv1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    @app.cli.command("mycommand")
    def mycommand():
        print("这是用来自定义命令的!")

    return app