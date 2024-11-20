from pydantic import BaseModel, Field
from typing import Optional

class TransactionBase(BaseModel):
    amount: float = Field(..., description="Transaction amount")
    type: str = Field(..., description="Transaction type")
    parent_id: Optional[int] = Field(None, description="Parent transaction ID")

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True 