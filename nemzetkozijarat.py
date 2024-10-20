from jarat import Jarat


class NemzetkoziJarat(Jarat):
    """
    Nemzetkozi jaratokra vonatkozo osztaly, magasabb jegyarakkal.

    Attributumok:
        celallomasokBelfold (list[str]) : belfoldi celallomasok listaja
        a tovabbiak megegyeznek az ososztalyeval
    """


    def __init__(self, celallomasokBelfold, jaratszam, legitarsasag, celallomas, jegyar):
        if jegyar < 100000:
            print("Figyelem: alacsony jegyar nemzetkozi jaratra!")
        if celallomas in celallomasokBelfold:
            print("Hiba! Ez belfoldi celallomas! Nem jott letre a jarat.")
        else:
            super().__init__(jaratszam, legitarsasag, celallomas, jegyar)