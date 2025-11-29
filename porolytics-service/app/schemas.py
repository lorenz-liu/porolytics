from typing import Optional

from pydantic import BaseModel


class SummonerDTO(BaseModel):
    profile_icon_id: int
    revision_date: int
    puuid: str
    summoner_level: int


class Match(BaseModel):
    match_id: str
    game_creation: int
    game_duration: int
    win: bool
    kills: int
    deaths: int
    assists: int
    gold_earned: int
    total_damage_dealt_to_champions: int


class PlayerStats(BaseModel):
    average_kda: str
    average_gpm: float
    average_dpm: float


class WinRate(BaseModel):
    win_rate: str


class AccountDto(BaseModel):
    puuid: str
    gameName: Optional[str] = None
    tagLine: Optional[str] = None
