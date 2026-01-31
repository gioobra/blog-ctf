import fastapi
import models
from .database import SessionLocal
from .database import engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)
app = fastapi()