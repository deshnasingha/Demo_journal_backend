import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from backend.db.enginedb import Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Boolean, Enum, ForeignKey


class ZenSettings(Base):
    __tablename__ = "zen_settings"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    natural_sounds_enabled = Column(Boolean, default=False)
    last_mode = Column(Enum("morning", "afternoon", "evening", "night",
                            name="zen_mode"), nullable=True)

    updated_at = Column(DateTime, default=datetime.utcnow)
