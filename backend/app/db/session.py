from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from backend.app.core.config import settings


engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """Classe de base des modèles SQLAlchemy."""


def get_db():
    """Fournit une session de base de données à une route API."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()