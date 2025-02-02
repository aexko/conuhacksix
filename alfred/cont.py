import csv
from datetime import datetime

# Read the CSV data
input_file = 'arbres-dhp.csv'

total_count = 0

with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date_str = row['RAD_DATE_PRISE']
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S').date()
        if date.year < 2022:
            total_count += 1

print(f'Total count of trees before 2022: {total_count}')