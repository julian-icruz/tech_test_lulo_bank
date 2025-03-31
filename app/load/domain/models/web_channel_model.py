from sqlalchemy import Column, String, Integer

from app.load.domain.models import Base


class WebChannel(Base):
    __tablename__ = "web_channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    country_name = Column(String(100), nullable=True)
    country_code = Column(String(10), nullable=True)
    country_timezone = Column(String(50), nullable=True)
    officialSite = Column(String(255), nullable=True)
