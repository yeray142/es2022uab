import pytest
import perfBotiguer
import catalegProductes
import producte

class TestDisponibilitat():
    def test_comprova_disponibilitat(self, producte):
        botiga=perfBotiguer()