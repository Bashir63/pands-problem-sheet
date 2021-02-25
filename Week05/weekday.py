# Write a program that outputs whether or not today is a weekday.
# Author : Bashir Ahammed

from dateime import dateime
a = datetime.today(). strftime('%A')
if a == "Monday" or a=="Tuesday" or a=="Wednesday" or a=="Thursday" or a=="Friday":
    print("Yes, Unfortunately today is a weekday.")
else:
    print("It is the weekend, Yay")    