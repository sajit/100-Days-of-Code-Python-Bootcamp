from pathlib import Path

import pandas as pd


csv_path = Path(__file__).with_name("2018_CP_Squirrel.csv")
squirrel_data = pd.read_csv(csv_path)

# Count squirrel records for each recorded primary fur color. Rows with no
# recorded fur color are excluded by groupby.
fur_color_counts = (
    squirrel_data.groupby("Primary Fur Color")
    .size()
    .reset_index(name="Count")
    .rename(columns={"Primary Fur Color": "Fur Color"})
)

print(fur_color_counts)
