import os
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path: str):
        _, extension = os.path.splitext(path)
        if extension == '.xml':
            with open(path) as fd:
                products = xmltodict.parse(fd.read())["dataset"]["record"]
            return products
        else:
            raise ValueError('Arquivo inválido')
