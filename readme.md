# Transaction Service

A RESTful service for managing financial transactions built with FastAPI and PostgreSQL.

## 🚀 Features

- Create and retrieve transactions
- Link transactions through parent-child relationships
- Query transactions by type
- Calculate transaction sums including linked transactions
- Containerized with Docker for easy deployment

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Pydantic
- Pytest

## 🏃‍♂️ Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.12+

### Installation

1. Clone the repository
2. Run the application using Docker Compose:

```bash
docker-compose up --build
```

The services will be available at:
- API: `http://localhost:8000`
- Adminer (Database UI): `http://localhost:8080`
- PostgreSQL: `localhost:5433`

## 🔑 Environment Variables

The application uses the following environment variables (defined in config.py):

```python
class Settings(BaseSettings):
    PROJECT_NAME: str = "Transaction Service"
    VERSION: str = "1.0.0"
    API_V1_STR: str = ""
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgrespass"
    POSTGRES_DB: str = "transaction_db"
    POSTGRES_HOST: str = "database"
    POSTGRES_PORT: str = "5432"
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
```

## 📡 API Endpoints

### Create Transaction
```http
PUT /transactionservice/transaction/{transaction_id}
```

Request body:
```json
{
    "amount": 5000,
    "type": "cars",
    "parent_id": null
}
```

### Get Transaction
```http
GET /transactionservice/transaction/{transaction_id}
```

### Get Transactions by Type
```http
GET /transactionservice/types/{type}
```

### Get Transaction Sum
```http
GET /transactionservice/sum/{transaction_id}
```

## 🧪 Testing

The project includes test cases that demonstrate the API functionality. To run the tests:

```bash
python -m pytest test/test_api.py
```

## 🐳 Docker Configuration

The application is containerized using three services:
1. FastAPI application
2. PostgreSQL database
3. Adminer for database management

## 📦 Dependencies

All required Python packages are listed in requirements.txt:

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
pytest
httpx
sqlalchemy
python-dotenv
pydantic_settings
```

## 🏗️ Project Structure

```
.
├── app/
│   ├── api/
│   │   └── endpoints/
│   ├── core/
│   ├── db/
│   ├── models/
│   └── schemas/
├── test/
├── docker-compose.yml
└── Dockerfile
```

## 📝 License

This project is licensed under the MIT License.

---

For more information or contributions, please open an issue or submit a pull request.
