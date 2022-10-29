import csv
import json
import xmltodict
import os
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        products = []
        type_class = SimpleReport if type == "simples" else CompleteReport
        _, extension = os.path.splitext(path)
        if extension == ".csv":
            with open(path, encoding="utf8") as file:
                products = list(csv.DictReader(file))
        elif extension == ".json":
            with open(path) as file:
                products = json.load(file)
        elif extension == ".xml":
            with open(path) as fd:
                products = xmltodict.parse(fd.read())['dataset']['record']
        else:
            raise ValueError()
        return type_class.generate(products)


if __name__ == "__main__":
    SimpleReport()
    CompleteReport()
