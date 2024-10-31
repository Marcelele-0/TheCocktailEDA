import hydra
from omegaconf import DictConfig, OmegaConf
import logging
import pandas as pd
import numpy as np
import os  # Ensure we can handle directory creation

# Configuring logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def create_tag_vector(tags, tags_indices):
    """Create a binary vector based on tags and indices."""
    if not tags or not isinstance(tags, list):
        return np.zeros(max(tags_indices.values()) + 1, dtype=int)  # Return zero vector if tags is None or not iterable

    vector = np.zeros(max(tags_indices.values()) + 1, dtype=int)
    for tag in tags:
        index = tags_indices.get(tag)
        if index is not None:
            vector[index] = 1
    return vector

def one_hot_encode_tags(cocktails_df, tags_column, output_column, tags_indices):
    """Generate one-hot encoding for tags based on tags_indices."""
    cocktails_df[output_column] = cocktails_df[tags_column].apply(
        lambda tags: create_tag_vector(tags, tags_indices).tolist()
    )
    return cocktails_df

def save_encoded_data(df, file_path):
    """Save the DataFrame with one-hot encoded tags to a JSON file."""
    df.to_json(file_path, orient='records', indent=4)
    logging.info("Data saved successfully to %s", file_path)  # Log success

@hydra.main(version_base=None, config_path="../../configs/preprocessing_configs", config_name="one_hot_encoding_config")
def main(cfg: DictConfig):
    # Load global configuration
    global_config = OmegaConf.load("configs/global_configs.yaml")

    # Access tags indices directly from the config
    tags_indices = cfg.tags_indices

    # Select data file based on data type in global config
    input_file = 'data/processed/tagged_cocktail_dataset.json' if global_config.data_type == 'processed' else 'data/raw/cocktail_dataset.json'
    output_file = 'data/processed/one_hot_encoded_cocktail_dataset.json'

    # Load data
    try:
        cocktails = pd.read_json(input_file)
        logging.info("Loaded data successfully from %s", input_file)
    except Exception as e:
        logging.critical(f"Error loading data: {e}")
        return None

    # Ensure 'tags' column exists and is not None or empty
    if 'tags' not in cocktails.columns or cocktails['tags'].isnull().any():
        logging.critical("Tags column 'tags' not found or contains null values in DataFrame. Available columns: %s", cocktails.columns.tolist())
        return None

    # Log some example tags for debugging
    logging.debug("Example tags: %s", cocktails['tags'].head())

    # Perform one-hot encoding on the tags column
    logging.info("Starting one-hot encoding of tags")
    cocktails = one_hot_encode_tags(cocktails, 'tags', f"{cfg.one_hot.output_column_prefix}", tags_indices)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save the encoded data
    logging.info("Saving one-hot encoded data to %s", output_file)
    save_encoded_data(cocktails, output_file)
    logging.info("One-hot encoding process complete!")

if __name__ == "__main__":
    main()
