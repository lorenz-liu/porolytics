import requests
from config import REGIONS, settings

from app import schemas


def get_summoner_data_by_puuid(region: str, puuid: str) -> schemas.SummonerDTO:
    """
    Get summoner data by PUUID.
    """
    platform = REGIONS[region]["platform"]
    url = f"https://{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    headers = {"X-Riot-Token": settings.RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return schemas.SummonerDTO(**data)


def get_account_by_riot_id(
    region: str, game_name: str, tag_line: str
) -> schemas.AccountDto:
    """
    Get account details by Riot ID (gameName and tagLine).
    """
    regional = REGIONS[region]["regional"]
    url = f"https://{regional}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": settings.RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print("=============== DATA ======================\n", data)
    return schemas.AccountDto(**data)
