import requests
from config import REGIONS, settings

from app import schemas

from . import account


def get_match_ids(
    region: str, puuid: str, start: int = 0, count: int = 20
) -> list[str]:
    """
    Get a list of match IDs for a given PUUID.
    """
    regional = REGIONS[region]["regional"]
    url = f"https://{regional}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
    headers = {"X-Riot-Token": settings.RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_match_details(region: str, match_id: str, puuid: str) -> schemas.Match:
    """
    Get the details of a single match
    """
    regional = REGIONS[region]["regional"]
    url = f"https://{regional}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": settings.RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    with open("/Users/niuniu/Desktop/match.txt", "w") as f:
        print(data, file=f)

    participant_index = data["metadata"]["participants"].index(puuid)
    participant_data = data["info"]["participants"][participant_index]

    return schemas.Match(
        match_id=match_id,
        game_creation=data["info"]["gameCreation"],
        game_duration=data["info"]["gameDuration"],
        win=participant_data["win"],
        kills=participant_data["kills"],
        deaths=participant_data["deaths"],
        assists=participant_data["assists"],
        gold_earned=participant_data["goldEarned"],
        total_damage_dealt_to_champions=participant_data["totalDamageDealtToChampions"],
    )


def get_player_match_history(
    region: str, game_name: str, tag_line: str, start: int = 0, count: int = 20
) -> list[schemas.Match]:
    """
    Get the match history for a player.
    """
    acc = account.get_account_by_riot_id(region, game_name, tag_line)
    puuid = acc.puuid
    match_ids = get_match_ids(region, puuid, start, count)

    matches = []
    for match_id in match_ids:
        try:
            match_details = get_match_details(region, match_id, puuid)
            matches.append(match_details)
        except requests.HTTPError as e:
            # Log the error or handle it as needed
            print(f"Error fetching details for match {match_id}: {e}")
            continue  # Or skip this match

    return matches
