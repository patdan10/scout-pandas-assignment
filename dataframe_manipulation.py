"""
The module for the program used to edit the dataframe for excel
Author: Patrick Danielson
"""

#imports
import pandas as pd
import numpy as np

# Method to add timestamp flag to dataframe of information,
#    indicating if timestamp data was present originally
# Input: dataframe
# Output: dataframe with 'timestamp_flag' present
def appendTimeFlag(df):
    flags = [0]*len(df)
    df['timestamp_flag'] = flags

# Method to add VTWS flag to dataframe of information,
#    indicating if VTWS data was present originally
# Input: dataframe
# Output: dataframe with 'timestamp_flag' present
def appendVTWSFlag(df):
    flags = [0]*len(df)
    df['data_qc_flag_VTWS_AVG'] = flags

# Method to add new timestamps with correct IDs and indices to dataframe
# Input: Dataframe and times to add
# Output: Dataframe with times added, with correct IDs and indices
def addNewTimes(df, times):
    # Adds new information
    for t in times:
        df.loc[len(df)] = [None, t, None, None, None, None, None, 1]
    
    # Sorts values, resetting the indices to be correct
    df.sort_values(by=['time'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    # Sets the ID to be correct
    df['id'] = df.index
    
    # Drops the generated index column
    df.drop(df.columns[2], axis=1)


# Method to set new VTWS flags with Erroneous or null, depending on if value were present or not
# Input: Dataframe
# Output: Dataframe column edited to say erroneous where VTWS is not present
def updateVTWSFlag(df):
    df['data_qc_flag_VTWS_AVG'] = np.where(df.VTWS_AVG.isnull(), "Erroneous", None)