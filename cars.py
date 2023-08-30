import pandas as pd

data = {
    'Car': ['Toyota', 'rav4', 'corolla', 'Tesla', 'model x', 'model y', 'Lexus', 'nx300', 'nx400'],
    'Total': [400, 200, 200, 300, 100, 200, 100, 30, 70],
}

df = pd.DataFrame(data)

sample = {
    'Car': ['Toyota', 'Tesla', 'Lexus'],
    'Total': [40, 20, 10],
}

sample_df = pd.DataFrame(sample)

result_rows = []

for index, row in df.iterrows():
    result_rows.append(row)
    if row['Car'] in sample_df['Car'].values:
        sample_row = sample_df[sample_df['Car'] == row['Car']].iloc[0]
        result_rows.append(sample_row)

result_df = pd.DataFrame(result_rows)

print(result_df)
