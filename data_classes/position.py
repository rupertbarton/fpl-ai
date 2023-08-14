from dataclasses import dataclass
from typing import Any, List
from pydantic import validate_arguments


@validate_arguments
@dataclass
class Position:
    id: int
    plural_name: str
    plural_name_short: str
    singular_name: str
    singular_name_short: str
    squad_select: int
    squad_min_play: int
    squad_max_play: int
    ui_shirt_specific: bool
    sub_positions_locked: list
    element_count: int
