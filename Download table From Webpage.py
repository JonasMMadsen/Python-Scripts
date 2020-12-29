# Based on https://medium.com/@ageitgey/quick-tip-the-easiest-way-to-grab-data-out-of-a-web-page-in-python-7153cecfca58

import pandas as pd

# Input parameters
url = "https://www.w3schools.com/html/html_tables.asp"
outputDirectory = "D:\\"
addHeaders = True
outputSeparator = ';'


tables = pd.read_html(url)

index = 1
for table in tables:
    print("---- Table " + str(index) + " ----")
    print(table)
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
    table.to_csv(outputDirectory + "Table" + str(index) + ".csv", index=addHeaders, sep=outputSeparator, )
    index = index + 1

#calls_df, = pd.read_html(url, header=0)
#print(calls_df)