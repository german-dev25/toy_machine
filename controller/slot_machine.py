import random

from controller.player import PlayerController
from controller.toy import ToyController
from model.slot_machine import SlotMachineModel
from view.slot_machine import SlotMachineView


class SlotMachineController:
    def __init__(self,
                 model: SlotMachineModel,
                 view: SlotMachineView):
        self.model = model
        self.view = view

    # список игрушек
    @property
    def get_toys_list(self) -> list:
        return [toy for toy in self.model.toys_list if toy.quantity > 0]

    def fill_machine(self, toy: ToyController) -> None:
        # проверяем, что не переполним автомат
        toy.set_quantity(min(toy.quantity, self.remaining_volume()))
        self.model.toys_list.append(toy)
        self.model.toys_quantity += toy.quantity
        self.set_frequency()

    # считаем, что вероятность выбора игрушки для розыгрыша равная для каждой
    def set_frequency(self) -> None:
        self.model.machine_frequency = 1 / self.model.toys_quantity

    # остаток места в автомате
    def remaining_volume(self) -> int:
        return self.model.volume_max - self.model.toys_quantity

    # выбор игрушки
    def select_toy(self) -> ToyController:
        toys = self.get_toys_list
        weights = [toy.quantity * self.model.machine_frequency for toy in toys]
        return random.choices(toys, weights)[0]

    # выдаем игрушку
    def pop_toy(self, toy: ToyController) -> ToyController:
        for toys in self.get_toys_list:
            if toys.id == toy.id:
                self.model.toys_quantity -= 1
                toys.sub_quantity()
                self.model.toys_list = self.get_toys_list
                if self.model.toys_quantity > 0:
                    self.set_frequency()
                return toy

    # розыгрыш игрушки
    def draw(self,
             player: PlayerController,
             attempt: int) -> ToyController | None:
        selected_toy = self.select_toy()
        player.view.attempts(attempt)
        selected_toy.view.get_frequency()
        if (player.lucky + selected_toy.frequency) / 2 > 0.5:
            player.view.win(selected_toy)
            return self.pop_toy(selected_toy)
        else:
            player.view.loss()
            return None
