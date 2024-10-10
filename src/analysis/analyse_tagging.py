import pandas as pd

# Load the JSON data
data = pd.read_json('data/processed/processed_data.json')

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
