from model.player import PlayerModel
from view.player import PlayerView


class PlayerController:
    def __init__(self,
                 model: PlayerModel,
                 view: PlayerView):
        self.model = model
        self.view = view

    @property
    def name(self) -> str:
        return self.model.name

    @property
    def attempts(self) -> int:
        return self.model.attempts

    @property
    def lucky(self) -> float:
        return self.model.lucky

    def update_results(self, win: bool = True, prize: str = None):
        if win:
            self.model.wins += 1
            self.model.prizes.append(prize)
        else:
            self.model.loss += 1
