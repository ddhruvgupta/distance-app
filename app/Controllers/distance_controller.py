from flask import jsonify, request
from flask_smorest import Blueprint, abort
from app.clients.geocoding_client import GeocodingClient
from app.db.session import get_db
from app.schemas.api_schemas import DistanceRequestSchema, DistanceResponseSchema
from contextlib import contextmanager
import logging
from app.repositories.distance_repository import DistanceRepository
from app.services.distance_service import DistanceService
from bleach import clean

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
            # Log the incoming request data
            logger.info(f"Incoming request data: {data}")

            # Sanitize inputs
            address1 = clean(data["address1"], strip=True)
            address2 = clean(data["address2"], strip=True)

            # Calculate and log the distance
            distance = self.distance_service.calculate_and_log_distance(address1, address2)

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
            try:
                logger.info(f"Received request payload: {data}")
                result = self.calculate_distance(data)
                logger.info(f"Distance calculation result: {result}")
                return result
            except Exception as e:
                logger.error(f"Error processing request: {str(e)}")
                raise


# Dependency Injection Setup
def create_distance_controller(distance_service: DistanceService) -> DistanceController:
    """Factory function to create a DistanceController with its dependencies."""
    if not distance_service:
        raise ValueError("DistanceService is required")
    
    return DistanceController(distance_service).blueprint