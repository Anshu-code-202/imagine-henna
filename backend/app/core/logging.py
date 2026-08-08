# Even if it only contains basic logging initially, having a dedicated place for logging keeps the architecture clean.
# app/core/logging.py
import logging
from app.core.config import settings

def setup_logging():
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )