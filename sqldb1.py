import xlrd
from sqlite3 import connect

# Open the Excel file
wb = xlrd.open_workbook('alerts_report.xlsx')

# Get the number of sheets in the workbook
num_sheets = wb.nsheets

# Connect to the SQLite database
conn = connect('alerts_report.db')
cursor = conn.cursor()

# Loop through each sheet in the workbook
for i in range(num_sheets):
    # Read the data from the current sheet
    sh = wb.sheet_by_index(i)

    # Insert the data into the corresponding column of the "Alerts" table
    cursor.execute("INSERT INTO Alerts VALUES (%s)", [sh.name])

# Close the connection to the database
conn.close()
