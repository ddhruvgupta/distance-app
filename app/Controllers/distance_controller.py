from flask import jsonify, request
from flask_smorest import Blueprint, abort
from app.services.distance_service import DistanceService
from app.clients.geocoding_client import GeocodingClient
from app.db.session import get_db
from app.schemas.api_schemas import DistanceRequestSchema, DistanceResponseSchema
from contextlib import contextmanager
import logging
from app.repositories.distance_repository import DistanceRepository

logger = logging.getLogger(__name__)

class DistanceController:
    """Controller for distance calculation endpoints"""
    
    def __init__(self, distance_service: DistanceService):
        """
        Initialize the DistanceController with its dependencies.
        
        Args:
            distance_service: Instance of DistanceService for distance calculations.
        """
        self.blueprint = Blueprint(
            "distance", 
            __name__,
            url_prefix="/distance",
            description="Operations for calculating distances between addresses"
        )
        self.distance_service = distance_service
        self.register_routes()
        logger.info("DistanceController initialized")

    def calculate_distance(self, data):
        """Calculate distance between two addresses."""
        try:
            distance = self.distance_service.calculate_and_log_distance(
                data["address1"],
                data["address2"]
            )

            logger.info(f"Distance calculated: {distance} miles")
            return jsonify({"distance_miles": distance})
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            abort(400, message=str(e))
        except Exception as e:
            logger.error(f"Error calculating distance: {str(e)}")
            abort(400, message=f"Error calculating distance")

    def register_routes(self):
        """Register routes with Swagger documentation"""
        @self.blueprint.route("/", methods=["POST"])  
        @self.blueprint.arguments(DistanceRequestSchema)
        @self.blueprint.response(200, DistanceResponseSchema)
        @self.blueprint.doc(
            summary="Calculate distance between two addresses",
            description="Takes two addresses and returns the distance between them in miles"
        )
        def calculate(data): 
            result = self.calculate_distance(data)
            logger.info(f"Distance calculation result: {result}")
            return result


# Dependency Injection Setup
def create_distance_controller(geocoding_client: GeocodingClient) -> DistanceController:
    """Factory function to create a DistanceController with its dependencies."""
    @contextmanager
    def db_session_provider():
        db = next(get_db())
        try:
            yield db
        finally:
            db.close()

    distance_repository = DistanceRepository(db_session_provider)
    distance_service = DistanceService(geocoding_client, distance_repository)
    return DistanceController(distance_service).blueprint