from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    POSTGRES_DB: str = "db_postgres"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432

    MYSQL_DB: str = "db_mysql"
    MYSQL_USER: str = "admin"
    MYSQL_PASSWORD: str = "password"
    MYSQL_HOST: str = "mysql"
    MYSQL_PORT: int = 3306
