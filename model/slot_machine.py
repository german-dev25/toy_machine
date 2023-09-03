from dataclasses import dataclass, field


@dataclass
class SlotMachineModel:
    volume_max: int
    toys_quantity: int = 0
    toys_list: list = field(default_factory=list)
    machine_frequency: float = 100
