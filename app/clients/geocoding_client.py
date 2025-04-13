import requests
from requests.exceptions import RequestException
import time
from functools import lru_cache
from tenacity import retry, stop_after_attempt, wait_fixed

class GeocodingClient:
    def __init__(self, base_url="https://nominatim.openstreetmap.org/search"):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'DistanceAPI/1.0', 
            'Accept': 'application/json'
        }
        self.last_request_time = 0
        self.min_request_interval = 1.0  # Minimum 1 second between requests

    def _rate_limit(self):
        """Implement rate limiting"""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()

    @lru_cache(maxsize=1000)  # Cache up to 1000 recent lookups
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def get_geocode(self, address):
        """Fetch geocode for a given address using the Nominatim API."""
        if not address or not address.strip():
            raise ValueError("The address provided is empty or invalid. Please provide a valid address.")
        
        params = {
            "q": address,
            "format": "json",
            "addressdetails": 1,
        }
        
        try:
            self._rate_limit()  # Ensure we don't exceed rate limits
            response = requests.get(
                self.base_url, 
                params=params,
                headers=self.headers,
                timeout=5  # 5 second timeout
            )
            response.raise_for_status()
            results = response.json()

            if not results or "boundingbox" not in results[0]:
                raise ValueError(
                    f"Address '{address}' could not be geocoded accurately. "
                    "Please refine the address and try again."
                )

            # Return latitude and longitude
            return float(results[0]["lat"]), float(results[0]["lon"])
            
        except RequestException as e:
            raise ValueError(f"Error geocoding address: {str(e)}")