import csv
from pathlib import Path

dataFile = "data.csv"
cfgFileDir = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(dataFile)

def get_data():
    with open(DATA_FILE,'r+') as f:
        reader = csv.reader(f)
        next(reader) # Skips the first row, as it has the header
        data = [tuple(row) for row in reader]

    return data

print(get_data())