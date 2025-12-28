import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, ForeignKey



class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    
    free_text = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="answers")
    question = relationship("Question")
    # option = relationship("QuestionOption")