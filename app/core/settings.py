from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str
    secret_key: str
    debug: bool = True

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = {
        "env_file": ".env",
        "from_attributes": True,
        "extra": "forbid"
    }

settings = Settings()
