from main.acasa.ProveidorExtern import ExternalProviderService


class Manager:

    def __init__(self, external_provider: ExternalProviderService):
        self.__external_provider = external_provider

    def cerca_producte(self, product_list: list, proveidor_extern: ExternalProviderService) -> (list, list):
        return True
