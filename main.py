import utils
from cli import mutat_menu
from foglalasirendszer import FoglalasiRendszer

if __name__ == '__main__':
    foglalasi_rendszer = FoglalasiRendszer()
    utils.inicializal(foglalasi_rendszer)
    while True:
        mutat_menu(foglalasi_rendszer)
