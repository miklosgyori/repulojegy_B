class NemzetkoziJarat(Jarat):
    """
    Nemzetkozi jaratokra vonatkozo osztaly, magasabb jegyarakkal.

    Attributumok:
        megegyeznek az ososztalyeval (Jarat)
    """


    def __init__(self, jaratszam: int, legitarsasag: LegiTarsasag, celallomas: str,
                 indulaskapacitas: Dict[datetime, int], jegyar: int):
        if jegyar < 100000:
            print("Figyelem: alacsony jegyar nemzetkozi jaratra!")
        else:
            super().__init__(jaratszam, legitarsasag, celallomas, indulaskapacitas, indulaskapacitas, jegyar)