from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's Date is ",today)
print("Current date and time is ",now)

print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)