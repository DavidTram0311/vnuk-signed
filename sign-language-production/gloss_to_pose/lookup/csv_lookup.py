import csv
import os
from .lookup import PoseLookup


class CSVPoseLookup(PoseLookup):
    """
    This class is a subclass of PoseLookup class that reads the index.csv file
    and prepare values for rows.
    """
    def __init__(self, lexicon_directory: str):
        with open(os.path.join(lexicon_directory, 'index.csv'), mode='r', encoding='utf-8') as f:
            rows = list(csv.DictReader(f))

        super().__init__(rows=rows, lexicon_directory=lexicon_directory)
