from random import seed, randrange
from datetime import datetime

seed(datetime.now().today())


def random_win(chance: float):
    assert 0 <= chance <= 1
    if chance == 0:
        return False
    max_value = round(1 / chance)
    return 0 == randrange(0, max_value)
