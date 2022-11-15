import datetime
from datetime import date

a=datetime.datetime.now()
a1=a.strftime("%d:%m:%Y, %H:%M:%S")
print("The Date and Time is:",a1)
b=date.today()
print("Year is:",b.year)
print(b.month,"th month",)
c=a.strftime("%U")
print(c,"th week of the year")
d=a.strftime("%A")
print(d)
e=a.strftime("%j")
print(e,"th day of the year")
f=a.strftime("%m")
print(f,"th day of the month")
g=a.strftime("%w")
print(g,"th day of the week")
