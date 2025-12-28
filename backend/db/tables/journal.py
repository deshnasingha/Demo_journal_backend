import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, Enum, ForeignKey



class Journal(Base):
    __tablename__ = "journals"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    content = Column(Text, nullable=False)
    mood1 = Column(String(50))
    mood2 = Column(String(50))
    mood3 = Column(String(50))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="journals")
