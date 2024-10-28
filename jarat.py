from abc import ABC
from legitarsasag import LegiTarsasag


class Jarat(ABC):
    """
    Absztrakt osztaly, egy altalanos jarat semaja.

    Attributomok:
        jaratszam (int)
        legitarsasag (str)
        celallomas (str)
        jegyar (int)
    """

    def __init__(self, jaratszam: int, legitarsasag: LegiTarsasag, celallomas: str, jegyar: int):
        self.jaratszam = jaratszam
        self.legitarsasag = legitarsasag
        self.celallomas = celallomas
        self.jegyar = jegyar
