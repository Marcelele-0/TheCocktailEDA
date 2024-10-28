import hydra
from omegaconf import DictConfig, OmegaConf
import logging
import pandas as pd

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def assign_tags(ingredients, tags_definitions):
    """Assigns tags to a cocktail based on its ingredients and tag thresholds."""
    assigned_tags = []
    for tag_def in tags_definitions:
        tag, tag_ingredients, threshold = tag_def['tag'], set(tag_def['ingredients']), tag_def['threshold']
        if len(ingredients & tag_ingredients) >= threshold:
            assigned_tags.append(tag)
    return assigned_tags

@hydra.main(config_path="../../configs/preprocessing_configs", config_name="tagging_config")
def main(cfg: DictConfig):
    tags_definitions = cfg.tags_definitions
    
    # Load global config (data_type)
    global_config = OmegaConf.load("configs/global_configs.yaml")

    # Select data file based on data type in global config
    if global_config.data_type == 'raw':
        file_path = 'data/raw/cocktail_dataset.json'
    elif global_config.data_type == 'processed':
        file_path = 'data/processed/processed_cocktail_dataset.json'
    else:
        logging.error("Invalid data type specified in global config. Use 'raw' or 'processed'.")
        return None

    # Load data
    try:
        cocktails = pd.read_json(file_path)
    except Exception as e:
        logging.critical(f"Error loading data: {e}")
        return None

    # Process each cocktail in the dataset
    for _, cocktail in cocktails.iterrows():
        ingredients = set(cocktail['ingredients'])  # Assuming 'ingredients' is a list
        assigned_tags = assign_tags(ingredients, tags_definitions)
        logging.info(f"Cocktail: {cocktail['name']}, Assigned Tags: {assigned_tags}")

if __name__ == "__main__":
    main()
