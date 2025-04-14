import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  TablePagination,
} from '@mui/material';

function HistoryTable({
  historyData,
  totalRows,
  page,
  rowsPerPage,
  handleChangePage,
  handleChangeRowsPerPage,
}) {
  return (
    <Paper elevation={3} sx={{ p: 4, borderRadius: 2 }}>
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
        onPageChange={handleChangePage}
        rowsPerPage={rowsPerPage}
        onRowsPerPageChange={handleChangeRowsPerPage}
        rowsPerPageOptions={[5, 10, 25]}
      />
    </Paper>
  );
}

export default HistoryTable;