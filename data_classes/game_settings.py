from dataclasses import dataclass
from typing import Any, List
from pydantic import validate_arguments


@validate_arguments
@dataclass
class GameSettings:
    league_join_private_max: int
    league_join_public_max: int
    league_max_size_public_classic: int
    league_max_size_public_h2h: int
    league_max_size_private_h2h: int
    league_max_ko_rounds_private_h2h: int
    league_prefix_public: str
    league_points_h2h_win: int
    league_points_h2h_lose: int
    league_points_h2h_draw: int
    league_ko_first_instead_of_random: bool
    cup_start_event_id: None
    cup_stop_event_id: None
    cup_qualifying_method: None
    cup_type: None
    squad_squadplay: int
    squad_squadsize: int
    squad_team_limit: int
    squad_total_spend: int
    ui_currency_multiplier: int
    ui_use_special_shirts: bool
    ui_special_shirt_exclusions: List
    stats_form_days: int
    sys_vice_captain_enabled: bool
    transfers_cap: int
    transfers_sell_on_fee: float
    league_h2h_tiebreak_stats: List[str]
    timezone: str
