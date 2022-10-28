from inventory_report.inventory.product import Product

nome_do_produto = "Sorvete"
nome_da_empresa = "28/10/2022"
data_de_fabricacao = "Sorveteria"
data_de_validade = "28/10/2023"
numero_de_serie = "ABC1234"
instrucoes_de_armazenamento = "Geladeira"


def test_cria_produto():
    new_product = Product(
        1,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )
    assert new_product.nome_do_produto == nome_do_produto
    assert new_product.nome_da_empresa == nome_da_empresa
    assert new_product.data_de_fabricacao == data_de_fabricacao
    assert new_product.data_de_validade == data_de_validade
    assert new_product.numero_de_serie == numero_de_serie
    assert (
        new_product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
    )
