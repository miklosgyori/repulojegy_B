class FoglalasiRendszer:
    """
    Singleton osztaly az alapveto adatok tarolasara es folyamatok mukodtetesere.
    """
    _instance = None
    _initialized = False

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.celallomasokBelfold: list[str] = []
            self.foglalasok: list[int] = []
            self._initialized = True
            print("Foglalasi rendszer letrejott.")
