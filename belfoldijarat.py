from jarat import Jarat


class BelfoldiJarat(Jarat):
    """
    Belfoldi jaratokra vonatkozó osztaly, amelyek olcsobbak es rovidebbek.

    Attributomok:
        celallomasokBelfold (list[str]) : belfoldi celallomasok listaja
        tovabbiak megegyeznek az ososztalyeval
    """

    def __init__(self, celallomasokBelfold, jaratszam, legitarsasag, celallomas, jegyar):
        if jegyar > 100000:
            print("Hiba! Belfoldi jegyar nem lehet magasabb mint 100.000! Nem jott letre a jarat.")
        elif celallomas not in celallomasokBelfold:
            print("Hiba! Nem letezo belfoldi celallomas! Nem jott letre a jarat.")
        else:
            super().__init__(jaratszam, legitarsasag, celallomas, jegyar)

