@echo off
title OBSIZEN Launcher

echo =========================================
echo         OBSIZEN - Starting Servers
echo =========================================
echo.

:: Start FastAPI backend in a new window
echo [1/2] Starting FastAPI backend on http://127.0.0.1:8000 ...
start "OBSIZEN - Backend" cmd /k "cd /d %~dp0 && myvenv\Scripts\python.exe -m uvicorn src.server:app --host 127.0.0.1 --port 8000"

:: Brief pause to let the backend process spawn
timeout /t 2 /nobreak >nul

:: Start Vite frontend dev server in a new window
echo [2/2] Starting React frontend on http://localhost:5173 ...
start "OBSIZEN - Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo =========================================
echo  Both servers are starting up!
echo  Backend  : http://127.0.0.1:8000
echo  Frontend : http://localhost:5173
echo  (Note: first chat request loads ML models
echo   and may take 30-60s)
echo =========================================
echo.
echo Press any key to open the app in your browser...
pause >nul

start http://localhost:5173
