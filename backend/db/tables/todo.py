import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, Enum, Date, Time, ForeignKey


class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    type = Column(Enum("task", "habit", name="todo_type"), nullable=False)

    date = Column(Date, nullable=False)
    is_all_day = Column(Boolean, default=False)
    alarm_time = Column(Time, nullable=True)

    status = Column(Enum("planned", "done", name="todo_status"), default="planned")
    completed_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="todos")
