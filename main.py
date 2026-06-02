# 1. Find and open the file
import csv
file_name='dirty_data.csv'

with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
# 2. Prepare to read it as a csv

    csv_reader = csv.DictReader(csv_file)

# 3. For each row of data in the file:
    for row in csv_reader:
   # 4. find the piece of data under the 'Campaign Name' column
        campaign_name = row['Campaign Name']
        clicks = row['Clicks']
        spend = row['Spend']
        date = row['Date']


   # 5. print that piece of data
        print(f"Campaign: {campaign_name} | Clicks: {clicks} | Spend: {spend} | Date: {date}")

# 6. Finish once all the rows are looped over, and be happy that the file is closed properly