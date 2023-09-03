from dataclasses import dataclass

from utils.randomizer import Randomizer


@dataclass
class ToyModel:
    id_counter: int = 1

    def __post_init__(self):
        self.id = ToyModel.id_counter
        ToyModel.id_counter += 1
        self.name: str = Randomizer.set_toy()
        self.quantity: int = Randomizer.toy_quantity()
        self.frequency: float = Randomizer.toy_frequency()

    def __str__(self):
        return f'{self.id}.{self.name} || {self.quantity} || {self.frequency}'