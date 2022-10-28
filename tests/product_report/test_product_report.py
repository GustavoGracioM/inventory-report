from inventory_report.inventory.product import Product

nome_do_produto = "Sorvete"
nome_da_empresa = "28/10/2022"
data_de_fabricacao = "Sorveteria"
data_de_validade = "28/10/2023"
numero_de_serie = "ABC1234"
instrucoes_de_armazenamento = "Geladeira"

result_print = (
    f"O produto {nome_do_produto}"
    f" fabricado em {data_de_fabricacao}"
    f" por {nome_da_empresa} com validade"
    f" até {data_de_validade}"
    f" precisa ser armazenado {instrucoes_de_armazenamento}."
)


def test_relatorio_produto():
    new_product = Product(
        1,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )
    assert str(new_product) == result_print
