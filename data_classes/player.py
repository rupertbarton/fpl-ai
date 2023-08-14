from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
from pydantic import validate_arguments


@validate_arguments
@dataclass(eq=True, frozen=True)
class Player:
    chance_of_playing_next_round: Optional[int]
    chance_of_playing_this_round: Optional[int]
    code: int
    cost_change_event: int
    cost_change_event_fall: int
    cost_change_start: int
    cost_change_start_fall: int
    dreamteam_count: int
    element_type: int
    ep_next: str
    ep_this: str
    event_points: int
    first_name: str
    form: float
    id: int
    in_dreamteam: bool
    news: str
    news_added: Optional[datetime]
    now_cost: int
    photo: str
    points_per_game: float
    second_name: str
    selected_by_percent: float
    special: bool
    squad_number: None
    status: str
    team: int
    team_code: int
    total_points: int
    transfers_in: int
    transfers_in_event: int
    transfers_out: int
    transfers_out_event: int
    value_form: float
    value_season: float
    web_name: str
    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: float
    creativity: float
    threat: float
    ict_index: float
    starts: int
    expected_goals: float
    expected_assists: float
    expected_goal_involvements: float
    expected_goals_conceded: float
    influence_rank: int
    influence_rank_type: int
    creativity_rank: int
    creativity_rank_type: int
    threat_rank: int
    threat_rank_type: int
    ict_index_rank: int
    ict_index_rank_type: int
    corners_and_indirect_freekicks_order: Optional[int]
    corners_and_indirect_freekicks_text: str
    direct_freekicks_order: Optional[int]
    direct_freekicks_text: str
    penalties_order: Optional[int]
    penalties_text: str
    expected_goals_per_90: float
    saves_per_90: float
    expected_assists_per_90: float
    expected_goal_involvements_per_90: float
    expected_goals_conceded_per_90: float
    goals_conceded_per_90: float
    now_cost_rank: int
    now_cost_rank_type: int
    form_rank: int
    form_rank_type: int
    points_per_game_rank: int
    points_per_game_rank_type: int
    selected_rank: int
    selected_rank_type: int
    starts_per_90: float
    clean_sheets_per_90: float

    @property
    def cost_efficiency(self):
        if self.points_per_game and self.now_cost:
            return self.points_per_game / self.now_cost
        else:
            return 0

    def format_name(self):
        return f"{self.second_name}, {self.first_name}: £{self.now_cost/10} | Points: {self.total_points}"