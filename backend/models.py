from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Attack(Base):
    __tablename__ = "attacks"
    
    id = Column(Integer, primary_key=True)
    technique_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    target = Column(String)
    status = Column(String, default="PENDING")

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True)
    wazuh_alert_id = Column(String, unique=True)
    rule = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    technique_id = Column(String, index=True)
