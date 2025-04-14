import React from 'react';
import { TextField, FormLabel } from '@mui/material';

function DistanceInput({ label, value, onChange }) {
return (
    <>
        <FormLabel>{label}</FormLabel>
        <TextField
            fullWidth
            variant="filled"
            value={value}
            onChange={onChange}
            helperText="Enter a valid location"
            sx={{
                backgroundColor: '#f9f9f9',
            }}
        />
    </>
);
}

export default DistanceInput;