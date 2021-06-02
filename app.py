import logging
from pathlib import Path

from flask import Flask

from controller import setup_database
from view import views


def make_app() -> any:
    """
    Make the flask app

    :return:
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(name)s] %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logging.info("Creating app.")
    app = Flask(__name__)
    app.register_blueprint(views)
    path = Path(__file__)
    logging.info("Loading data from json.")
    setup_database(path)
    logging.info("App ready to use.")
    return app


if __name__ == "__main__":
    make_app()
