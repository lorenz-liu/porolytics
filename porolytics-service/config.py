from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    RIOT_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()

REGIONS = {
    "br": {"platform": "br1", "regional": "americas"},
    "eune": {"platform": "eun1", "regional": "europe"},
    "euw": {"platform": "euw1", "regional": "europe"},
    "jp": {"platform": "jp1", "regional": "asia"},
    "kr": {"platform": "kr", "regional": "asia"},
    "lan": {"platform": "la1", "regional": "americas"},
    "las": {"platform": "la2", "regional": "americas"},
    "na": {"platform": "na1", "regional": "americas"},
    "oce": {"platform": "oc1", "regional": "americas"},
    "tr": {"platform": "tr1", "regional": "europe"},
    "ru": {"platform": "ru", "regional": "europe"},
    "ph": {"platform": "ph2", "regional": "sea"},
    "sg": {"platform": "sg2", "regional": "sea"},
    "th": {"platform": "th2", "regional": "sea"},
    "tw": {"platform": "tw2", "regional": "sea"},
    "vn": {"platform": "vn2", "regional": "sea"},
}
