import collections
from datetime import datetime


class SimpleReport:
    @staticmethod
    def earliest_manufacturing_date(products: list):
        return min([value["data_de_fabricacao"] for value in products])

    @staticmethod
    def closest_expiration_date(products: list):
        datetime_now = datetime.today().strftime("%Y-%m-%d")
        return min(
            [
                value["data_de_validade"]
                for value in products
                if value["data_de_validade"] > datetime_now
            ]
        )

    @staticmethod
    def company_more_products(products: list):
        return list(
            collections.Counter(
                [value["nome_da_empresa"] for value in products]
            ).items()
        )

    @staticmethod
    def generate(products: list):
        data_de_fabricacao = SimpleReport.earliest_manufacturing_date(products)
        data_de_validade = SimpleReport.closest_expiration_date(products)
        nome_empresa = max(
            SimpleReport.company_more_products(products),
            key=lambda item: item[1],
        )[0]
        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {nome_empresa}"
        )
