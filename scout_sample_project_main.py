"""
The main method for the program used to edit an excel file
of wind turbine information
Author: Patrick Danielson
"""


# Imports
import pandas as pd
import time_generation as tg
import dataframe_manipulation as em

# Method in progress to create new excel file with conditions given
# Input: Excel file
# Output: Creates file on desktop
def fileReader(inputFile):
    df = pd.read_excel(inputFile)
    
    #Create columns
    em.appendTimeFlag(df)
    em.appendVTWSFlag(df)
    
    #Generate missing times
    times = tg.makeTimes(df.iloc[0]['time'], df.iloc[-1]['time'], df['time'].tolist())
    
    #Add missing times to excel file
    em.addNewTimes(df, times)
    df.to_excel('/Users/patrick/Desktop/OUTPUT.xlsx', index=False)

# Main function, to ensure correct running enviroment.
if __name__ == '__main__':
    inputFile = '/Users/patrick/Desktop/test 2021-05-06 start.xlsx'
    fileReader(inputFile)
