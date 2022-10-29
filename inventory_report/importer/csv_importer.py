import csv
import os
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path: str):
        _, extension = os.path.splitext(path)
        if extension == '.csv':
            with open(path, encoding="utf8") as file:
                products = list(csv.DictReader(file))
            return products
        else:
            raise ValueError('Arquivo inválido')
