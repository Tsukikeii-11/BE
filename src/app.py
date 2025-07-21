from flask import Flask
from .api.middleware import middleware
from .api.responses import success_response
from .infrastructure.databases import init_db
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    init_db(app)

    # Register middleware
    middleware(app)

    # Register routes
    # Example: app.add_url_rule('/example', view_func=example_view)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)