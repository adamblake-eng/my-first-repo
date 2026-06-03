# 1. Find and open the file
import csv
from utils import validate_row
file_name='dirty_data.csv'

print("---- Validating Each Row ----")

with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
# 2. Prepare to read it as a csv

    csv_reader = csv.DictReader(csv_file)

# 3. For each row of data in the file:
    for row in csv_reader:

        # pulling function from utils.py file
        is_row_valid, clicks, spend = validate_row(row)


        if is_row_valid:
            campaign_name = row['Campaign Name']
            date = row['Date']
            print(f"Campaign: {campaign_name} | Clicks: {clicks} | Spend: {spend} | Date: {date}")
        else:
            print("Invalid")
                

   