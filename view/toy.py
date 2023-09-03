from model.toy import ToyModel


class ToyView:
    def __init__(self, model: ToyModel):
        self.model = model

    def get_name(self):
        print(f'{self.model.name}')

    def get_quantity(self):
        print(f'{self.model.quantity}.' if self.model.quantity != 0
              else 'No more toys.')

    def get_frequency(self):
        print(f'{self.model.name.capitalize()} '
              f'({int(self.model.frequency * 100)}% chance to win).')
