from app import schemas


def calculate_win_rate(matches: list[schemas.Match]) -> schemas.WinRate:
    """
    Calculate the win rate from a list of matches.
    """
    if not matches:
        return schemas.WinRate(win_rate="0.00%")

    wins = sum(1 for match in matches if match.win)
    total_games = len(matches)
    win_rate = (wins / total_games) * 100
    return schemas.WinRate(win_rate=f"{win_rate:.2f}%")


def calculate_player_stats(matches: list[schemas.Match]) -> schemas.PlayerStats:
    """
    Calculate average KDA, GPM, and DPM from a list of matches.
    """
    if not matches:
        return schemas.PlayerStats(
            average_kda="0/0/0", average_gpm=0.0, average_dpm=0.0
        )

    total_kills = sum(match.kills for match in matches)
    total_deaths = sum(match.deaths for match in matches)
    total_assists = sum(match.assists for match in matches)
    total_gold = sum(match.gold_earned for match in matches)
    total_damage = sum(match.total_damage_dealt_to_champions for match in matches)
    total_duration_minutes = sum(match.game_duration / 60 for match in matches)
    num_matches = len(matches)

    avg_kills = total_kills / num_matches
    avg_deaths = total_deaths / num_matches
    avg_assists = total_assists / num_matches

    # Avoid division by zero
    if total_duration_minutes > 0:
        avg_gpm = total_gold / total_duration_minutes
        avg_dpm = total_damage / total_duration_minutes
    else:
        avg_gpm = 0.0
        avg_dpm = 0.0

    # Format KDA as a string "K/D/A"
    kda_str = f"{avg_kills:.2f}/{avg_deaths:.2f}/{avg_assists:.2f}"

    return schemas.PlayerStats(
        average_kda=kda_str,
        average_gpm=round(avg_gpm, 2),
        average_dpm=round(avg_dpm, 2),
    )
