from sqlalchemy import Column, Integer, String
from backend.db.base import Base


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    also_text = Column(String, index=True)
