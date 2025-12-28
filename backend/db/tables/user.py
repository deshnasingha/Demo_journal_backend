import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    temp_password = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships
    
    answers = relationship("UserAnswer", back_populates="user")
    journals = relationship("Journal", back_populates="user")
    todos = relationship("ToDo", back_populates="user")
    session_tokens = relationship("SessionToken", back_populates="user")
    profile = relationship("Profile", back_populates="user", uselist=False)

