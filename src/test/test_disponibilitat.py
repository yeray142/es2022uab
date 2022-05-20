import pytest
import numpy as np
from main.perfBotiguer import botiguer
#import producte

class TestDisponibilitat():
    def test_comprova_disponibilitat(self):
        botiga=botiguer()
        botiga.afegirProducte("poma", 3)
        botiga.afegirProducte("taronja", 1)
        botiga.afegirProducte("pera", 5)
        botiga.treureProducte("taronja", 1)
        botiga.treureProducte("pera", 2)
        botiga.treureProducte("poma", 5)
        assert botiga.disponibilitat("poma") == 0
        assert botiga.disponibilitat("taronja") == 0
        assert botiga.disponibilitat("pera") != 0



if __name__ == "__main__"
    pytest.main()