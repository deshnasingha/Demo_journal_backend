import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, Enum



class MoodKeyword(Base):
    __tablename__ = "mood_keywords"

    id = Column(Integer, primary_key=True)
    keyword = Column(String(100), nullable=False)

