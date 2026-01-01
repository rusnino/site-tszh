from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "TSZH MVP"
    environment: str = "development"

    db_host: str = "db"
    db_port: int = 5432
    db_name: str = "tszh"
    db_user: str = "tszh"
    db_password: str = "tszh"

    jwt_secret: str = "change_me"
    jwt_algorithm: str = "HS256"
    access_token_exp_minutes: int = 30
    refresh_token_exp_days: int = 7

    cors_origins: str = "http://localhost:5173"

    rate_limit: str = "10/minute"

    class Config:
        env_file = ".env"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
