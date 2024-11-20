from pydantic_settings import BaseSettings

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

    class Config:
        env_file = ".env"

settings = Settings() 