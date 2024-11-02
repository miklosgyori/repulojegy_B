from abc import ABC


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

    def __init__(self, legitarsasagnev: str, indulasiallomas: str, celallomas: str, indulas: str, kapacitas: int, jegyar: int):
        self.jaratszam = 0
        self.legitarsasagnev = legitarsasagnev
        self.indulasiallomas = indulasiallomas
        self.celallomas = celallomas
        self.indulas = indulas
        self.kapacitas = kapacitas
        self.jegyar = jegyar

    def __str__(self):
        return (f"jaratszam: {self.jaratszam}; legitarsasag: {self.legitarsasagnev};"
                f" {self.indulasiallomas} --> {self.celallomas}; "
                f"indulas: {self.indulas}; szabad helyek: {self.kapacitas}; ar: {self.jegyar}")
