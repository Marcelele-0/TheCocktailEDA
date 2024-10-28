import pandas as pd
import logging
import hydra
from omegaconf import DictConfig, OmegaConf

# Configure logging with a custom format
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(message)s')

def load_data(file_path):
    """Load JSON data from a specified file."""
    try:
        data = pd.read_json(file_path)
        logging.debug("Data loaded successfully.")
        return data
    except Exception as e:
        logging.critical(f"Error loading data: {e}")
        return None

def analyze_ingredients(data):
    """Analyze ingredients and their properties."""
    logging.debug("Analyzing ingredients used in cocktails...")

    # Flatten the ingredients
    ingredients_flat = data['ingredients'].explode().dropna()

    # Ensure that ingredients are dictionaries to extract their attributes
    if ingredients_flat.apply(lambda x: isinstance(x, dict)).all():
        ingredients_df = pd.json_normalize(ingredients_flat)

        # Display basic statistics for ingredient attributes
        logging.info("Basic statistics for ingredients:")
        stats = ingredients_df.describe(include='all')  # Include all data types
        logging.info(f"\n{stats}\n")  # Log stats

        logging.debug(f"Available columns in ingredients_df: {ingredients_df.columns.tolist()}")
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

def print_unique_ingredients(ingredients_df):
    """Print unique ingredients in the dataset."""
    unique_ingredients = ingredients_df['name'].unique()
    unique_ingredients = [ingredient.replace("ñ", "n") for ingredient in unique_ingredients]

    logging.info(f"Unique ingredients in the dataset: {unique_ingredients}")

def print_strong_alcohol_ingredients(ingredients_df):
    """Print unique ingredients with a high alcohol content."""
    # Filter for ingredients where 'percentage' is high
    strong_alcohol = ingredients_df[ingredients_df['percentage'] > 30]

    if not strong_alcohol.empty:
        logging.info("Unique ingredients with high alcohol content:")
        
        # Replace 'ñ' with 'n' using .loc to avoid SettingWithCopyWarning
        strong_alcohol.loc[:, 'name'] = strong_alcohol['name'].str.replace("ñ", "n")

        # Get unique combinations of ID and Name
        unique_ingredients = strong_alcohol[['id', 'name']].drop_duplicates()
        
        for index, row in unique_ingredients.iterrows():
            logging.info(f"ID: {row['id']}, Name: {row['name']}")
    else:
        logging.info("No ingredients with high alcohol content found.")


def print_alcohol_ingredients(ingredients_df):
    """Print unique ingredients with a high alcohol content."""
    # Filter for ingredients where 'percentage' is high
    strong_alcohol = ingredients_df[ingredients_df['percentage'] > 0] 

    if not strong_alcohol.empty:
        logging.info("Unique ingredients with high alcohol content:")
        
        # Replace 'ñ' with 'n' using .loc to avoid SettingWithCopyWarning
        strong_alcohol.loc[:, 'name'] = strong_alcohol['name'].str.replace("ñ", "n")

        # Get unique combinations of ID and Name
        unique_ingredients = strong_alcohol[['id', 'name']].drop_duplicates()
        
        for index, row in unique_ingredients.iterrows():
            logging.info(f"ID: {row['id']}, Name: {row['name']}")
    else:
        logging.info("No ingredients with high alcohol content found.")



@hydra.main(version_base=None, config_path="../../configs/analysis_configs", config_name="ingredient_analysis_config")
def main(cfg: DictConfig):
    # Load global config (data_type)
    global_config = OmegaConf.load("configs/global_configs.yaml")

    # Global selection of data type: raw or processed
    if global_config.data_type == 'raw':
        file_path = 'data/raw/cocktail_dataset.json'
    elif global_config.data_type == 'processed':
        file_path = 'data/processed/processed_cocktail_dataset.json'
    else:
        logging.error("Invalid data type specified in global config. Use 'raw' or 'processed'.")
        return None

    # Load data if enabled in config
    if cfg.functions.load_data:
        data = load_data(file_path)
    else:
        logging.info("Data loading is disabled.")
        return None

    if data is not None:
        # Analyze ingredients if enabled in config
        if cfg.functions.analyze_ingredients:
            ingredients_df = analyze_ingredients(data)
        else:
            ingredients_df = None
            logging.info("Ingredient analysis is disabled.")
        
        # Print ingredients without alcohol if enabled in config
        if ingredients_df is not None and cfg.functions.print_ingredients_without_alcohol:
            print_ingredients_without_alcohol(ingredients_df)
        else:
            logging.info("Printing ingredients without alcohol is disabled or no valid ingredient data.")

        # Print unique ingredients if enabled in config
        if ingredients_df is not None and cfg.functions.print_unique_ingredients:
            print_unique_ingredients(ingredients_df)
        else:
            logging.info("Printing unique ingredients is disabled or no valid ingredient data.")

        # Print ingredients with high alcohol content if enabled in config
        if ingredients_df is not None and cfg.functions.print_strong_alcohol_ingredients:
            print_strong_alcohol_ingredients(ingredients_df)
        else:
            logging.info("Printing ingredients with high alcohol content is disabled or no valid ingredient data.")

        
        # Print ingredients with any alcohol content if enabled in config
        if ingredients_df is not None and cfg.functions.print_strong_alcohol_ingredients:
            print_alcohol_ingredients(ingredients_df)
        else:
            logging.info("Printing ingredients with high alcohol content is disabled or no valid ingredient data.")
    else:
        logging.error("No data to analyze.")

if __name__ == "__main__":
    main()
