import os

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

bp = Blueprint("api", __name__)

@bp.route("/")
def home():
    return """
    <h1>Palm Leaf Transliteration System</h1>
    <h2>Deployment Successful!</h2>

    <p>API Status:
    <a href="/health">Health Check</a></p>

    <p>Upload API:
    POST /upload</p>
    """
    
@bp.route("/health", methods=["GET"])
def health():

    return jsonify(
        {
            "status": "running",
            "project": "Malayanma Agentic AI"
        }
    )


@bp.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:

        return jsonify(
            {
                "error": "No file uploaded"
            }
        ), 400

    file = request.files["file"]

    os.makedirs("uploads", exist_ok=True)

    path = os.path.join("uploads", file.filename)

    file.save(path)

    return jsonify(
        {
            "message": "Uploaded",
            "path": path
        }
    )