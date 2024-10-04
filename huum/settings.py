from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    huum_username: Optional[str]
    huum_password: Optional[str]


settings = Settings()
