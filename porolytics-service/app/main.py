from typing import List

from config import REGIONS
from fastapi import FastAPI, HTTPException, Path, Query

from app import schemas
from app.crud import matches, account, stats

app = FastAPI() 


def check_region(region: str):
    if region not in REGIONS:
        raise HTTPException(status_code=404, detail="Region not found")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Porolytics API"}


@app.get(
    "/players/{region}/account/{game_name}/{tag_line}", response_model=schemas.AccountDto
)
def get_account_by_riot_id(
    region: str = Path(..., description="The player's region.", example="na"),
    game_name: str = Path(..., description="The player's game name.", example="Boober"),
    tag_line: str = Path(..., description="The player's tag line.", example="NA1"),
):
    """
    Get account details by Riot ID (gameName and tagLine).
    """
    check_region(region)
    try:
        return account.get_account_by_riot_id(region, game_name, tag_line)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    "/players/{region}/match-history/{game_name}/{tag_line}",
    response_model=List[schemas.Match],
)
def get_match_history(
    region: str = Path(..., description="The player's region.", example="na"),
    game_name: str = Path(..., description="The player's game name.", example="Boober"),
    tag_line: str = Path(..., description="The player's tag line.", example="NA1"),
    start: int = Query(0, ge=0, description="The starting index of the match history."),
    count: int = Query(
        20, ge=1, le=100, description="The number of matches to retrieve."
    ),
):
    """
    Get the match history for a player.
    """
    check_region(region)
    try:
        return matches.get_player_match_history(region, game_name, tag_line, start, count)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    "/players/{region}/win-rate/{game_name}/{tag_line}", response_model=schemas.WinRate
)
def get_win_rate(
    region: str = Path(..., description="The player's region.", example="na"),
    game_name: str = Path(..., description="The player's game name.", example="Boober"),
    tag_line: str = Path(..., description="The player's tag line.", example="NA1"),
    count: int = Query(
        20, ge=1, le=100, description="The number of matches to consider."
    ),
):
    """
    Calculate the win rate for a player based on recent matches.
    """
    check_region(region)
    try:
        match_history = matches.get_player_match_history(
            region, game_name, tag_line, 0, count
        )
        return stats.calculate_win_rate(match_history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    "/players/{region}/player-stats/{game_name}/{tag_line}",
    response_model=schemas.PlayerStats,
)
def get_player_stats(
    region: str = Path(..., description="The player's region.", example="na"),
    game_name: str = Path(..., description="The player's game name.", example="Boober"),
    tag_line: str = Path(..., description="The player's tag line.", example="NA1"),
    count: int = Query(
        20, ge=1, le=100, description="The number of matches to consider."
    ),
):
    """
    Calculate player stats (KDA, GPM, DPM) based on recent matches.
    """
    check_region(region)
    try:
        match_history = matches.get_player_match_history(
            region, game_name, tag_line, 0, count
        )
        return stats.calculate_player_stats(match_history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
