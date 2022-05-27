import pytest
from unittest.mock import call, MagicMock
from main.acasa.Manager import Manager


@pytest.fixture()
def manager():
    def _manager(proveidor_extern, fake_bd):
        return Manager(proveidor_extern, fake_bd)

    return _manager


def assertMyTupleEqual(self, expected, actual):
    self.assertEqual(type(expected), type(actual))  # Checks the type
    self.assertEqual(len(expected), len(actual))    # Checks the length


class TestCerca:

    # Test 1
    def test_external_provider_calls(self, manager) -> None:
        product_list = ["product_1", "product_2", "product_3", "product_4"]
        mock_proveidor_extern = MagicMock()
        fake_bd = MagicMock()
        manager(mock_proveidor_extern, fake_bd).cerca_producte(product_list)

        calls = [call(product_list[0]), call(product_list[1]), call(product_list[2]), call(product_list[3])]
        mock_proveidor_extern.has_associated_ad.assert_has_calls(calls, any_order=False)

    # Test 2
    def test_returned_values_must_be_two_lists(self, manager) -> None:
        product_list = ["product_1", "product_2", "product_3", "product_4", "product_5"]
        mock_proveidor_extern = MagicMock()
        fake_bd = MagicMock()
        mock_proveidor_extern.has_associated_ad = MagicMock(return_value=False)  # Sets the mock to return always False.
        disponibility, ads = manager(mock_proveidor_extern, fake_bd).cerca_producte(product_list)

        assert (len(disponibility) == len(product_list), len(ads) == len(product_list))  # Check the lengths
        assert all(type(i) is bool for i in disponibility)  # Check the disponibility list type.
        assert all(type(i) is bool for i in ads)  # Check the ads list type.

    # Test 3
    def test_ad_is_true_when_it_has_to_be_true(self, manager) -> None:
        product_list = ["product_1", "product_2", "product_3", "product_4", "product_5", "producte_6", "product_7"]
        mock_proveidor_extern = MagicMock()
        fake_bd = MagicMock()
        expected_ads = [False, False, True, True, False, True, False]

        mock_proveidor_extern.has_associated_ad = MagicMock(side_effect=expected_ads)  # Returns different values on each call.
        disponibility, ads = manager(mock_proveidor_extern, fake_bd).cerca_producte(product_list)
        assert ads == expected_ads

    # Test 4
    def test_fake_bd_query_is_called_once(self, manager) -> None:
        product_list = ["product_1"]
        mock_proveidor_extern = MagicMock()
        fake_bd = MagicMock()
        manager(mock_proveidor_extern, fake_bd).cerca_producte(product_list)

        fake_bd.product_query.assert_called_once()

    # Test 5
    def test_5(self) -> None:
        pass
