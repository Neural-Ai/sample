import pandas as pd
import sqlite3

# Open the SQLite database connection
conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your desired database file name
cursor = conn.cursor()

# Open the Excel file
excel_file = pd.ExcelFile('your_file.xlsx')  # Replace with your Excel file

# Iterate through the sheet names in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the sheet into a DataFrame
    df = excel_file.parse(sheet_name)
    
    # Define a table name for the sheet (you can customize this)
    table_name = sheet_name.replace(' ', '_')  # Ensure no spaces in table names
    
    # Save the DataFrame to the SQLite database
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the SQLite database connection
conn.close()
In this modified code, we open the SQLite database connection before iterating through the sheet names and save each sheet as a separate table in the same SQLite database. Finally, we close the connection when we're done saving all the sheets.

Now, all the sheets will be stored as individual tables within the same SQLite database file specified in 'your_database.db'.





