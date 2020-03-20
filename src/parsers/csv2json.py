import os
import typing

from src.base.parsers import BaseParser

import csv


class CSVParser(BaseParser):
    def parse(self, path: typing.Union[str, os.PathLike], *args, **kwargs):
        with open(path) as f:
            reader = csv.DictReader(f, delimiter=';')
            rows = list(reader)

        output_path = kwargs.get('output_path', '../../data/csv-parsed/BoardingData.json')
        self.to_json(rows, output_path=output_path)


if __name__ == '__main__':
    a = CSVParser()
    a.parse('/Users/dmitrij/Downloads/BoardingData.csv')
