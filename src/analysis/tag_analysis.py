import pandas as pd
import logging
import hydra
from omegaconf import DictConfig, OmegaConf
from collections import Counter

# Configure logging with a custom format
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def load_data(file_path):
    """Load JSON data from a specified file."""
    try:
        data = pd.read_json(file_path)
        logging.debug("Data loaded successfully.")
        return data
    except Exception as e:
        logging.critical(f"Error loading data: {e}")
        return None

def analyze_tags(data):
    """Analyze tags and print unique values."""
    logging.debug("Analyzing tags used in cocktails...")

    # Flatten the tags if they're stored in lists
    tags_flat = data['tags'].explode().dropna()

    unique_tags = tags_flat.unique()
    logging.info(f"Unique tags in the dataset: {unique_tags}")

    return unique_tags

def tag_counter(data):
    tag_counts = Counter()
    for tags in data['tags']:
        tag_counts.update(tags)
    # Convert to DataFrame for better visualization
    tag_counts_df = pd.DataFrame(tag_counts.items(), columns=['Tag', 'Count'])
    print(tag_counts_df)

@hydra.main(version_base=None, config_path="../../configs/analysis_configs", config_name="tag_analysis_config")
def main(cfg: DictConfig):
    # Load global config (data_type)
    global_config = OmegaConf.load("configs/global_configs.yaml")

    if global_config.data_type == 'raw':
        file_path = 'data/raw/cocktail_dataset.json'
    elif global_config.data_type == 'processed':
        file_path = 'data/processed/tagged_cocktail_dataset.json'
    else:
        logging.error("Invalid data type specified in global config. Use 'raw' or 'processed'.")
        return None

    # Load data if enabled in config
    if cfg.functions.load_data:
        data = load_data(file_path)
    else:
        logging.info("Data loading is disabled.")
        return None
    
    tag_counter(data)

    if data is not None and cfg.functions.analyze_tags:
        unique_tags = analyze_tags(data)
    else:
        logging.info("Tag analysis is disabled or no valid data found.")

if __name__ == "__main__":
    main()
