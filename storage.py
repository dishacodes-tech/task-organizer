from datetime import datetime, date

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def calculate_days_left(deadline_str):
    deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y").date()
    today = date.today()
    return (deadline_date - today).days