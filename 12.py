import calendar
import datetime
from calendar import monthrange
from datetime import date


#input your date
while True :
    date0 = input('Give a date (dd/mm/yyyy): ')
    try :
        date0 = datetime.datetime.strptime(date0, "%d/%m/%Y")
        break
    except ValueError:
        print("Error: must be format dd/mm/yyyy ")

#take pc's date
date1 = datetime.datetime.today()       

#finds the distance of dates
#for this date and an older date
delta=date1-date0
#for a later date
if (delta.days<0):
 delta=date0-date1
 
 
#results
print("The date given is ",delta.days," days,",delta.seconds//3600
      ," hours,",(delta.seconds//60)%60, " minites(",delta.seconds," seconds) from the current day")

print("Τhe days of the month of the date given are ",calendar.monthrange(date0.year, date0.month)[1]," days")

