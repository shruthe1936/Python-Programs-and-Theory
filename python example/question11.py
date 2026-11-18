import pandas as pd

# Extract
data = pd.read_csv("orders.csv")

# Transform
data = data.drop_duplicates()
data = data.dropna()

# Load
data.to_csv("cleaned_orders.csv", index=False)

print("ETL process completed")