from fastapi import FastAPI
from app.api.endpoints import transactions
from app.core.config import settings
from app.db.session import Base
from app.db.session import engine

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(
    transactions.router,
    prefix="/transactionservice/transaction",
    tags=["transactions"]
) 