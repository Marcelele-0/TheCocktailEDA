import pandas as pd
import logging

# Configure logging with a custom format
logging.basicConfig(level=logging.DEBUG,
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

        logging.info(f"Available columns in ingredients_df: {ingredients_df.columns.tolist()}")
        return ingredients_df  # Return the DataFrame for further analysis
    else:
        logging.warning("No valid ingredient dictionaries found.")
        return None  # Return None if no valid data found

def print_ingredients_without_alcohol(ingredients_df):
    """Print ingredients that do not have assigned alcohol content (NaN)."""
    # Filter for ingredients where 'alcohol' is NaN
    missing_alcohol = ingredients_df[ingredients_df['alcohol'].isna()]
    
    # Print unique values in the 'alcohol' column
    unique_alcohol_values = ingredients_df['alcohol'].unique()
    logging.debug(unique_alcohol_values)
    # Print the first few rows of the 'alcohol' column
    logging.debug("First few values in 'alcohol' column:")
    logging.debug(ingredients_df['alcohol'].head())

    if not missing_alcohol.empty:
        logging.info("Ingredients without assigned alcohol content (NaN):")
        for index, row in missing_alcohol.iterrows():
            logging.info(f"ID: {row['id']}, Name: {row['name']}")
    else:
        logging.info("All ingredients have assigned alcohol content.")

def main():
    data = load_data('data/raw/cocktail_dataset.json')

    if data is not None:
        ingredients_df = analyze_ingredients(data)  # Get the DataFrame for ingredients
        if ingredients_df is not None:  # Ensure the DataFrame is valid
            print_ingredients_without_alcohol(ingredients_df)  # Call the function to print ingredients without alcohol
        else:
            logging.error("No valid ingredients data to analyze.")
    else:
        logging.error("No data to analyze.")

if __name__ == "__main__":
    main()
