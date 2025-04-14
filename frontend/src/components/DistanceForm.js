import React, { useState } from 'react';
import {
  Box,
  TextField,
  RadioGroup,
  FormControlLabel,
  Radio,
  Button,
  FormLabel,
  FormControl,
  Alert,
  Snackbar,
  Grid
} from '@mui/material';
import CalculateIcon from '@mui/icons-material/Calculate'; // Import the calculator icon
import fetchDistance from '../api_endpoints/distance_endpoint';

// Helper function to convert miles to kilometers
const milesToKm = (miles) => (miles * 1.60934).toFixed(2);

function DistanceForm() {
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

  return (
    <Box component="form" onSubmit={handleSubmit} mt={2}>
      <Grid container spacing={3} alignItems="flex-start">
        <Grid item xs={12} md={3}>
          <FormLabel>Source Address</FormLabel>
          <TextField
            fullWidth
            variant="filled"
            label="Input Address"
            value={address1}
            onChange={(e) => setAddress1(e.target.value)}
            sx={{
              backgroundColor: '#f9f9f9', // Light fill color
              borderRadius: 1,            // Slightly rounded corners
              input: { padding: '12px' }, // More padding inside
            }}
          />
        </Grid>

        <Grid item xs={12} md={3}>
          <FormLabel>Destination Address</FormLabel>
          <TextField
            fullWidth
            label="Input Address"
            variant="filled"
            value={address2}
            onChange={(e) => setAddress2(e.target.value)}
            sx={{
              backgroundColor: '#f9f9f9', // Light fill color
              borderRadius: 1,            // Slightly rounded corners
              input: { padding: '12px' }, // More padding inside
            }}
          />
        </Grid>

        <Grid item xs={12} md={3}>
          <FormControl component="fieldset">
            <FormLabel>Unit</FormLabel>
            <RadioGroup
              value={unit}
              onChange={(e) => setUnit(e.target.value)}
            >
              <FormControlLabel value="miles" control={<Radio />} label="Miles" />
              <FormControlLabel value="kilometers" control={<Radio />} label="Kilometers" />
              <FormControlLabel value="both" control={<Radio />} label="Both" />
            </RadioGroup>
          </FormControl>
        </Grid>

        <Grid item xs={12} md={3}>
          <FormControl component="fieldset">
            <FormLabel>Distance</FormLabel>
            {distance !== null && (
              <Alert severity="success">
                Distance: {formatDistance(distance)}
              </Alert>
            )}
          </FormControl>
        </Grid>
      </Grid>

      <Box mt={4}>
        <Button
          variant="contained"
          color="error"
          type="submit"
          disabled={!address1 || !address2}
          endIcon={<CalculateIcon />} // Add the calculator icon here
        >
          Calculate Distance
        </Button>
      </Box>

      <Snackbar
        open={!!error}
        autoHideDuration={4000}
        onClose={() => setError(null)}
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
      >
        <Alert onClose={() => setError(null)} severity="error" sx={{ width: '100%' }}>
          {error}
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default DistanceForm;
