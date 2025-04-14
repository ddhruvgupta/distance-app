import React, { Component } from 'react';
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
import fetchHistory from '../api_endpoints/history_endpoint';
import withNavigation from '../utils/withNavigation';

class History extends Component {
  constructor(props) {
    super(props);
    this.state = {
      historyData: [],
      page: 0,
      rowsPerPage: 10,
      totalRows: 0,
    };
  }

  componentDidMount() {
    this.loadHistory();
  }

  componentDidUpdate(prevProps, prevState) {
    if (
      prevState.page !== this.state.page ||
      prevState.rowsPerPage !== this.state.rowsPerPage
    ) {
      this.loadHistory();
    }
  }

  async loadHistory() {
    const { page, rowsPerPage } = this.state;
    try {
      const data = await fetchHistory(page, rowsPerPage);
      this.setState({
        historyData: data.results,
        totalRows: data.total_count,
      });
    } catch (error) {
      console.error('Error loading history:', error);
    }
  }

  handleChangePage = (event, newPage) => {
    this.setState({ page: newPage });
  };

  handleChangeRowsPerPage = (event) => {
    this.setState({
      rowsPerPage: parseInt(event.target.value, 10),
      page: 0, // Reset to the first page
    });
  };

  navigateToCalculator = () => {
    this.props.navigate('/'); // Use the injected `navigate` function
  };

  render() {
    const { historyData, page, rowsPerPage, totalRows } = this.state;

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
            onClick={this.navigateToCalculator}
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
                    <TableCell>{row.address1}</TableCell>
                    <TableCell>{row.address2}</TableCell>
                    <TableCell>{row.distance.toFixed(2)}</TableCell>
                    <TableCell>{(row.distance * 1.60934).toFixed(2)}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>

          <TablePagination
            component="div"
            count={totalRows}
            page={page}
            onPageChange={this.handleChangePage}
            rowsPerPage={rowsPerPage}
            onRowsPerPageChange={this.handleChangeRowsPerPage}
            rowsPerPageOptions={[5, 10, 25]}
          />
        </Paper>
      </Box>
    );
  }
}

export default withNavigation(History);