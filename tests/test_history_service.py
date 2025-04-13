import pytest
from unittest.mock import patch, MagicMock
from app.services.history_service import HistoryService
from app.models.query_model import DistanceQuery

@pytest.fixture
def mock_db_session():
    with patch("app.services.history_service.HistoryService.db_session") as mock_session:
        yield mock_session

def test_get_all_requests(mock_db_session):
    # Mock database session and query
    mock_db = MagicMock()
    mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = [
        DistanceQuery(
            id=1,
            address1="New York, NY",
            address2="Los Angeles, CA",
            distance_km=3940.2,
            created_at="2025-04-10T13:45:12.123Z",
        ),
        DistanceQuery(
            id=2,
            address1="Chicago, IL",
            address2="Houston, TX",
            distance_km=1514.3,
            created_at="2025-04-10T14:12:34.567Z",
        ),
    ]
    mock_db.query.return_value.count.return_value = 2
    mock_db_session.return_value.__enter__.return_value = mock_db

    # Call the service method
    result = HistoryService.get_all_requests(page=1, page_size=10)

    # Assertions
    assert result["page"] == 1
    assert result["page_size"] == 10
    assert result["total_count"] == 2
    assert result["total_pages"] == 1
    assert len(result["results"]) == 2
    assert result["results"][0]["address1"] == "New York, NY"
    assert result["results"][1]["distance_km"] == 1514.3