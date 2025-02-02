import csv
import random
from datetime import datetime, timedelta

# Function to generate dates from 2022 to 2024
def generate_dates(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = timedelta(days=1)
    dates = []

    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += delta
    return dates

# Function to generate happiness values with an average of 40
def generate_happiness_values(num_values, avg_value=40, fluctuation=10):
    values = []
    for _ in range(num_values):
        value = random.uniform(avg_value - fluctuation, avg_value + fluctuation)
        values.append(value)
    return values

# Generate dates
dates = generate_dates(2022, 2024)

# Generate happiness values
values = generate_happiness_values(len(dates))

# Write data to CSV file
csv_file = 'outputHAPPINES.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Happiness'])  # Write header
    writer.writerows(zip(dates, values))  # Write rows of data

print(f'CSV file {csv_file} has been created.')