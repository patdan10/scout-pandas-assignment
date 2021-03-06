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
def fileReader(inputFile, outputFile, dstActive):
    df = pd.read_excel(inputFile)
    
    # Create time column
    em.appendTimeFlag(df)
    
    # Generate missing times, by finding 
    times = tg.makeTimes(df['time'].tolist(), dstActive)
    
    # Add missing times to excel file
    em.addNewTimes(df, times)
    
    # Create and update VTWS Flags for missing values
    em.appendVTWSFlag(df)
    em.updateVTWSFlag(df)
    
    # Export file
    df.to_excel(outputFile, index=False)

# Main function, to ensure correct running enviroment.
# Please replace inputFile, outputFile, and dstActive to the desired variables.
# Set inputFile to input excel file, outputFile to desired output location,
#     and dstActive to whether DST is recognized in the given area (On by default)
if __name__ == '__main__':
    inputFile = '/Users/patrick/Desktop/test 2021-05-06 start.xlsx'
    outputFile = '/Users/patrick/Desktop/check results.xlsx'
    dstActive = True
    fileReader(inputFile, outputFile, dstActive)
