#Matthew Suriawinata
#4.26.18
#displayDate.py - displays date


from datetime import *

today = date.today()

day = str(today.day)
month = (today.month)
year = str(today.year)
weekday = today.weekday()




weeks = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("Today is", weeks[weekday], months[month] , day , year)