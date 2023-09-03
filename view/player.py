from model.player import PlayerModel


class PlayerView:
    def __init__(self, model: PlayerModel):
        self.model = model

    def name(self) -> None:
        print(f'Player {self.model.name}')

    def attempts(self, num) -> None:
        print(f'{self.model.name} (lucky {int(self.model.lucky * 100)}%) '
              f'trying to win. '
              f'Attempts: {num + 1}/{self.model.attempts}.')

    def win(self, toy) -> None:
        print(f'{self.model.name} win {toy.name.capitalize()}.')

    def loss(self) -> None:
        print(f'{self.model.name} is lose.')
