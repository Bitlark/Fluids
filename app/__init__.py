from flask import Flask, render_template
from .config import config


def create_app(config_name='default'):
    conf = config[config_name]

    app = Flask(__name__)
    app.config.from_object(conf)

    # install plugins

    # register blue prints
    from app.exts import helper
    helper.init_app(app)
    helper.mount_blueprints()
    print(app.url_map)
    return app
