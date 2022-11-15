import datetime
from datetime import date,timedelta

a=datetime.date.today()
a1=a.strftime("%d-%m-%Y")
print("Current date is: ",a1)

b=timedelta(days=5)
c=a-b
d=c.strftime("%d-%m-%Y")
print("5 days before date is:",d)

