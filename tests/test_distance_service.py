import pytest
from unittest.mock import MagicMock
from app.services.distance_service import DistanceService
from app.repositories.distance_repository import DistanceRepository
from contextlib import contextmanager

@pytest.fixture
def mock_distance_repository():
    """Provide a mock distance repository."""
    return MagicMock()

@pytest.fixture
def mock_geocoding_client():
    """Provide a mock geocoding client."""
    mock_client = MagicMock()
    mock_client.get_geocode.side_effect = [
        (40.7128, -74.0060),  # New York, NY
        (34.0522, -118.2437),  # Los Angeles, CA
    ]
    return mock_client

def test_calculate_distance(mock_geocoding_client):
    # Initialize the DistanceService with the mock geocoding client and a mock repository
    distance_service = DistanceService(mock_geocoding_client, MagicMock())

    # Call the calculate_distance method
    result = distance_service.calculate_distance("New York, NY", "Los Angeles, CA")

    # Assertions
    assert round(result, 1) == 2451  # Approximate distance in miles
    mock_geocoding_client.get_geocode.assert_any_call("New York, NY")
    mock_geocoding_client.get_geocode.assert_any_call("Los Angeles, CA")

def test_calculate_and_log_distance(mock_geocoding_client, mock_distance_repository):
    # Initialize the DistanceService with mocks
    distance_service = DistanceService(mock_geocoding_client, mock_distance_repository)

    # Call the calculate_and_log_distance method
    distance = distance_service.calculate_and_log_distance("New York, NY", "Los Angeles, CA")

    # Assertions
    assert round(distance, 1) == 2451  # Approximate distance in miles
    mock_geocoding_client.get_geocode.assert_any_call("New York, NY")
    mock_geocoding_client.get_geocode.assert_any_call("Los Angeles, CA")
    mock_distance_repository.log_distance_query.assert_called_once_with(
        "New York, NY", "Los Angeles, CA", distance
    )