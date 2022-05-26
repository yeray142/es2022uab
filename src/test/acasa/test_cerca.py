import pytest
from unittest.mock import call, MagicMock
from main.acasa.Manager import Manager


@pytest.fixture()
def manager():
    def _manager(proveidor_extern):
        return Manager(proveidor_extern)

    return _manager


def assertMyTupleEqual(self, expected, actual):
    self.assertEqual(type(expected), type(actual))  # Checks the type
    self.assertEqual(len(expected), len(actual))    # Checks the length


class TestCerca:

    # Test 1
    def test_external_provider_calls(self, manager) -> None:
        product_list = ["product_1", "product_2", "product_3", "product_4"]
        mock_proveidor_extern = MagicMock()
        manager(mock_proveidor_extern).cerca_producte(product_list, mock_proveidor_extern)

        calls = [call(product_list[0]), call(product_list[1]), call(product_list[2]), call(product_list[3])]
        mock_proveidor_extern.has_associated_ad.assert_has_calls(calls, any_order=False)

    # Test 2
    def test_2(self) -> None:
        pass

    # Test 3
    def test_3(self) -> None:
        pass

    # Test 4
    def test_4(self) -> None:
        pass

    # Test 5
    def test_5(self) -> None:
        pass
