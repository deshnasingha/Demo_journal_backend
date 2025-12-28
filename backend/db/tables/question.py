import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)
    question_order = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    # options = relationship("QuestionOption", back_populates="question")