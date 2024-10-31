import hydra
from omegaconf import DictConfig, OmegaConf
import logging
import pandas as pd

# Configuring logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


def assign_classic_tags(cocktail, classic_definitions):
    """
    Assign classic, contemporary classic, or new era tags to a cocktail based on ingredient structure.

    Parameters:
    cocktail (dict): The cocktail data.
    classic_definitions (list): Definitions for classic tags.
    
    Returns:
    list: List of assigned tags.
    """
    ingredients_map = {definition['tag']: definition['ingredients'] for definition in classic_definitions}

    classic_ingredients = ingredients_map.get('Classic', [])
    new_era_ingredients = ingredients_map.get('NewEra', [])

    classic_count = 0
    new_era_count = 0

    for ingredient in cocktail['ingredients']:
        if ingredient.get('name') in classic_ingredients:
            classic_count += 1
        elif ingredient.get('name') in new_era_ingredients:
            new_era_count += 1

    if classic_count > 0 and new_era_count == 0:
        return ['Classic']
    elif classic_count > 0 and new_era_count == 1:
        return ['ContemporaryClassic']
    elif new_era_count >= 2:
        return ['NewEra']

    return []


def assign_vegan_vegetarian_tags(cocktail, vegan_definitions):
    """
    Assign vegan or vegetarian tags by excluding non-vegan/vegetarian ingredients.

    Parameters:
    cocktail (dict): The cocktail data.
    vegan_definitions (list): Definitions for vegan and vegetarian tags.
    
    Returns:
    list: List of assigned tags.
    """
    vegan_map = {definition['tag']: definition['ingredients'] for definition in vegan_definitions}

    non_vegan_ingredients = vegan_map.get('NonVegan', [])
    non_vegetarian_ingredients = vegan_map.get('NonVegetarian', [])

    vegan = True
    vegetarian = True

    for ingredient in cocktail['ingredients']:
        if ingredient.get('name') in non_vegan_ingredients:
            vegan = False
        if ingredient.get('name') in non_vegetarian_ingredients:
            vegetarian = False

    tags = []
    if vegan:
        tags.append('Vegan')
    if vegetarian:
        tags.append('Vegetarian')

    return tags


def assign_other_tags(cocktail, other_definitions):
    """
    Assign other tags based on additional definitions.

    Parameters:
    cocktail (dict): The cocktail data.
    other_definitions (list): Definitions for other tags.
    
    Returns:
    list: List of assigned tags.
    """
    other_tags_map = {definition['tag']: definition['ingredients'] for definition in other_definitions}

    tags = []
    for ingredient in cocktail['ingredients']:
        for tag, ingredients in other_tags_map.items():
            if ingredient.get('name') in ingredients:
                tags.append(tag)

    return tags


def save_simplified_data(df, file_path):
    """
    Save the simplified DataFrame to a JSON file.

    Parameters:
    df (DataFrame): The DataFrame to save.
    file_path (str): The file path to save the JSON file.
    """
    df.to_json(file_path, orient='records', indent=4)


@hydra.main(version_base=None, config_path="../../configs/preprocessing_configs", config_name="tagging_config")
def main(cfg: DictConfig):
    global_config = OmegaConf.load("configs/global_configs.yaml")

    # Select data file based on data type in global config
    input_file = 'data/raw/cocktail_dataset.json' if global_config.data_type == 'raw' else 'data/processed/processed_cocktail_dataset.json'
    output_file = 'data/processed/processed_cocktail_dataset.json'

    # Load data
    try:
        cocktails = pd.read_json(input_file)
    except Exception as e:
        logging.critical(f"Error loading data: {e}")
        return None

    # Process each cocktail in the dataset
    tags_column = []
    for _, cocktail in cocktails.iterrows():
        # Clear existing tags for the cocktail
        cocktail['tags'] = []

        # Assign tags
        tags = []

        # Assign classic tags if enabled in config
        if cfg.functions.assign_classic_tags:
            tags.extend(assign_classic_tags(cocktail, cfg.tags_definitions.classic_tags))

        # Assign vegan and vegetarian tags if enabled in config
        if cfg.functions.assign_vegan_vegetarian_tags:
            tags.extend(assign_vegan_vegetarian_tags(cocktail, cfg.tags_definitions.vegan_vegetarian_tags))

        # Assign other tags if enabled in config
        if cfg.functions.assign_other_tags:
            tags.extend(assign_other_tags(cocktail, cfg.tags_definitions.other_tags))

        # Remove duplicate tags and add to cocktail's tags
        unique_tags = list(set(tags))
        cocktail['tags'] = unique_tags
        tags_column.append(unique_tags)

    # Assign the tags to the DataFrame
    cocktails['tags'] = tags_column

    # Save updated data
    logging.info("Saving tagged data to %s", output_file)
    save_simplified_data(cocktails, output_file)
    logging.info("Data processing complete!")


if __name__ == "__main__":
    main()
