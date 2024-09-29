""""
 Python’s datetime module by writing a script 
 that performs specified operations with dates and times.
"""
#import the datetime module
from datetime import date
from datetime import datetime
today = date.today()
time_now = datetime.now()

def display_current_datetime():
  
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time
print("Current date and time : ",display_current_datetime())



from datetime import datetime, timedelta

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    #number_of_days = int(input("Enter the number of days to add to current date: "))
    
    future_date = datetime.now() + timedelta(days=number_of_days)
    future_date = future_date.strftime("Future date: %Y-%m-%d ")
    return future_date

print(calculate_future_date())

