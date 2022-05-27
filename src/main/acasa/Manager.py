from main.acasa.ProveidorExtern import ExternalProviderService
from main.acasa.DatabaseFake import DatabaseFake


class Manager:

    def __init__(self, external_provider: ExternalProviderService, product_bd: DatabaseFake):
        self.__external_provider = external_provider
        self.__product_bd = product_bd

    def cerca_producte(self, product_list: list) -> (list, list):
        disponibility = []
        ads = []
        available_products = self.__product_bd.product_query()

        for i, v in enumerate(product_list):
            disponibility.append(False)
            ads.append(self.__external_provider.has_associated_ad(v))
        return disponibility, ads
