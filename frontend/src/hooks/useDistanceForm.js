import { useState } from 'react';
import fetchDistance from '../api_endpoints/distance_endpoint';

const milesToKm = (miles) => (miles * 1.60934).toFixed(2);

export const useDistanceForm = () => {
  const [address1, setAddress1] = useState('');
  const [address2, setAddress2] = useState('');
  const [unit, setUnit] = useState('miles');
  const [distance, setDistance] = useState(null);
  const [error, setError] = useState(null);

  const formatDistance = (distanceInMiles) => {
    switch (unit) {
      case 'kilometers':
        return `${milesToKm(distanceInMiles)} km`;
      case 'both':
        return `${distanceInMiles} miles (${milesToKm(distanceInMiles)} km)`;
      default:
        return `${distanceInMiles} miles`;
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setDistance(null);

    try {
      const result = await fetchDistance(address1, address2);
      setDistance(result.distance_miles);
    } catch (err) {
      setError(err.message);
    }
  };

  return {
    address1,
    setAddress1,
    address2,
    setAddress2,
    unit,
    setUnit,
    distance,
    error,
    setError,
    formatDistance,
    handleSubmit,
  };
};