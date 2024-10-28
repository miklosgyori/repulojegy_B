from jarat import Jarat


class NemzetkoziJarat(Jarat):
    """
    Nemzetkozi jaratokra vonatkozo osztaly, magasabb jegyarakkal.

    Attributumok:
        megegyeznek az ososztalyeval (Jarat)
    """


    def __init__(self, jaratszam: int, legitarsasag: LegiTarsasag, celallomas: str, jegyar: int):
        if jegyar < 100000:
            print("Figyelem: alacsony jegyar nemzetkozi jaratra!")
        if celallomas in celallomasokBelfold:
            print("Hiba! Ez belfoldi celallomas! Nem jott letre a jarat.")
        else:
            super().__init__(jaratszam, legitarsasag, celallomas, jegyar)