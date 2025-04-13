from flask import request
from flask_smorest import Blueprint, abort
from app.services.history_service import HistoryService
from app.schemas.api_schemas import PaginatedHistoryResponseSchema
from icecream import ic


class HistoryController:
    def __init__(self, history_service: HistoryService):
        """
        Initialize the History Controller.
        
        Args:
            history_service: Service layer for handling history-related operations
        """
        self.history_service = history_service
        self.blueprint = Blueprint(
            "history", 
            __name__,
            url_prefix="/history",
            description="Operations for viewing distance calculation history"
        )
        self.register_routes()

    def get_history(self, request):
        """Handle GET requests for paginated history."""
        page = request.args.get("page", "1")
        page_size = request.args.get("page_size", "10")
        
        # Validate pagination parameters
        if not page.isdigit() or int(page) <= 0:
            abort(400, message="Invalid 'page' parameter. Must be a positive integer.")
        if not page_size.isdigit() or int(page_size) <= 0:
            abort(400, message="Invalid 'page_size' parameter. Must be a positive integer.")

        try:
            result = self.history_service.get_all_requests(
                page=int(page),
                page_size=int(page_size)
            )
            return result
        except ValueError as ve:
            ic(f"Validation error: {str(ve)}")
            abort(400, message=str(ve))
        except Exception as e:
            ic(f"Unexpected error: {str(e)}")
            abort(500, message=f"Error retrieving historical data: {str(e)}")

    def register_routes(self) -> None:
        """Register all routes with Swagger documentation."""
        # Wrapper function to pass the request explicitly
        def view_func():
            return self.get_history(request)

        # Attach Swagger documentation and response schema
        self.blueprint.add_url_rule(
            "/",
            view_func=self.blueprint.response(200, PaginatedHistoryResponseSchema)(
                self.blueprint.doc(
                    description="Get paginated history of distance calculations",
                    parameters=[
                        {
                            "name": "page",
                            "in": "query",
                            "description": "Page number",
                            "default": 1,
                            "schema": {"type": "integer", "minimum": 1}
                        },
                        {
                            "name": "page_size",
                            "in": "query",
                            "description": "Items per page",
                            "default": 10,
                            "schema": {"type": "integer", "minimum": 1, "maximum": 100}
                        }
                    ]
                )(view_func)
            ),
            methods=["GET"]
        )


def create_history_controller(history_service: HistoryService) -> Blueprint:
    """
    Factory function to create the history controller and return its blueprint.
    
    Args:
        history_service: Service layer for handling history-related operations
        
    Returns:
        Configured Flask Blueprint
    """
    controller = HistoryController(history_service)
    return controller.blueprint