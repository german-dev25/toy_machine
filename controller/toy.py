from model.toy import ToyModel
from view.toy import ToyView


class ToyController:
    def __init__(self,
                 toy: ToyModel,
                 view: ToyView):
        self.toy = toy
        self.view = view

    @property
    def id(self) -> int:
        return self.toy.id

    @property
    def name(self) -> str:
        return self.toy.name

    @property
    def quantity(self) -> int:
        return self.toy.quantity

    @property
    def frequency(self) -> float:
        return self.toy.frequency

    def set_quantity(self, amount: int) -> None:
        self.toy.quantity = amount

    def sub_quantity(self) -> None:
        self.toy.quantity -= 1
