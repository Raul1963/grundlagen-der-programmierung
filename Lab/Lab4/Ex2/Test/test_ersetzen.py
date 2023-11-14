from Logik.Ersetzen import Count
from ui.console import run


def test():
    assert(Count('meine_datei.txt', 'rot', 'indigo'))==3
