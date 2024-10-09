import pandas as pd

# Load the JSON data
data = pd.read_json('data/raw/cocktail_dataset.json')

# Print basic information about the dataset
print("Basic Information:")
print(data.info())
print("\n")

# Extract unique tags
unique_tags = set()
for tags in data['tags'].dropna():  # Drop any NaN values
    if isinstance(tags, str):  # Check if tags is a string
        tags_list = eval(tags)  # Convert string representation of list back to a list
    elif isinstance(tags, list):  # If it's already a list
        tags_list = tags
    else:
        continue  # Skip any other type
    
    unique_tags.update(tags_list)

print("Unique Tags:")
print(unique_tags)
print("\n")


# Extract unique ingredients
unique_ingredients = set()
for ingredients in data['ingredients']:
    if isinstance(ingredients, list):  # Ensure we only process lists
        for ingredient in ingredients:
            unique_ingredients.add(ingredient['name'])  # Add the name of the ingredient

print("Unique Ingredients:")
print(unique_ingredients)




# # Print descriptive statistics for all columns
# print("Descriptive Statistics:")
# print(data.describe(include='all'))  # Include all data types
# print("\n")

# # Print missing values for each column
# print("Missing Values:")
# print(data.isnull().sum())
# print("\n")

# # Print unique values and their counts for each categorical column
# print("Unique Values in Each Column:")
# for column in data.select_dtypes(include=['object']).columns:
#     print(f"\nColumn: {column}")
#     print(data[column].value_counts())
    
# # Print a summary of numerical columns
# print("\nNumerical Summary:")
# for column in data.select_dtypes(include=['int64', 'float64']).columns:
#     print(f"\nColumn: {column}")
#     print(data[column].describe())
    