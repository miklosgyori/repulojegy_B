from . import *
from abc import ABC
from typing import Dict
from datetime import datetime


class Jarat(ABC):
    """
    Absztrakt osztaly, egy altalanos jarat semaja.

    Attributomok:
        jaratszam (int)
        legitarsasag (str)
        celallomas (str)
        indulasKapacitas (Dict[datetime, int]): az indulasi datumokat es az ervenyes kapacotasokat tartalmazza
        jegyar (int)
    """

    def __init__(self, jaratszam: int, legitarsasag: LegiTarsasag, celallomas: str,
                 indulaskapacitas: Dict[datetime, int], jegyar: int):
        self.jaratszam = jaratszam
        self.legitarsasag = legitarsasag
        self.celallomas = celallomas
        self.indulaskapacitas = indulaskapacitas
        self.jegyar = jegyar
