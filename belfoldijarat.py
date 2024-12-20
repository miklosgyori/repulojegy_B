from jarat import Jarat


class BelfoldiJarat(Jarat):
    """
    Belfoldi jaratokra vonatkozó osztaly, amelyek olcsobbak es rovidebbek.

    Attributomok:
        megegyeznek az ososztalyeval (Jarat)
    """

    def __init__(self, legitarsasagnev: str, indulasiallomas: str, celallomas: str,
                 indulas: str, kapacitas: int, jegyar: int):
        if jegyar > 100000:
            print("Hiba! Belfoldi jegyar nem lehet magasabb mint 100.000! Nem jott letre a jarat.")
        else:
            super().__init__(legitarsasagnev, indulasiallomas, celallomas, indulas, kapacitas, jegyar)
