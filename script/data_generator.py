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

# Function to generate fluctuating values with an ascending or decreasing trend
def generate_trend_values(num_values, mode='random', min_val=0, max_val=100, fluctuation=10):
    step_size = (max_val - min_val) / num_values
    values = [random.uniform(min_val, min_val + step_size)]  # Start with a random value near the min_val
    
    for i in range(1, num_values):
        prev_value = values[-1]
        random_fluctuation = random.uniform(-fluctuation, fluctuation)
        
        if mode == 'ascending':
            next_value = prev_value + step_size + random_fluctuation
            next_value = max(min(next_value, max_val), prev_value)  # Ensure general upward trend
        elif mode == 'decreasing':
            next_value = prev_value - step_size + random_fluctuation
            next_value = min(max(next_value, min_val), prev_value)  # Ensure general downward trend
        else:
            next_value = random.uniform(min_val, max_val)
        
        values.append(next_value)
    
    return values

# Get user input for value generation mode
mode = input("Enter mode (ascending, decreasing, random): ").strip().lower()

# Generate dates
dates = generate_dates(2022, 2024)

# Generate values based on the chosen mode
values = generate_trend_values(len(dates), mode)

#Get user input for name of CSV file
csv_file = input("Enter the name of the CSV file: ")

# Write data to CSV file
csv_file = f'{csv_file}.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Value'])  # Write header
    writer.writerows(zip(dates, values))  # Write rows of data

print(f'CSV file {csv_file} has been created.')
