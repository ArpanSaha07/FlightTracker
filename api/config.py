from pydantic import BaseSettings

class Settings(BaseSettings):
    ROOT_URL: str           # attribute

settings = Settings()