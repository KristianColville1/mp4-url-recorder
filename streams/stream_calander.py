import pandas as pd
from calendar import monthrange


DAYS = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
DAYS_INDEX = [0,1,2,3,4,5,6]

def get_calander_days_of_month(month, year):
    """
    Gets the days of a month and builds a dictionary
    that uses the key value pairs to find the dates of each day of a month.
    """
    calendar_obj = {}
    length_of_month = monthrange(year, month)
    print(length_of_month)
    keys = range(length_of_month[-1])
    day_of_week = 0
    for i in keys:
        if day_of_week >=7:
            day_of_week = 0
        
        calendar_obj[i] = i + 1
        day_of_week+=1
    
    # convert the key value pairs into a iterable 
    # calendar objects that can be used in the frontend

    return calendar_obj