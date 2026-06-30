import axios from 'axios';

// Create a base axios instance. 
// In the future this will point to the actual FastAPI backend (e.g., http://localhost:8000)
export const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// We can add interceptors here later if needed for auth or error handling
