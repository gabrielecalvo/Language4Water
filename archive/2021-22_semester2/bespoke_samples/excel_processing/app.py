"""
To run this file you need pandas and openpyxl, you can install them by running:

python -m pip install pandas openpyxl

"""

import pandas as pd

# load data
df = pd.read_excel("raw_data.xlsx")

# process data
sum_series = df.sum()

# export data
sum_series.to_frame().to_csv("my_output.csv")
