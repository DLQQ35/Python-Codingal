import calendar
from datetime import date, time, datetime

today = date.today()
print("Year:",today.year)

def all_months():
    for i in range(1,13):
        print(calendar.month_name[i])

if __name__ == "__main__":
    all_months()