from model.slot_machine import SlotMachineModel


class SlotMachineView:
    def __init__(self,
                 model: SlotMachineModel):
        self.model = model

    def show_toys(self):
        print('In Slot Machine:')
        for toy in self.model.toys_list:
            print(f'{toy.name.capitalize()} ({toy.quantity} pieces).')

    @staticmethod
    def start_draw():
        print('Start slot machine\'s draws!!!')

    @staticmethod
    def new_player():
        print('==================\n'
              'New player trying.')
