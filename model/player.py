from dataclasses import dataclass, field

from utils.randomizer import Randomizer


@dataclass
class PlayerModel:
    wins: int = 0
    loss: int = 0
    prizes: list = field(default_factory=list)

    def __post_init__(self):
        self.name: str = Randomizer.player_name()
        self.attempts: int = Randomizer.player_attempts()
        self.lucky: float = Randomizer.player_lucky()
