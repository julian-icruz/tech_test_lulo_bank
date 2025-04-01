from sqlalchemy import Column, String, Integer

from app.load.domain.models import Base


class Network(Base):
    __tablename__ = "networks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    country_name = Column(String(100), nullable=True)
    country_code = Column(String(10), nullable=True)
    country_timezone = Column(String(50), nullable=True)
    officialSite = Column(String(255), nullable=True)
