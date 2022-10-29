import csv
import json
import xmltodict
import os
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_data(path):
        with open(path, encoding="utf8") as file:
            products = list(csv.DictReader(file))
        return products

    @staticmethod
    def json_data(path):
        with open(path) as file:
            products = json.load(file)
        return products

    @staticmethod
    def xml_data(path):
        with open(path) as fd:
            products = xmltodict.parse(fd.read())["dataset"]["record"]
        return products

    @staticmethod
    def import_data(path: str, type: str):
        products = []
        type_class = SimpleReport if type == "simples" else CompleteReport
        _, extension = os.path.splitext(path)
        if extension == ".csv":
            products = Inventory.csv_data(path)
        elif extension == ".json":
            products = Inventory.json_data(path)
        elif extension == ".xml":
            products = Inventory.xml_data(path)
        else:
            raise ValueError("Arquivo invalido")
        return type_class.generate(products)
