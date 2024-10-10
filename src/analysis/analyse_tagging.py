import pandas as pd
import json
import logging

# Configure logging with a custom format
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(message)s')


def load_data(file_path):
    """Load JSON data from a specified file."""
    try:
        data = pd.read_json(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None


def extract_unique_tags(data):
    """Extract unique tags from the dataset."""
    unique_tags = set()
    for tags in data['tags'].dropna():
        if isinstance(tags, str):
            tags_list = json.loads(tags)  # Safe alternative to eval
        elif isinstance(tags, list):
            tags_list = tags
        else:
            continue

        unique_tags.update(tags_list)
    logging.debug(f"Extracted unique tags: {unique_tags}")
    return unique_tags


def extract_unique_ingredients(data):
    """Extract unique ingredients from the dataset."""
    unique_ingredients = set()
    for ingredients in data['ingredients']:
        if isinstance(ingredients, list):
            for ingredient in ingredients:
                unique_ingredients.add(ingredient['name'])
    logging.debug(f"Extracted unique ingredients: {unique_ingredients}")
    return unique_ingredients


def summarize_findings(data):
    """Summarize findings regarding vegetarian and vegan tags."""
    vegetarian_not_vegan = data[data['tags'].str.contains('Vegetarian', na=False) &
                               ~data['tags'].str.contains('Vegan', na=False)]

    if vegetarian_not_vegan.empty:
        logging.info("All vegetarian drinks are also vegan.")
    else:
        logging.warning(f"Some vegetarian drinks are not vegan: {vegetarian_not_vegan['name'].tolist()}")


def main():
    data = load_data('data/processed/processed_data.json')

    if data is not None:
        logging.debug("Basic Information:")
        logging.debug(data.info())

        unique_tags = extract_unique_tags(data)
        logging.info("Unique Tags extracted successfully.")

        unique_ingredients = extract_unique_ingredients(data)
        logging.info("Unique Ingredients extracted successfully.")

        summarize_findings(data)
    else:
        logging.critical("No data loaded. Exiting program.")


if __name__ == "__main__":
    main()
