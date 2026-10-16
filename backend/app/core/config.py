from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DocuMind AI"
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    app_secret_key: str = "development-only-change-me"

    database_url: str = (
        "postgresql+psycopg://documind_user:CHANGE_ME"
        "@localhost:5432/documind_db"
    )

    max_upload_size_mb: int = 15
    allowed_extensions: str = ".pdf,.png,.jpg,.jpeg"
    upload_dir: str = "storage/uploads"
    frontend_origin: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()
