import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import theme from './theme'; // Import the theme from theme.js
import 'bootstrap/dist/css/bootstrap.min.css';
// ErrorBoundary is a custom component that catches JavaScript errors anywhere in its child component tree,
// logs those errors, and displays a fallback UI instead of crashing the whole app.
import ErrorBoundary from './components/ErrorBoundary'; // Import the ErrorBoundary

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <ErrorBoundary>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <App />
            </ThemeProvider>
        </ErrorBoundary>
    </React.StrictMode>
);

reportWebVitals();
