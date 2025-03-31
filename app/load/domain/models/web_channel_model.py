from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WebChannel(Base):
    __tablename__ = "web_channels"

    id = Column(Float, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    country_name = Column(String(100), nullable=True)
    country_code = Column(String(10), nullable=True)
    country_timezone = Column(String(50), nullable=True)
    officialSite = Column(String(255), nullable=True)
