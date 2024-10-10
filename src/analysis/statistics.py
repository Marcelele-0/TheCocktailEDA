
import pandas as pd

# Load the JSON data
data = pd.read_json('data/processed/processed_data.json')

# Print descriptive statistics for all columns
print("Descriptive Statistics:")
print(data.describe(include='all'))  # Include all data types
print("\n")