from . import *
from datetime import datetime


class JegyFoglalas:
    """
    A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

    Attributumok:
        szam (int): foglalas szama
        nev (str): utas neve
        jarat (Jarat): jarat
        indulas (datetime): indulasi datum es ido
    """

    def __init__(self, szam: int, nev: str, jarat: Jarat, indulas: datetime):
        self.szam = szam
        self.nev = nev
        self.jarat = jarat
        self.indulas = indulas
