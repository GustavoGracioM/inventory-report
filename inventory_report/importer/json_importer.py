import json
import os
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path: str):
        _, extension = os.path.splitext(path)
        if extension == '.json':
            with open(path) as file:
                products = json.load(file)
            return products
        else:
            raise ValueError('Arquivo inválido')
