from pathlib import Path
import pandas as pd
from io import StringIO

path = r"C:\Users\madsm\Documents\Sports Interactive\Football Manager 2024\Untitled.html"
html_text = Path(path).read_text(encoding="utf-8")

tables = pd.read_html(StringIO(html_text))
df = pd.read_csv("player_data.csv")

# Saves player data into a CSV file
for i, table in enumerate(tables):
    table.to_csv(f"player_data.csv", index=False)






# Clean player data
cols_to_clean = ["Wage", "Transfer Value"]
for col in cols_to_clean:
    df[col] = df[col].str.replace("Kr", "", regex=False)
    df[col] = df[col].str.replace("p/w", "", regex=False)

df.to_csv("player_data.csv", index=False)


