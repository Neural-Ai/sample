import pandas as pd
from scipy.stats import zscore

# create a sample DataFrame
df = pd.DataFrame({'A': [10, 20, 30], 'B': [20, 30, 40], 'C': [30, 40, 50]})

# apply the z-score function to the DataFrame
df_zscore = df.apply(zscore)

# print the original and z-score DataFrames
print("Original DataFrame:")
print(df)
print("\nZ-score DataFrame:")
print(df_zscore)
