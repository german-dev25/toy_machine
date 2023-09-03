import random
import names

from config import MAX_PLAYER_ATTEMPTS, MAX_ONE_TOY_QUANTITY, TOYS_LIST

# генерация случаных данных для автомата
class Randomizer:
    @staticmethod
    def player_attempts() -> int:
        return random.randint(1, MAX_PLAYER_ATTEMPTS)

    @staticmethod
    def player_name() -> str:
        return names.get_first_name()

    @staticmethod
    def player_lucky() -> float:
        return round(random.uniform(0.05, 0.95), 2)

    @staticmethod
    def set_toy() -> str:
        return random.choice(TOYS_LIST)

    @staticmethod
    def toy_frequency() -> float:
        return round(random.uniform(0.05, 0.95), 2)

    @staticmethod
    def toy_quantity() -> int:
        return random.randint(1, MAX_ONE_TOY_QUANTITY)