from enum import Enum


class Status(Enum):
    IN_PROGRESS = 0
    X_WINS = 1
    O_WINS = 2
    STALEMATE = 3
    ABORTED = 4