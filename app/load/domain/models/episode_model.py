from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Text,
    ForeignKey,
    Date,
    Time,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=True)
    name = Column(String(150), nullable=True)
    season = Column(Integer, nullable=True)
    number = Column(Integer, nullable=True)
    type = Column(String(50), nullable=True)
    airdate = Column(Date, nullable=True)
    airtime = Column(Time, nullable=True)
    airstamp = Column(DateTime, nullable=True)
    runtime = Column(Float, nullable=True)
    rating = Column(Float, nullable=True)
    summary = Column(Text, nullable=True)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
