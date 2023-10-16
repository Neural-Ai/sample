import pandas as pd

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'Alert Name': ['Alert 1', 'Alert 2', 'Alert 3', 'Alert 4'],
    'January': [10, 5, 0, 0],
    'February': [8, 0, 0, 0],
    'March': [12, 0, 0, 0],
    'April': [9, 0, 0, 0],
}

df = pd.DataFrame(data)

# Sum the counts for each alert across all months
df['Total'] = df.sum(axis=1)

# Filter alerts with a total count of 0
zero_count_alerts = df[df['Total'] == 0]

# Select only the 'Alert Name' column to get the alerts with zero counts
result = zero_count_alerts['Alert Name']

# Print the alerts with zero counts
print(result)
