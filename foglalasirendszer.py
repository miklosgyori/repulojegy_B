from legitarsasag import LegiTarsasag
from jegyfoglalas import JegyFoglalas


class FoglalasiRendszer:
    """
    Singleton osztaly az alapveto adatok tarolasara es az alapveto funkciok mukodtetesere.
    """
    _instance = None
    _initialized = False
    jaratok_szama = 0
    legitarsasagok: list[LegiTarsasag] = []
    foglalasok: list[JegyFoglalas] = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            print("\nFoglalasi rendszer letrejott.")

