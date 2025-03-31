from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey, Date, DateTime

Base = declarative_base()


class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=True)
    name = Column(String(100), nullable=True)
    type = Column(String(50), nullable=True)
    language = Column(String(50), nullable=True)
    genres = Column(ARRAY(String), nullable=True)
    status = Column(String(50), nullable=True)
    averageRuntime = Column(Float, nullable=True)
    premiered = Column(Date, nullable=True)
    ended = Column(Date, nullable=True)
    officialSite = Column(String(255), nullable=True)
    weight = Column(Integer, nullable=True)
    updated = Column(DateTime, nullable=True)
    time = Column(String(50), nullable=True)
    days = Column(String(100), nullable=True)
    web_channel_id = Column(Float, ForeignKey("web_channels.id"), nullable=True)
    medium = Column(String(255), nullable=True)
    original = Column(String(255), nullable=True)
    links_self_href = Column(String(255), nullable=True)
    links_previousepisode_href = Column(String(255), nullable=True)
    links_previousepisode_name = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)
    thetvdb = Column(Float, nullable=True)
    runtime = Column(Float, nullable=True)
    id_2 = Column(Float, nullable=True)
    name_1 = Column(String(100), nullable=True)
    country_name = Column(String(100), nullable=True)
    country_code = Column(String(10), nullable=True)
    country_timezone = Column(String(50), nullable=True)
    officialSite_1 = Column(String(255), nullable=True)
    imdb = Column(String(100), nullable=True)
    average = Column(Float, nullable=True)
    tvrage = Column(Float, nullable=True)
    links_nextepisode_href = Column(String(255), nullable=True)
    links_nextepisode_name = Column(String(255), nullable=True)
