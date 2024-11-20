from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse

router = APIRouter()

@router.put("/{transaction_id}", response_model=TransactionResponse)
def create_transaction(
    transaction_id: int,
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    db_transaction = Transaction(id=transaction_id, **transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/{transaction_id}", response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/types/{type}", response_model=List[int])
def get_transactions_by_type(type: str, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.type == type).all()
    return [transaction.id for transaction in transactions]

@router.get("/sum/{transaction_id}")
def get_sum(transaction_id: int, db: Session = Depends(get_db)):
    def calculate_sum(trans_id: int) -> float:
        total_sum = 0.0
        current_transaction = db.query(Transaction).filter(Transaction.id == trans_id).first()
        if current_transaction:
            total_sum += current_transaction.amount
            children = db.query(Transaction).filter(Transaction.parent_id == trans_id).all()
            for child in children:
                total_sum += calculate_sum(child.id)
        return total_sum
    
    return {"sum": calculate_sum(transaction_id)} 