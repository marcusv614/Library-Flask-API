from sqlalchemy.dialects.postgresql import UUID,TEXT
from sqlalchemy import func
from db import db

class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=func.uuid_generate_v4())
