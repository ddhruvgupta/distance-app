import React from 'react';
import { Box, Grid, Typography, Button, Paper } from '@mui/material';
import HistoryIcon from '@mui/icons-material/History';
import DistanceForm from '../components/DistanceForm';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

function Home() {
  const navigate = useNavigate(); // Initialize the navigate function

  return (
    <Box sx={{ mt: 6, px: 4 }}>
      <Paper elevation={3} sx={{ p: 4, borderRadius: 2 }}>
        <Grid container justifyContent="space-between" alignItems="center" spacing={2}>
          <Grid item xs={12} md={8}>
            <Typography variant="h4" component="h1" gutterBottom>
              Distance Calculator
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Prototype web application for calculating the distance between addresses.
            </Typography>
          </Grid>
          <Grid item xs={12} md="auto">
            <Button
              variant="contained"
              color="secondary"
              startIcon={<HistoryIcon />}
              onClick={() => navigate('/history')} // Navigate to the History page
            >
              View Historical Queries
            </Button>
          </Grid>
        </Grid>

        <Box mt={4}>
          <DistanceForm />
        </Box>
      </Paper>
    </Box>
  );
}

export default Home;
