from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.session import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("transactions.id"), nullable=True) 