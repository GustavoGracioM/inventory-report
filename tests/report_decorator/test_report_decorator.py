from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

products = [
    {
        "id": 1,
        "nome_do_produto": "Cafe",
        "nome_da_empresa": "Cafes Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "instrucao",
    },
    {
        "id": 2,
        "nome_do_produto": "Refrigerante",
        "nome_da_empresa": "Cafes Nature",
        "data_de_fabricacao": "2021-07-04",
        "data_de_validade": "2024-02-09",
        "numero_de_serie": "GR49",
        "instrucoes_de_armazenamento": "instrucao",
    },
    {
        "id": 3,
        "nome_do_produto": "Bolo",
        "nome_da_empresa": "Bolos Nature",
        "data_de_fabricacao": "2022-07-04",
        "data_de_validade": "2025-02-09",
        "numero_de_serie": "AR40",
        "instrucoes_de_armazenamento": "instrucao",
    },
]


def test_decorar_relatorio():
    GREEN, BLUE, RED, END = ["\033[32m", "\033[36m", "\033[31m", "\033[0m"]
    result = (
        f"{GREEN}Data de fabricação mais antiga:{END} {BLUE}2020-07-04{END}\n"
        f"{GREEN}Data de validade mais próxima:{END} {BLUE}2023-02-09{END}\n"
        f"{GREEN}Empresa com mais produtos:{END} {RED}Cafes Nature{END}"
    )

    colored_report = ColoredReport(SimpleReport).generate(products)
    assert colored_report in result
