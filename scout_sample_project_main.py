# Imports
import pandas
from datetime import datetime as date, timedelta
import pytz
import time

# Initializations
est, cst = pytz.timezone('US/Eastern'), pytz.timezone('US/Central')
dstStartNaive, dstEndNaive = date(2020, 3, 8, 1), date(2020, 11, 1, 1)
dstStartTZ, dstEndTZ = cst.localize(date(2020, 3, 8, 1)), est.localize( date(2020, 11, 1, 1))


# Method to create list of all times in hourly intervals between two given times. Timezone and DST sensitive.
# Input: First time and last time as strings
# Output: List of all times in hourly intervals between those times

def makeTimes(firstTime, lastTime):
    # Initializations. List to be filled, as well as datetime objects of the times
    timesList = []
    timeObj = date.strptime(firstTime, '%Y-%m-%d %H:00:00%z')
    lastTimeObj = date.strptime(lastTime, '%Y-%m-%d %H:00:00%z')

    # While we are before the last time, we will loop and add more times
    while timeObj < lastTimeObj:
        
        # Add current time to list
        timesList.append(timeObj)



        # If daylight savings starts, or ends on the current hour.
        # Note: Whenever we are at the last time object, we will be DST or not as that time is.
        # Flipping back and forth will lead to the correct instance when we reach the final time.
        if timeObj == dstStartTZ:
            
            #Change the time to account for it, add the new time to list, and account for the last time being in DST
            timeObj = cst.localize(timeObj.replace(tzinfo=None), is_dst=True)
            timesList.append(timeObj)
            lastTimeObj -=  timedelta(hours=1)
            
        # If it ends
        elif timeObj == dstEndTZ:
           
           #Change the time to account for it, add the new time to list, and account for the last time NOT being in DST
            timeObj = cst.localize(timeObj.replace(tzinfo=None), is_dst=False)
            timesList.append(timeObj)
            lastTimeObj +=  timedelta(hours=1)
        
        
        
        # Add an hour, creating the next time to add to the list
        timeObj = timeObj + timedelta(hours=1)
    
    # Return the finalized list
    return timesList




# Method in progress to create new excel file with conditions given
# Input: Excel file
# Output: 0 at present
def fileReader(inputFile):
    df = pandas.read_excel(inputFile)
    times = makeTimes(df.iloc[0]["time"], df.iloc[-1]["time"])
    return 0


# Main function, to ensure correct running enviroment.
if __name__ == "__main__":
    inputFile = "/Users/patrick/Desktop/test 2021-05-06 start.xlsx"
    fileReader(inputFile)