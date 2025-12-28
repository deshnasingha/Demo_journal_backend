import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, ForeignKey



class UserAffirmation(Base):
    __tablename__ = "user_affirmations"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    affirmation_id = Column(Integer, ForeignKey("affirmations.id"), nullable=False)

    displayed_at = Column(DateTime, default=datetime.utcnow)
    note = Column(Text, nullable=True)

    user = relationship("User")
    affirmation = relationship("Affirmation")