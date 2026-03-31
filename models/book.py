from sqlalchemy.dialects.postgresql import UUID,TEXT
from sqlalchemy import func
from db import db

class Book(db.Model):
    __tablename__ = "book"
    
