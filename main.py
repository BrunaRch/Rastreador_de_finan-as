import pandas as pd
import csv
import os
from datetime import datetime


class CSV:
    CSV_FILE ="dados_financeiros.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description)
CSV.initialize_csv()


# 20-07-2024, 125, ENtrada, Salário


