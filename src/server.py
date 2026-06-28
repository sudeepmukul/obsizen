from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.chat import router as chat_router
from src.api.routes.health import router as health_router

app = FastAPI(
    title="OBSIZEN API",
    version="1.6.0"
)

# Allow React frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    chat_router,
    prefix="/api"
)