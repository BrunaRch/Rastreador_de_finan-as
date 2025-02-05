import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_ARQUIVO ="dados_financeiros.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_ARQUIVO)
        except FileNotFoundError:
            
