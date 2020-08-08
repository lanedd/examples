import pandas as pd
from datetime import datetime, date

# Example taken from https://xlsxwriter.readthedocs.io/working_with_pandas.html

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15],
                   'Date and time': [datetime(2015, 1, 1, 11, 30, 55),
                                     datetime(2015, 1, 2, 1,  20, 33),
                                     datetime(2015, 1, 3, 11, 10    ),
                                     datetime(2015, 1, 4, 16, 45, 35),
                                     datetime(2015, 1, 5, 12, 10, 15)],
                   'Dates only':    [date(2015, 2, 1),
                                     date(2015, 2, 2),
                                     date(2015, 2, 3),
                                     date(2015, 2, 4),
                                     date(2015, 2, 5)],
                   'Percentages': [0.30, 0.50, 0.24, 0.90, 0.12]
                   })


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx',
                        engine='xlsxwriter',
                        # datetime_format='mmm d yyyy hh:mm:ss',
                        datetime_format='yyyy-mm-dd',
                        date_format='mmmm dd yyyy')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=None)

# Get the xlsxwriter objects from the dataframe writer object.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Set Column Width
worksheet.set_column('B:C', 20)

# Set the column width and format.
format1 = workbook.add_format({'num_format': '0.0%'})
worksheet.set_column('D:D', 18, format1)

# Apply a conditional format to the cell range.
worksheet.conditional_format('A2:A8', {'type': '3_color_scale'})
worksheet.conditional_format('D2:D8', {'type': '3_color_scale'})

# Close the Pandas Excel writer and output the Excel file.
writer.save()
