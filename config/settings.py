from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    google_api_key: str
    redis_host: str
    redis_port: int
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
