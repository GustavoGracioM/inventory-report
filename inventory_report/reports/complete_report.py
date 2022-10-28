from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(products: list):
        company = SimpleReport.company_more_products(products)
        products_quantity = ""
        for pq in company:
            products_quantity += f"- {pq[0]}: {pq[1]}\n"
        result = SimpleReport.generate(products)
        return (
            f"{result}\n"
            "Produtos estocados por empresa:\n"
            f"{products_quantity}"
        )
