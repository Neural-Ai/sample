import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})

# Write the DataFrame to an Excel file with xlsxwriter engine
with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1', header=True)

    # Get the workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Set the cell alignment to left for all cells
    cell_format = workbook.add_format({'align': 'left'})
    worksheet.set_default_row(15, cell_format=cell_format)
