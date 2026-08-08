# from fastapi import FastAPI

# from app.core.config import settings

# app = FastAPI(
#     title=settings.app_name,
#     version=settings.app_version,
# )
# print("Configuration loaded successfully.")

from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/health")
async def root():
    return {"status": "ok"}

logger.info("Application startup complete")