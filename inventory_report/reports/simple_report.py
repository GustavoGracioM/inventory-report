import collections


class SimpleReport:
    def generate(self, products: list):
        data_de_fabricacao = min(
            [value["data_de_fabricacao"] for value in products]
        )
        data_de_validade = max(
            [value["data_de_validade"] for value in products]
        )
        nome_empresa = list(
            collections.Counter(
                [value["nome_da_empresa"] for value in products]
            ).items()
        )[0]
        return f"""
            Data de fabricação mais antiga: {data_de_fabricacao}
            Data de validade mais próxima: {data_de_validade}
            Empresa com mais produtos: {nome_empresa}
        """
