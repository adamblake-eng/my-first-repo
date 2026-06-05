# 1. Find and open the file
import csv
from datetime import datetime  # To add timestamps to our log file
from utils import validate_row
file_name='dirty_data.csv'
output_file = 'clean_data.csv'
log_file = 'validation_log.txt'

print("---- Processing & Cleaning Data ----")

with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file_in, \
     open(output_file, mode='w', newline='', encoding='utf-8') as csv_file_out, \
     open(log_file, mode='w', encoding='utf-8') as log_out:  # Open log in write mode
    
# 2. Prepare to read it as a csv
    csv_reader = csv.DictReader(csv_file_in)

    # Define the exact columns you want in your final output file
    headers = ['Campaign Name', 'Clicks', 'Spend', 'Date']
    csv_writer = csv.DictWriter(csv_file_out, fieldnames=headers)

    # Write the header row into the clean file first
    csv_writer.writeheader()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_out.write("==================================================\n")
    log_out.write(f"DATA VALIDATION RUN: {current_time}\n")
    log_out.write(f"Source File: {file_name}\n")
    log_out.write("==================================================\n\n")

    # Keep track of counts for a summary at the end
    clean_count = 0
    dirty_count = 0

# 3. For each row of data in the file:
    for row_num, row in enumerate(csv_reader, start=2): # start=2 because row 1 is the header


        # pulling function from utils.py file
        is_row_valid, clicks, spend = validate_row(row)

        if is_row_valid:
            clean_campaign_name = row['Campaign Name'].strip().lower() # removes whitespace and make all lower case
            date = row['Date']

            csv_writer.writerow({
                'Campaign Name': clean_campaign_name,
                'Clicks': int(clicks),
                'Spend': round(spend, 2),
                'Date': date
            })
            clean_count += 1
        else:
            dirty_count += 1
            campaign_label = row['Campaign Name'] if row['Campaign Name'] else "[EMPTY NAME FIELD]"
            
            reason = "Unknown Validation Failure"
            if not row['Campaign Name'] or not row['Clicks'] or not row['Spend']:
                reason = "Missing critical data fields (Name, Clicks, or Spend is empty)"
            else:
                try:
                    click_check = float(row['Clicks'])
                    spend_check = float(row['Spend'])
                    if click_check < 0 or spend_check < 0:
                        reason = f"Negative value detected (Clicks: {row['Clicks']}, Spend: {row['Spend']})"
                except ValueError:
                    reason = f"Non-numeric metric characters (Clicks: '{row['Clicks']}', Spend: '{row['Spend']}')"

            # 6. Write the structured error line straight to validation_log.txt
            log_out.write(f"[ROW {row_num}] FAILED - Campaign: {campaign_label}\n")
            log_out.write(f"          Reason: {reason}\n\n")

    # 7. Write a final summary snapshot block at the bottom of the log file
    log_out.write("==================================================\n")
    log_out.write("RUN SUMMARY:\n")
    log_out.write(f"Total Rows Successfully Cleaned: {clean_count}\n")
    log_out.write(f"Total Rows Dropped / Flagged:    {dirty_count}\n")
    log_out.write("==================================================\n")

print(f"🎉 Success! Cleaned data saved to {output_file}")
print(f"📄 Detailed error logs generated in {log_file}")
                

   