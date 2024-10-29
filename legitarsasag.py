from jarat import Jarat
from typing import List


class LegiTarsasag:
    """
    LegiTarsasag osztaly: tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.

    Attributumok:
        nev (str): legitarsasag neve
        jaratok (list[Jarat]): legitarsasag jaratai
    """

    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok: List[Jarat] = []
        print("Legitarsasag letrejott.")

    def __str__(self):
        jaratokstring = ""
        if self.jaratok:
            for jarat in self.jaratok:
                jaratokstring += f"\t{jarat}\n"
        else:
            jaratokstring += "(meg nincs jarat)"
        return f"legitarsasag neve: {self.nev}; jaratok: \n{jaratokstring}"
