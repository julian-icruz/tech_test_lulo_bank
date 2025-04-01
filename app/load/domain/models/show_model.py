from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Text,
    ForeignKey,
    Date,
    DateTime,
    BigInteger,
)

from app.load.domain.models import Base


class Show(Base):
    __tablename__ = "shows"

    id = Column(BigInteger, primary_key=True, index=True)
    url = Column(String(255), nullable=True)
    name = Column(String(100), nullable=True)
    type = Column(String(50), nullable=True)
    language = Column(String(50), nullable=True)
    genres = Column(ARRAY(String), nullable=True)
    status = Column(String(50), nullable=True)
    averageruntime = Column(Integer, nullable=True)
    premiered = Column(Date, nullable=True)
    ended = Column(Date, nullable=True)
    officialsite = Column(String(255), nullable=True)
    weight = Column(Integer, nullable=True)
    updated = Column(DateTime, nullable=True)
    time = Column(String(50), nullable=True)
    days = Column(ARRAY(String), nullable=True)
    webchannel_id = Column(Integer, ForeignKey("web_channels.id"), nullable=True)
    medium = Column(String(255), nullable=True)
    original = Column(String(255), nullable=True)
    links_self_href = Column(String(255), nullable=True)
    links_previousepisode_href = Column(String(255), nullable=True)
    links_previousepisode_name = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)
    thetvdb = Column(BigInteger, nullable=True)
    runtime = Column(Integer, nullable=True)
    network_id = Column(Integer, ForeignKey("networks.id"), nullable=True)
    imdb = Column(String(100), nullable=True)
    average = Column(Float, nullable=True)
    tvrage = Column(BigInteger, nullable=True)
    links_nextepisode_href = Column(String(255), nullable=True)
    links_nextepisode_name = Column(String(255), nullable=True)
