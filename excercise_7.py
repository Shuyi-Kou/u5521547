from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Convert the date strings to datetime objects
    today = datetime.strptime(todays_date, '%d %B')
    scheduled = datetime.strptime(scheduled_date, '%d %B')
   # Compare dates
    if today < scheduled:
        print("Scheduled date is yet to pass.")
    elif today > scheduled:
        print("Scheduled date has passed.")
    else:
        print("Scheduled date is today.")

# Test cases
date_passed("26 March", "25 March")  # Expected: Scheduled date has passed
date_passed("26 March", "26 March")  # Expected: Scheduled date is today
date_passed("26 March", "27 March")  # Expected: Scheduled date is yet to pass