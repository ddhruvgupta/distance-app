from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from flask_cors import CORS
import os
import logging

from app.clients.geocoding_client import GeocodingClient
from app.repositories.distance_repository import DistanceRepository

logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to INFO
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
    CORS(app)

    # Database configuration
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL environment variable is not set.")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # API documentation configuration
    app.config.update({
        "API_TITLE": "Distance API",
        "API_VERSION": "v1",
        "OPENAPI_VERSION": "3.0.2",
        "OPENAPI_URL_PREFIX": "",  # Changed from "/" to ""
        "OPENAPI_SWAGGER_UI_PATH": "/docs",  # Changed from "/swagger-ui" to "/docs"
        "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
        "API_SPEC_OPTIONS": {
            "components": {
                "schemas": {},
                "responses": {
                    "UnauthorizedError": {
                        "description": "Authentication is required"
                    }
                }
            }
        }
    })

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    # Initialize services
    from app.services.history_service import HistoryService
    from app.services.distance_service import DistanceService
    history_service = HistoryService()
    geocoding_client = GeocodingClient()
    distance_repo = DistanceRepository()
    distance_service = DistanceService(geocoding_client, distance_repo)

    # Import and register blueprints
    from app.Controllers.distance_controller import create_distance_controller
    from app.Controllers.history_controller import create_history_controller
    history_bp = create_history_controller(history_service)
    distance_bp = create_distance_controller(distance_service)

    api.register_blueprint(distance_bp)
    api.register_blueprint(history_bp)

    # Flask should not handle CORS preflight requests automatically
    # because we are using Flask-CORS to handle them manually.
    @app.before_request
    def handle_options_request():
        if request.method == "OPTIONS":
            return '', 204

    @app.route("/")
    def index():
        return jsonify(list(app.blueprints.keys()))

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
