from jarat import Jarat


class NemzetkoziJarat(Jarat):
    """
    Nemzetkozi jaratokra vonatkozo osztaly, magasabb jegyarakkal.

    Attributumok:
        megegyeznek az ososztalyeval (Jarat)
    """

    def __init__(self, legitarsasagnev: str, indulasiallomas: str, celallomas: str,
                 indulas: str, kapacitas: int, jegyar: int):
        if jegyar < 100000:
            print("Hiba! Alacsony jegyar nemzetkozi jaratra! Nem jott letre a jarat.")
        else:
            super().__init__(legitarsasagnev, indulasiallomas, celallomas, indulas, kapacitas, jegyar)
