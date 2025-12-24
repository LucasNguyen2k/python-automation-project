from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    BASE_URL: str = "https://api.coingecko.com/api/v3"
    TIMEOUT: int = 10

settings = Settings()
