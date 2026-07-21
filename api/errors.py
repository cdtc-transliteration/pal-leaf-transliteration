from flask import jsonify


def register_errors(app):

    @app.errorhandler(404)
    def page_not_found(e):

        return jsonify(
            {
                "error": "Not Found"
            }
        ), 404

    @app.errorhandler(500)
    def internal_error(e):

        return jsonify(
            {
                "error": "Internal Server Error"
            }
        ), 500