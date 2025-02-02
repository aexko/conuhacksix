import csv
from datetime import datetime

# Read the CSV data
input_file = 'arbres-dhp.csv'
output_file = 'outputTREES.csv'
initial_tree_total = 592246  # Replace with your initial tree total

date_counts = {}
cumulative_total = initial_tree_total

with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date_str = row['RAD_DATE_PRISE']
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S').date()
        if date.year >= 2022:
            if date not in date_counts:
                date_counts[date] = 0
            date_counts[date] += 1

# Write the results to a new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Cumulative Total'])
    for date in sorted(date_counts):
        cumulative_total += date_counts[date]
        writer.writerow([date, cumulative_total])