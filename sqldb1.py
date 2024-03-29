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



import sqlite3

# Open the SQLite database connection
conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your database file name

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Define your SQL query
sql_query = "SELECT * FROM your_table_name"  # Replace 'your_table_name' with the actual table name you want to query

# Execute the query
cursor.execute(sql_query)

# Fetch and print the query result (for example, fetch the first 5 rows)
result = cursor.fetchmany(5)
for row in result:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()



#sql_query = "SELECT name FROM sqlite_master WHERE type='table';"




import pandas as pd
import sqlite3
import datetime

# Step 1: Open the SQLite database connection
conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your database file name
cursor = conn.cursor()

# Step 2: Read and save each sheet
excel_file = pd.ExcelFile('your_file.xlsx')  # Replace with your Excel file

for sheet_name in excel_file.sheet_names:
    # Step 3: Read the sheet into a DataFrame
    df = excel_file.parse(sheet_name)
    
    # Step 4: Define a table name for the sheet with a unique identifier (e.g., month-year)
    current_month_year = datetime.datetime.now().strftime('%Y_%m')
    table_name = f"{sheet_name}_{current_month_year}"
    
    # Step 5: Save the DataFrame to the SQLite database (append data if table exists)
    df.to_sql(table_name, conn, if_exists='append', index=False)

# Step 6: Close the database connection
conn.close()




