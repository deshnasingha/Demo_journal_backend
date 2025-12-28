import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, Enum



class Affirmation(Base):
    __tablename__ = "affirmations"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    time_period = Column(Enum("morning", "afternoon", "evening", "night",
                              name="time_period_enum"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)