from jarat import Jarat


class BelfoldiJarat(Jarat):
    """
    Belfoldi jaratokra vonatkozó osztaly, amelyek olcsobbak es rovidebbek.

    Attributomok:
        megegyeznek az ososztalyeval (Jarat)
    """

    def __init__(self, jaratszam: int, legitarsasag: LegiTarsasag, celallomas: str, jegyar: int):
        if jegyar > 100000:
            print("Hiba! Belfoldi jegyar nem lehet magasabb mint 100.000! Nem jott letre a jarat.")
        elif celallomas not in celallomasokBelfold:
            print("Hiba! Nem letezo belfoldi celallomas! Nem jott letre a jarat.")
        else:
            super().__init__(jaratszam, legitarsasag, celallomas, jegyar)

