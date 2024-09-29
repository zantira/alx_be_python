git """"
 Python’s datetime module by writing a script 
 that performs specified operations with dates and times.
"""
#import the datetime module
from datetime import date
from datetime import datetime
today = date.today()
time_now = datetime.now()

def display_current_date():
    """
    Displays the current date and time.

    Parameters:
        None

    Returns:
        None
    """
    current_time = datetime.now()
    print("Current date and time: ", current_time.strftime("%y-%d-%m") + " " + current_time.strftime("%H:%M:%S"))

display_current_date()

from datetime import datetime, timedelta

number_of_days = int(input("Enter the number of days to add to current date: "))
def calculate_future_date(number_of_days):
    """
    Calculates the future date by adding a specified number of days to the current date.

    Args:
        number_of_days (int): The number of days to add to the current date.

    Returns:
        str: The future date in the format "%d-%m-%Y".
    """
    future_date = datetime.now() + timedelta(days=number_of_days)
    return future_date.strftime("%d-%m-%Y")

print("Future date : ",calculate_future_date(number_of_days))

