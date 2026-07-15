import axios from 'axios';

// Axios instance pointing to the FastAPI backend
export const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 120000, // 120s — first request loads ML models, which can be slow
});
