# We'll centralize environment variables here instead of scattering os.getenv() throughout the project.
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_version: str
    environment: str
    database_url: str
    secret_key: str

    debug: bool = False
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
)
settings = Settings()