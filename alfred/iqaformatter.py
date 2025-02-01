import csv
from collections import defaultdict

# Read the CSV data
input_file = 'rsqa-indice-qualite-air-2022-2024.csv'
output_file = 'outputIQA.csv'

# Dictionary to store the sum and count of values for each day
date_data = defaultdict(lambda: [0, 0])

with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row['date']
        value = float(row['valeur'])

        date_data[date][0] += value
        date_data[date][1] += 1

# Calculate the average values and write to the output CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Average Value'])

    for date, (total, count) in date_data.items():
        average_value = total / count
        writer.writerow([date, average_value])