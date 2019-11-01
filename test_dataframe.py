"""
CSE583_HW3
Robert Chang_1870687
This python extends hw2 by importing the module, hw2_Robert_1870687.py
    and adds 3 tests:
    1. Check that all columns have values of the correct type;
    2. Check for nan values;
    3. Verify that the dataframe has at least one row.
The python prompts the user to input the source of data that he wants to
test and runs the test from HW2 and the 3 tests above in order. The test
results are printed on the console
"""
import math
import numbers
import hw2_robert_1870687 as HW2


def test_1(data_frame):
    """
    The function takes a pandas dataframe as the parameter and returns
        a list of string that contains the names of the columns whose
        values have incorrect type. It returns an empty list if values in each
        column have correct types
    """
    wrong_columns = []
    for column_name in data_frame.columns:
        init_type = type(data_frame[column_name][0])
        for j in range(1, len(data_frame.index)):
            if init_type != type(data_frame[column_name][j]):
                wrong_columns.append(column_name)
                break
    return wrong_columns


def test_2(data_frame):
    """
    The function takes a pandas dataframe and returns a list of string
        that contains the names of the columns which have nan values.
        The list is empty if there is no nan in each column
    """
    nan_columns = []
    for column_name in data_frame.columns:
        for j in range(1, len(data_frame.index)):
            if isinstance(data_frame[column_name][j], numbers.Number):
                if math.isnan(data_frame[column_name][j]):
                    nan_columns.append(column_name)
                    break
    return nan_columns


# creates the dataframe from module HW2 based on the link the user provides.
DATA_SOURCE = str(input("Enter the website or the source of data you want to test: "))
DF = HW2.read_create_dataframe(DATA_SOURCE)

# prompts the user to enter the list containing the names of columns to be checked in HW2
N = int(input("Enter the number of elements in the list that contains names you want to "
              "check(Enter 0 if you want to use the original columns of the dataframe): "))
NAMES_COLUMNS = []
if N == 0:
    NAMES_COLUMNS = DF.columns
else:
    for i in range(0, N):
        ele = str(input("Enter the name of column " + str(i+1) + ": "))
        NAMES_COLUMNS.append(ele)

# tests if the dataframe match up to all of the 3 conditions in HW2
RESULT_TEST_HW2 = HW2.test_create_dataframe(DF, NAMES_COLUMNS)
if RESULT_TEST_HW2:
    print("The dataframe meet 3 conditions in HW2.")
else:
    print("The dataframe DOESN'T meet the 3 conditions simultaneously in HW2!")

# runs test_1 with the introduced dataframe and prints results
RESULT_TEST_1 = test_1(DF)
COUNT_PASSED = 0
if len(RESULT_TEST_1) == 0:
    print("Pass. All columns have values of the correct type.")
    COUNT_PASSED += 1
else:
    print("Fail. The column(s)--" + ', '.join(RESULT_TEST_1)
          + "--contains value(s) with incorrect type!")

# runs test_2 with the introduced dataframe and prints results
RESULT_TEST_2 = test_2(DF)
if len(RESULT_TEST_2) == 0:
    print("Pass. There is no nan value in all columns.")
    COUNT_PASSED += 1
else:
    print("Fail. The column(s)--" + ', '.join(RESULT_TEST_2)
          + "--contains nan value(s)!")

# runs the test 3 and prints the final results
if len(DF.index) >= 1:
    print("Pass. The dataframe has at least one row.")
    COUNT_PASSED += 1
else:
    print("Fail. The dataframe has no row!")
print("You passed " + str(COUNT_PASSED) + " of 3 tests. ")
