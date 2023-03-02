import csv
from prettytable import PrettyTable

# Example CSV data stored in a variable
csv_data = 'Name,Age,City\nJohn,25,New York\nJane,30,Los Angeles\n'

# Parse the CSV data and create a list of rows
rows = list(csv.reader(csv_data.splitlines()))

# Create a table with column names
table = PrettyTable()
table.field_names = rows[0]

# Add rows to the table
for row in rows[1:]:
    table.add_row(row)

# Print the table
print(table)
