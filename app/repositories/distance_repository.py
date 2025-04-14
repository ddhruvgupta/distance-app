from app.models.query_model import DistanceQuery
from contextlib import contextmanager
from app.db.session import get_db

# Using SQL Alchemy for database interaction to prevent sql injection
class DistanceRepository:
    def __init__(self):
        """
        Initialize the DistanceRepository.
        """
        pass

    @contextmanager
    def db_session_provider(self):
        """Provide a database session."""
        db = next(get_db())
        try:
            yield db
        finally:
            db.close()

    def log_distance_query(self, address1, address2, distance):
        """Log the distance query into the database."""
        with self.db_session_provider() as db:
            query = DistanceQuery(
                address1=address1,
                address2=address2,
                distance=distance
            )
            db.add(query)
            db.commit()