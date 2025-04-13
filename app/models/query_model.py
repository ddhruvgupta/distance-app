from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class DistanceQuery(Base):
    __tablename__ = "distance_queries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address1 = Column(String(255), nullable=False)
    address2 = Column(String(255), nullable=False)
    distance = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())