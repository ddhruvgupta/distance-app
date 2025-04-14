from geopy.distance import geodesic
from app.clients.geocoding_client import GeocodingClient
from app.repositories.distance_repository import DistanceRepository
from icecream import ic
from bleach import clean

class DistanceService:
    def __init__(self, geocoding_client: GeocodingClient, distance_repository: DistanceRepository):
        """
        Initialize the DistanceService.

        :param geocoding_client: A client for geocoding addresses.
        :param distance_repository: A repository for handling distance-related database operations.
        """
        self.geocoding_client = geocoding_client
        self.distance_repository = distance_repository

    def calculate_distance(self, address1, address2):
        """Calculate the distance between two addresses."""
        # Use the geocoding client to fetch coordinates
        coords1 = self.geocoding_client.get_geocode(address1)
        coords2 = self.geocoding_client.get_geocode(address2)

        # Calculate the distance in miles
        return geodesic(coords1, coords2).miles

    def calculate_and_log_distance(self, address1, address2):
        """Calculate the distance and log the query into the database."""
        # Sanitize inputs to prevent XSS
        address1 = clean(address1, strip=True)
        address2 = clean(address2, strip=True)

        distance = self.calculate_distance(address1, address2)

        # Delegate logging to the repository
        self.distance_repository.log_distance_query(address1, address2, distance)
        ic(distance)
        return distance