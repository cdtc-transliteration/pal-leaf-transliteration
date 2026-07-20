import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    HOST = os.getenv("HOST", "0.0.0.0")

    PORT = int(os.getenv("PORT", 5000))

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

    OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "output")

    MAX_CONTENT_LENGTH = int(
        os.getenv("MAX_CONTENT_LENGTH", 50 * 1024 * 1024)
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")