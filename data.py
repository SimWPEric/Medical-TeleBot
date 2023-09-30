import csv

csv_file_path = "Data.csv"

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    header = next(csv_reader)

def displayHeader():
    column_options = {}

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        header = next(csv_reader)

        for column_name in header:
            column_options[column_name] = set()

        csv_file.seek(0)
        next(csv_reader)

        for row in csv_reader:
            for index, column_name in enumerate(header):
                column_options[column_name].add(row[index])

    for column_name, options_set in column_options.items():
        column_options[column_name] = list(options_set)

    return column_options


column_options_dict = displayHeader()
for key, value in column_options_dict.items():
    print(f"{key}: {value}")



