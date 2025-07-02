from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from . import settings


if settings.DB_URL.startswith("sqlite:/"):
    engine = create_engine(settings.DB_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(engine, autoflush=False, autocimmit=False)
Base = declarative_base()
