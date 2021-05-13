"""
The module used for timestamp generation between two defined timestamps,
    properly formatted
Author: Patrick Danielson
"""


# Imports
from datetime import datetime as date, timedelta
import pytz
import pandas as pd

# Method to create list of all times in hourly intervals between two given times. Timezone and DST sensitive.
# Input: First time and last time as strings
# Output: List of all times in hourly intervals between those times
def makeTimes(currentTimes, dstActive, tz):
    # Initializations. List to be filled, as well as datetime objects of the bookend times
    timesList = []
    firstTime = currentTimes[0]
    lastTime = currentTimes[-1]
    timeObj = date.strptime(firstTime, '%Y-%m-%d %H:00:00%z')
    lastTimeObj = date.strptime(lastTime, '%Y-%m-%d %H:00:00%z')
    
    # Timezone object creation and DST object creation
    tz = pytz.timezone(tz)
    dstStartTZ, dstEndTZ = tz.localize(date(2020, 3, 8, 1), is_dst=False), tz.localize(date(2020, 11, 1, 1), is_dst=True)
    

    # While we are before the last time, we will loop and add more times
    while timeObj < lastTimeObj:
        
        # Add current time to list, if not currently in dataframe
        if timeEdit(timeObj.strftime('%Y-%m-%d %H:00:00%z')) not in currentTimes:
            timesList.append(timeEdit(timeObj.strftime('%Y-%m-%d %H:00:00%z')))


        
        # If daylight savings starts, or ends on the current hour.
        # Note: Whenever we are at the last time object, we will be DST or not as that time is.
        # Flipping back and forth will lead to the correct instance when we reach the final time.
        if timeObj == dstStartTZ and dstActive == True:
            
            #Change the time to account for it, add the new time to list, and account for the last time being in DST
            timeObj = tz.localize(timeObj.replace(tzinfo=None), is_dst=True)
            
            # Add current time to list, if not currently in dataframe
            if timeEdit(timeObj.strftime('%Y-%m-%d %H:00:00%z')) not in currentTimes:
                timesList.append(timeEdit(timeObj.strftime('%Y-%m-%d %H:00:00%z')))
            lastTimeObj -=  timedelta(hours=1)
            
        # If it ends
        elif timeObj == dstEndTZ and dstActive == True:
            
            #Change the time to account for it, add the new time to list, and account for the last time NOT being in DST
            timeObj = tz.localize(timeObj.replace(tzinfo=None), is_dst=False)
            
            # Add current time to list, if not currently in dataframe
            if timeEdit(timeObj.strftime('%Y-%m-%d %H:00:00%z')) not in currentTimes:
                timesList.append(timeEdit(timeObj.strftime('%Y-%m-%d %H:00:00%z')))
            lastTimeObj +=  timedelta(hours=1)
        
        
        
        # Add an hour, creating the next time to add to the list
        timeObj = timeObj + timedelta(hours=1)
    
    # Return the finalized list
    return timesList

# Method To edit output of datetime strings properly format timezone
# Input: Improperly formatted string
# Output: Properly formatted string, with colon present
def timeEdit(string):
    return "{0}:{1}".format(
  string[:-2],
  string[-2:]
)