from abc import ABC
from datetime import datetime


class Jarat(ABC):
    """
    Absztrakt osztaly, egy altalanos jarat semaja.

    Attributomok:
        legitarsasagnev (str)
        jaratszam (int)
        indulasiallomas (str)
        celallomas (str)
        indulas (datetime)
        kapacitas (int)
        jegyar (int)
    """

    def __init__(self, legitarsasagnev: str, jaratszam: int, indulasiallomas: str, celallomas: str,
                 indulas: datetime, kapacitas: int, jegyar: int):
        self.legitarsasagnev = legitarsasagnev
        self.jaratszam = jaratszam
        self.indulasiallomas = indulasiallomas
        self.celallomas = celallomas
        self.indulas = indulas
        self.kapacitas = kapacitas
        self.jegyar = jegyar

    def __str__(self):
        return (f"{self.legitarsasagnev}-{self.jaratszam}: {self.indulasiallomas} --> {self.celallomas}; {self.indulas};"
                f"szabad helyek: {self.kapacitas}; ar: {self.jegyar}")
