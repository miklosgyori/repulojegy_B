from . import *

class LegiTarsasag:
    """
    LegiTarsasag osztaly: tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.

    Attributumok:
        nev (str): legitarsasag neve
        jaratok (list[Jarat]): legitarsasag jaratai
    """

    def __init__(self, nev: str, jaratok: list[Jarat]):
        self.nev = nev
        self.jaratok = jaratok
