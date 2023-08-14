from dataclasses import dataclass
from typing import Any, List
from pydantic import validate_arguments
from data_classes.game_settings import GameSettings

from data_classes.player import Player
from data_classes.position import Position


class FantasyTeam:
    goalkeepers: set[Player]
    defenders: set[Player]
    midfielders: set[Player]
    forwards: set[Player]
    game_settings: GameSettings

    def __init__(self, game_settings: GameSettings):
        self.goalkeepers = set()
        self.defenders = set()
        self.midfielders = set()
        self.forwards = set()
        self.game_settings = game_settings

    @property
    def all_players(self) -> List[Player]:
        return (
            self.goalkeepers
            .union(self.defenders)
            .union(self.midfielders)
            .union(self.forwards)
        )
    
    @property
    def size(self) -> int:
        return len(self.all_players)
    
    @property
    def cost(self):
        return sum([player.now_cost for player in self.all_players])
    
    @property
    def total_points(self):
        return sum([player.total_points for player in self.all_players])

    def add_player(self, player: Player, position: Position):
        max_size = self.game_settings.squad_squadsize
        if self.size < max_size:
            current_player_list = (
                self.goalkeepers,
                self.defenders,
                self.midfielders,
                self.forwards,
            )[position.id - 1]
            if len(current_player_list) < position.squad_select:
                current_player_list.add(player)
            else:
                raise Exception(
                    f"Fantasy team size cannot exceed more than {position.squad_select} {position.plural_name}"
                )

        else:
            raise Exception(
                f"Fantasy team size cannot exceed more than {max_size} players"
            )

    def force_add_player(self, player: Player):
        (
            self.goalkeepers,
            self.defenders,
            self.midfielders,
            self.forwards,
        )[
            player.element_type - 1
        ].add(player)

    def print_team(self):
        output = f"""
        {self._format_postition("Goalkeepers", self.goalkeepers)}
        {self._format_postition("Defenders", self.defenders)}
        {self._format_postition("Midfielders", self.midfielders)}
        {self._format_postition("Forwards", self.forwards)}

        Cost: {self.cost/10}
        With this team, the current total score is: {self.total_points}
        """
        print(output)

    def _format_postition(self, position_name: str, position_list: List[Player]) -> str:
        string = f"{position_name}:\n"
        for p in position_list:
            string += p.format_name() + "\n"
        return string
