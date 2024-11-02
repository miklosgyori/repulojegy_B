class JegyFoglalas:
    """
    A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

    Attributumok:
        szam (int): foglalas szama
        nev (str): utas neve
        jarat (Jarat): jarat
    """

    foglalasok_szama: int = 0

    def __init__(self, utasnev: str, jaratszam: int):
        self.szam = self.__class__.foglalasok_szama + 1
        self.utasnev = utasnev
        self.jaratszam = jaratszam
        self.__class__.foglalasok_szama += 1
        print("Foglalas letrejott.")

    def __str__(self):
        return f"foglalas szama: {self.szam}; utasnev: {self.utasnev}; jaratszam: {self.jaratszam}"
