# 1. Find and open the file
import csv
file_name='dirty_data.csv'

print("---- Validating Each Row ----")

with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
# 2. Prepare to read it as a csv

    csv_reader = csv.DictReader(csv_file)

# 3. For each row of data in the file:
    for row in csv_reader:

        # assuming all rows are valid until proven otherwise
        is_row_valid = True

        # Rule 1: Name, Spend, CLick Fields cannot be emtpy
        if not row['Campaign Name'] or not row['Clicks'] or not row['Spend']:
            is_row_valid = False
            

        if is_row_valid:
            try:
                # Rule 2: clicks and spend must be numeric so we try ot convert them to decimal numbers
                # if they cant be converted then they are not a number and it fails and goes to except block
                clicks = float(row['Clicks'])
                spend = float(row['Spend'])

                # Rule 3 :clicks and spend cannot be negative
                if clicks < 0 or spend < 0:
                    is_row_valid = False
                    

            except ValueError:
                is_row_valid = False

        if is_row_valid:
            campaign_name = row['Campaign Name']
            date = row['Date']
            print(f"Campaign: {campaign_name} | Clicks: {clicks} | Spend: {spend} | Date: {date}")
        else:
            print("Invalid")
                

   