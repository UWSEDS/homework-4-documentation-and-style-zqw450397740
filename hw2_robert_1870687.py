"""
CSE583_HW2
Robert Chang_1870687
This module provides two functions: read_create_dataframe(str) and test_create_dateframe(DataFrame, list).
  The former creates a new pandas DataFrame based on the url the user inputs. The latter tests if the
  DataFrame meet the following conditions:
      1. The DataFrame only contains the columns specified in the list;
      2. The values in each column have the same python type;
      3. There are at least 10 rows in the DataFrame.
"""
import pandas as pd


# returns a pandas DataFrame based on the file downloaded from the url
def read_create_dataframe(url):
    return pd.read_csv(url)


# returns True if the DataFrame meets the 3 conditions above meanwhile; return False if not
def test_create_dataframe(theFrame, list_names):
    for column_name in theFrame.columns:
        if column_name not in list_names:
            return False
    for column_name in theFrame.columns:
        type_init = type(theFrame[column_name][0])
        for i in range(1, len(theFrame.index)):
            if type_init != type(theFrame[column_name][i]):
                return False
    return len(theFrame.index) >= 10


