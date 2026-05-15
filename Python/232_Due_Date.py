#30-03-2026 | 30-03-2026

'''
    Given: date in str format.
    Problem: date after 9 months.
    Return: the future date after 9 months 
'''


from datetime import datetime
import calendar

def get_due_date(date_str):
    # Convert string to date
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Add 9 months
    new_month = date.month + 9
    new_year = date.year + (new_month - 1) // 12
    new_month = ((new_month - 1) % 12) + 1
    
    # Get last day of new month
    last_day = calendar.monthrange(new_year, new_month)[1]
    
    # Adjust day if needed
    new_day = min(date.day, last_day)
    
    # Return formatted string
    return f"{new_year:04d}-{new_month:02d}-{new_day:02d}"

def test_cases():
    print(get_due_date("2025-03-30"))  # 2025-12-30
    print(get_due_date("2025-04-27"))  # 2026-01-27
    print(get_due_date("2025-05-29"))  # 2026-02-28
    print(get_due_date("2026-06-30"))  # 2027-03-30
    print(get_due_date("2026-10-11"))  # 2027-07-11


if __name__ == "__main__":
    test_cases()