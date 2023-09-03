import logging

from config import MAX_TOYS_QUANTITY, MAX_PLAYERS

from model.slot_machine import SlotMachineModel
from controller.slot_machine import SlotMachineController
from view.slot_machine import SlotMachineView

from model.player import PlayerModel
from view.player import PlayerView
from controller.player import PlayerController

from model.toy import ToyModel
from view.toy import ToyView
from controller.toy import ToyController

from utils.logger import setup_logger

# устанавливаем логгер
setup_logger()

# Создаем модель игрового автомата и его контроллер
smm = SlotMachineModel(volume_max=MAX_TOYS_QUANTITY)
smv = SlotMachineView(smm)
smc = SlotMachineController(model=smm, view=smv)

# Наполняем автомат различными игрушками
while smc.model.toys_quantity < smm.volume_max:
    toy_model = ToyModel()
    toy_view = ToyView(toy_model)
    smc.fill_machine(ToyController(toy=toy_model, view=toy_view))

# заполняем в файл список игрушек
for toy in smc.model.toys_list:
    logging.info(f'{toy.name.capitalize()} - {toy.quantity} pieces.')

# Создаем список игроков
players_list = []
for _ in range(MAX_PLAYERS):
    player_model = PlayerModel()
    player_controller = PlayerController(model=player_model,
                                         view=PlayerView(player_model))
    players_list.append(player_controller)

# Устраиваем розыгрыш среди участников
for player in players_list:
    smc.view.new_player()
    logging.info(f'{player.name} has {player.attempts} attempts.')
    for attempt in range(player.attempts):
        if smc.model.toys_quantity <= 0:
            break
        game_result = smc.draw(player, attempt)
        if game_result:
            player.update_results(prize=game_result.name)
    logging.info(f'{player.name} win {player.model.wins} '
                 f'and loss {player.model.loss}.\n'
                 f'Prizes: {", ".join(player.model.prizes) if player.model.prizes else "Nothing"}')

logging.info(
    f'Collected {MAX_TOYS_QUANTITY - smc.model.toys_quantity} / {MAX_TOYS_QUANTITY}'
)
