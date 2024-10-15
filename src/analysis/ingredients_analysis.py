import pandas as pd
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
        logging.critical(f"Error loading data: {e}")
        return None

def analyze_ingredients(data):
    """Analyze ingredients and their properties."""
    logging.info("Analyzing ingredients used in cocktails...")

    # Flatten the ingredients
    ingredients_flat = data['ingredients'].explode().dropna()

    # Ensure that ingredients are dictionaries to extract their attributes
    if ingredients_flat.apply(lambda x: isinstance(x, dict)).all():
        ingredients_df = pd.json_normalize(ingredients_flat)

        # Display basic statistics for ingredient attributes
        logging.info("Basic statistics for ingredients:")
        stats = ingredients_df.describe(include='all')  # Include all data types
        logging.info(f"\n{stats}\n")  # Log stats

    else:
        logging.warning("No valid ingredient dictionaries found.")

def main():
    data = load_data('data/raw/cocktail_dataset.json')
    if data is not None:
        analyze_ingredients(data)  # Call the ingredient analysis function
    else:
        logging.error("No data to analyze.")

if __name__ == "__main__":
    main()
