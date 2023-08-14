import requests
import json
from datetime import datetime
from pprint import pprint
from data_classes.fantasy_team import FantasyTeam

from data_classes.player import Player
from data_classes.position import Position
from data_classes.team import Team
from data_classes.game_settings import GameSettings

json_file_name = "data/" + datetime.today().strftime("%d_%m_%Y") + "_data.json"

base_url = "https://fantasy.premierleague.com/api/"
data = {}

try:
    data = requests.get(base_url + "bootstrap-static/", timeout=5).json()
    with open(json_file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
except:
    with open(json_file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

players = [Player(**i) for i in data["elements"]]
teams = [Team(**i) for i in data["teams"]]
positions = [Position(**i) for i in data["element_types"]]
game_settings = GameSettings(**data["game_settings"])


point_ordered_players = sorted(players, key=lambda x: x.total_points, reverse=True)

positions_and_players = [
    {
        "position": pos,
        "players": [
            player
            for player in players
            if player.element_type is pos.id
        ],
    }
    for pos in positions
]

curent_fantasy_team = FantasyTeam(game_settings=game_settings)

for player in point_ordered_players[:4]:
    curent_fantasy_team.force_add_player(player)

for i in positions_and_players:
    cost_efficiency_ordered_players = sorted(i["players"], key=lambda x: x.cost_efficiency, reverse=True)

    for player in cost_efficiency_ordered_players:
        try:
            curent_fantasy_team.add_player(player, i["position"])
        except:
            break

curent_fantasy_team.print_team()
