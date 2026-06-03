def validate_row(row):
    
    if not row['Campaign Name'] or not row['Clicks'] or not row['Spend']:
        # Decided here: if it fails Rule 1, return False, and two "Nones"
        return False, None, None

    try:
        clicks = float(row['Clicks'])
        spend = float(row['Spend'])

        if clicks < 0 or spend < 0:
            return False, None, None
            
        # Decided here: If it passes all rules, return True AND the clean numbers!
        return True, clicks, spend

    except ValueError:
        return False, None, None