import os

from flask import Flask

from config import Config
from api.routes import bp
from api.errors import register_errors
from utils.logger import setup_logger


logger = setup_logger()


def create_app():

    app = Flask(__name__)

    app.config["MAX_CONTENT_LENGTH"] = Config.MAX_CONTENT_LENGTH

    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(Config.OUTPUT_FOLDER, exist_ok=True)

    app.register_blueprint(bp)

    register_errors(app)

    logger.info("Server Started")

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=True
    )