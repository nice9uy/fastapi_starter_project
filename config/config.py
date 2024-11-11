from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI : str
    MONGODB_DATABASE: str

    class Config:
        env_file = ".env.development" 

settings = Settings()