import pandas as pd
import os

NON_VEGAN_INGREDIENTS = [
    'Light Cream', 'Heavy Cream', 'Whipped Cream', 'Egg Yolk', 'Egg White',
    'Honey', 'Milk', 'Gelatin'
]

NON_VEGETARIAN_INGREDIENTS = [
    'Gelatin', 'Meat'
]

NUTTY_INGREDIENTS = [
    'Amaretto', 'Nutmeg', 'Almond', 'Hazelnut', 'Peanut Butter'
]

STRONG_INGREDIENTS = [
    'Whiskey', 'Bourbon', 'Tequila', 'Vodka', 'Rum', 'Cognac', 'Gin'
]

EXPENSIVE_INGREDIENTS = [
    'Champagne', 'Cognac', 'Añejo Rum'
]

CHILLI_INGREDIENTS = [
    'Tabasco Sauce', 'Chilli'
]

CHRISTMAS_INGREDIENTS = [
    'Nutmeg', 'Cinnamon', 'Clove', 'Ginger', 'Eggnog'
]

FRUITY_INGREDIENTS = [
    'Orange', 'Lemon', 'Lime', 'Pineapple', 'Strawberries', 'Apple',
    'Grapefruit'
]

COLD_INGREDIENTS = [
    'Ice', 'Frozen'
]

DAIRY_INGREDIENTS = [
    'Milk', 'Cream', 'Butter', 'Whipped Cream', 'Yogurt'
]

SOUR_INGREDIENTS = [
    'Lemon Juice', 'Lime Juice', 'Vinegar', 'Sour Mix'
]


EXOTIC_INGREDIENTS = [
    'Passion Fruit', 'Coconut', 'Mango'
]

SWEET_INGREDIENTS = [
    'Sugar', 'Honey', 'Syrup', 'Chocolate', 'Sweet Vermouth'
]

TROPICAL_INGREDIENTS = [
    'Coconut', 'Mango', 'Pineapple', 'Passion Fruit'
]

COFFEE_INGREDIENTS = [
    'Kahlua', 'Tia Maria', 'Coffee Liqueur', 'Espresso'
]

HERBAL_INGREDIENTS = [
    'Angostura Bitters', 'Campari', 'Chartreuse', 'Benedictine', 'Mint'
]

DESSERT_INGREDIENTS = [
    'Nutmeg', 'Chocolate Ice-cream', 'Whipped Cream'
]


def add_tags(cocktail):
    """
    Function to assign appropriate tags to a cocktail based on its ingredients.

    Parameters:
    - cocktail: dict, a dictionary representing a cocktail (name, ingredients, tags).

    Returns:
    - cocktail: dict, the cocktail with additional tags assigned.
    """
    ingredients = cocktail.get('ingredients', [])
    tags = cocktail.get('tags', [])

    # Ensure tags is a list
    if tags is None:
        tags = []

    # Vegan and Vegetarian
    if not any(ingredient in NON_VEGAN_INGREDIENTS for ingredient in ingredients):
        if 'Vegan' not in tags:
            tags.append('Vegan')

    if not any(ingredient in NON_VEGETARIAN_INGREDIENTS for ingredient in ingredients):
        if 'Vegetarian' not in tags:
            tags.append('Vegetarian')

    # Nutty
    if any(ingredient in NUTTY_INGREDIENTS for ingredient in ingredients):
        if 'Nutty' not in tags:
            tags.append('Nutty')

    # Strong
    if any(ingredient in STRONG_INGREDIENTS for ingredient in ingredients):
        if 'Strong' not in tags:
            tags.append('Strong')

    # Expensive
    if any(ingredient in EXPENSIVE_INGREDIENTS for ingredient in ingredients):
        if 'Expensive' not in tags:
            tags.append('Expensive')

    # Chilli
    if any(ingredient in CHILLI_INGREDIENTS for ingredient in ingredients):
        if 'Chilli' not in tags:
            tags.append('Chilli')

    # Christmas
    if any(ingredient in CHRISTMAS_INGREDIENTS for ingredient in ingredients):
        if 'Christmas' not in tags:
            tags.append('Christmas')

    # Fruity
    if any(ingredient in FRUITY_INGREDIENTS for ingredient in ingredients):
        if 'Fruity' not in tags:
            tags.append('Fruity')

    # Cold
    if any(ingredient in COLD_INGREDIENTS for ingredient in ingredients):
        if 'Cold' not in tags:
            tags.append('Cold')

    # Dairy
    if any(ingredient in DAIRY_INGREDIENTS for ingredient in ingredients):
        if 'Dairy' not in tags:
            tags.append('Dairy')

    # Sour
    if any(ingredient in SOUR_INGREDIENTS for ingredient in ingredients):
        if 'Sour' not in tags:
            tags.append('Sour')


    # Exotic
    if any(ingredient in EXOTIC_INGREDIENTS for ingredient in ingredients):
        if 'Exotic' not in tags:
            tags.append('Exotic')

    # Sweet
    if any(ingredient in SWEET_INGREDIENTS for ingredient in ingredients):
        if 'Sweet' not in tags:
            tags.append('Sweet')

    # Tropical
    if any(ingredient in TROPICAL_INGREDIENTS for ingredient in ingredients):
        if 'Tropical' not in tags:
            tags.append('Tropical')

    # Coffee
    if any(ingredient in COFFEE_INGREDIENTS for ingredient in ingredients):
        if 'Coffee' not in tags:
            tags.append('Coffee')

    # Herbal
    if any(ingredient in HERBAL_INGREDIENTS for ingredient in ingredients):
        if 'Herbal' not in tags:
            tags.append('Herbal')

    # Dessert
    if any(ingredient in DESSERT_INGREDIENTS for ingredient in ingredients):
        if 'Dessert' not in tags:
            tags.append('Dessert')

    # Alcoholic - remove this tag if it exists
    if 'Alcoholic' in tags:
        tags.remove('Alcoholic')
        

    # Save tags
    cocktail['tags'] = tags
    return cocktail


# Load data from a JSON file
def load_data(file_path):
    return pd.read_json(file_path)




# Save processed data to a JSON file
def save_data(data, output_path):
    data.to_json(output_path, orient='records', lines=False) 



# Process cocktails to add tags
def process_cocktails(data):
    processed_cocktails = []
    for cocktail in data:
        processed_cocktail = add_tags(cocktail)
        processed_cocktails.append(processed_cocktail)
    return processed_cocktails


# Main function
def main():
    # Input and output file paths
    input_file = './data/raw/cocktail_dataset.json'
    output_file = './data/processed/processed_data.json'

    # Load the data
    data = load_data(input_file)

    # Process the cocktails
    processed_data = process_cocktails(data.to_dict(orient='records'))

    # Save the processed data
    save_data(pd.DataFrame(processed_data), output_file)
    print(f'Processed data has been saved to: {output_file}')


if __name__ == "__main__":
    main()