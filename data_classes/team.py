from dataclasses import dataclass
from typing import Any
from pydantic import validate_arguments


@validate_arguments
@dataclass
class Team:
    code: int
    draw: int
    form: None
    id: int
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: None
    unavailable: bool
    win: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int
    pulse_id: int
