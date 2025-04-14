import React, { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  TablePagination,
  Button,
} from '@mui/material';
import CalculateIcon from '@mui/icons-material/Calculate';
import { useNavigate } from 'react-router-dom';
import fetchHistory from '../api_endpoints/history_endpoint'; // Import the API function

function History() {
  const [historyData, setHistoryData] = useState([]);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [totalRows, setTotalRows] = useState(0);
  const navigate = useNavigate();

  useEffect(() => {
    const loadHistory = async () => {
      try {
        const data = await fetchHistory(page, rowsPerPage);
        setHistoryData(data.results);
        setTotalRows(data.total_count); // Use total_count from the API response
      } catch (error) {
        console.error('Error loading history:', error);
      }
    };

    loadHistory();
  }, [page, rowsPerPage]);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0); // Reset to the first page
  };

  return (
    <Box sx={{ mt: 6, px: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={4}>
        <Typography variant="h4" component="h1">
          Distance Calculator
        </Typography>
        <Button
          variant="contained"
          color="secondary"
          startIcon={<CalculateIcon />}
          onClick={() => navigate('/')}
        >
          Back to Calculator
        </Button>
      </Box>

      <Paper elevation={3} sx={{ p: 4, borderRadius: 2 }}>
        <Typography variant="h6" gutterBottom>
          Historical Queries
        </Typography>
        <Typography variant="body2" color="text.secondary" gutterBottom>
          History of the user's queries.
        </Typography>

        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Source Address</TableCell>
                <TableCell>Destination Address</TableCell>
                <TableCell>Distance in Miles</TableCell>
                <TableCell>Distance in Kilometers</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {historyData.map((row) => (
                <TableRow key={row.id}>
                  <TableCell>{row.address1}</TableCell> {/* Use address1 */}
                  <TableCell>{row.address2}</TableCell> {/* Use address2 */}
                  <TableCell>{row.distance.toFixed(2)}</TableCell> {/* Use distance */}
                  <TableCell>{(row.distance * 1.60934).toFixed(2)}</TableCell> {/* Convert to kilometers */}
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>

        <TablePagination
          component="div"
          count={totalRows}
          page={page}
          onPageChange={handleChangePage}
          rowsPerPage={rowsPerPage}
          onRowsPerPageChange={handleChangeRowsPerPage}
          rowsPerPageOptions={[5, 10, 25]}
        />
      </Paper>
    </Box>
  );
}

export default History;