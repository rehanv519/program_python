import datetime as dt
x = dt.datetime.now()
print(x)   #date and time
print(x.year) #Year
print(x.strftime("%A")) #Day
x = dt.datetime(2020, 5, 17) 
print(x)
print(x.strftime("%B")) #month
print(x.strftime("%a")) #day  
print(x.strftime("%A")) #full name of day
print(x.strftime("%w")) #Number Of Day
print(x.strftime("%d")) #date
print(x.strftime("%b")) #Month Short Name
print(x.strftime("%B")) #Month Full Name
print(x.strftime("%m")) #No Of Month
print(x.strftime("%y")) #Year's Last Two digit
print(x.strftime("%Y")) #Full Year
print(x.strftime("%H")) #Hour [1]
print(x.strftime("%I"))  #Hour [01]
print(x.strftime("%p")) #am/pm
print(x.strftime("%M")) #Minute
print(x.strftime("%S")) #Second
print(x.strftime("%f")) #Microsecond
print(x.strftime("%z")) #UTC offset
print(x.strftime("%Z")) #timezone
print(x.strftime("%j")) #No of Day
print(x.strftime("%U")) #No Of Week Sunday as First Day
print(x.strftime("%W")) #No Of Week Monday as First Day
print(x.strftime("%c")) #Local Version Of Date & Time
print(x.strftime("%C"))  #Century
print(x.strftime("%x"))  #Local Version of Date
print(x.strftime("%X")) #Local version Of Time
print(x.strftime("%%")) #A % character
print(x.strftime("%G")) #ISO 8601 Date
print(x.strftime("%u"))  #ISO 8601 weekday (1-7)
print(x.strftime("%V")) #ISO 8601 weeknumber (01-53)






