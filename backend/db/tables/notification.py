import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, Enum, ForeignKey


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    todo_id = Column(Integer, ForeignKey("todos.id"), nullable=True)

    notification_time = Column(DateTime, nullable=False)
    status = Column(Enum("scheduled", "sent", name="notif_status"), default="scheduled")

    created_at = Column(DateTime, default=datetime.utcnow)
