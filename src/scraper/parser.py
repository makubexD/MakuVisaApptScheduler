from datetime import datetime
from config import MY_SCHEDULE_DATE

last_seen = None

def MY_CONDITION(month, day): return True

def is_earlier(date):
    my_date = datetime.strptime(MY_SCHEDULE_DATE, "%Y-%m-%d")
    new_date = datetime.strptime(date, "%Y-%m-%d")
    result = my_date > new_date
    print(f'Is {my_date} > {new_date}:\t{result}')
    return result

def get_available_date(dates):
    global last_seen

    print("Checking for an earlier date:")
    for d in dates:
        date = d.get('date')
        if is_earlier(date) and date != last_seen:
            _, month, day = date.split('-')
            if MY_CONDITION(month, day):
                last_seen = date
                return date
            

def print_dates(dates):
    print("Available dates:")
    for d in dates:
        print("%s \t business_day: %s" % (d.get('date'), d.get('business_day')))
    print()