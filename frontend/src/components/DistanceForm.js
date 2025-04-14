import React from 'react';
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
  Grid,
} from '@mui/material';
import CalculateIcon from '@mui/icons-material/Calculate';
import { useDistanceForm } from '../hooks/useDistanceForm';
import DistanceInput from './DistanceInput';

function DistanceForm() {
  const {
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
  } = useDistanceForm();

  return (
    <Box component="form" onSubmit={handleSubmit} mt={2}>
      <Grid container spacing={3} alignItems="flex-start">
        <Grid item xs={12} md={3}>
          <DistanceInput
            label="Source Address"
            value={address1}
            onChange={(e) => setAddress1(e.target.value)}
          />
        </Grid>

        <Grid item xs={12} md={3}>
          <DistanceInput
            label="Destination Address"
            value={address2}
            onChange={(e) => setAddress2(e.target.value)}
          />
        </Grid>

        <Grid item xs={12} md={3}>
          <FormControl component="fieldset">
            <FormLabel>Unit</FormLabel>
            <RadioGroup value={unit} onChange={(e) => setUnit(e.target.value)}>
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
          endIcon={<CalculateIcon />}
        >
          Calculate Distance
        </Button>
      </Box>

      <Snackbar
        open={!!error}
        autoHideDuration={4000}
        onClose={() => setError(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
      >
        <Alert
          onClose={() => setError(null)}
          severity="error"
          sx={{ width: '100%' }}
          action={
            <Button color="inherit" size="small" onClick={() => setError(null)}>
              X
            </Button>
          }
        >
          <strong>Calculation Failed</strong><br />
          Something went wrong and the calculation failed.
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default DistanceForm;
