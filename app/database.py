from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: we need to change to hide string connection
SQLALCHEMY_ENDPOINT = "postgresql://admin:123qwe@db/fastapi"

engine = create_engine(SQLALCHEMY_ENDPOINT)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
