from jarat import Jarat


class NemzetkoziJarat(Jarat):
    """
    Nemzetkozi jaratokra vonatkozo osztaly, magasabb jegyarakkal.

    Attributumok:
        megegyeznek az ososztalyeval (Jarat)
    """

    def __init__(self, legitarsasagnev:str , jaratszam: int, indulasiallomas: str, celallomas: str,
                 indulas: str, kapacitas: int, jegyar: int):
        if jegyar < 100000:
            print("Figyelem: alacsony jegyar nemzetkozi jaratra!")
        else:
            super().__init__(legitarsasagnev, jaratszam, indulasiallomas, celallomas,
                 indulas, kapacitas, jegyar)