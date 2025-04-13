from app.models.query_model import DistanceQuery
from app.db.session import get_db
from contextlib import contextmanager

class HistoryService:
    @staticmethod
    @contextmanager
    def db_session():
        """Provide a transactional scope for database operations."""
        db = next(get_db())
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    def get_all_requests(page: int = 1, page_size: int = 10):
        """Retrieve paginated historical distance calculation requests."""
        with HistoryService.db_session() as db:
            # Calculate the offset for pagination
            offset = (page - 1) * page_size

            # Query the paginated records from the DistanceQuery table
            queries = db.query(DistanceQuery).offset(offset).limit(page_size).all()

            # Serialize the results into a list of dictionaries
            result = [
                {
                    "id": query.id,
                    "address1": query.address1,
                    "address2": query.address2,
                    "distance": query.distance,
                    "created_at": query.created_at,
                }
                for query in queries
            ]

            # Get the total count of records for metadata
            total_count = db.query(DistanceQuery).count()

            # Return the paginated results along with metadata
            return {
                "page": page,
                "page_size": page_size,
                "total_count": total_count,
                "total_pages": (total_count + page_size - 1) // page_size,  # Calculate total pages
                "results": result,
            }