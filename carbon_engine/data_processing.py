import csv



years = [2030, 2040, 2050,2060,2070,2080,2090,2100,2110,2120,2130,2140]
levels = [0.23, 0.33, 0.44, 0.56, 0.69, 0.82, 0.96, 1.12, 1.24, 1.39, 1.54, 1.69]

def get_data(path):

    with open(path, 'r') as read_file:

        reader = csv.reader(read_file)

        for row in reader:

            print(row)

def get_columns(path, i):

    with open(path, 'r') as read_file:

        reader = csv.reader(read_file)

        next(reader)

        return [row[i] for row in reader]