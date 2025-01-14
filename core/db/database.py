from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.settings import settings

engine = create_engine(settings.BATABASE_URL, future=False)
session: Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
