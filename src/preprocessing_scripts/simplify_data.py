import pandas as pd
import logging
import hydra
from omegaconf import DictConfig, OmegaConf

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simplify_cocktail_data(df):
    '''Simplify the cocktail data by removing unnecessary columns: createdAt, updatedAt, imageUrl and simplifying the ingredients data'''
    # Drop unnecessary columns
    df = df.drop(columns=['createdAt', 'updatedAt', 'imageUrl', 'instructions'], errors='ignore')
    
    df['ingredients'] = df['ingredients'].apply(lambda ingredients: [
        {k: v for k, v in ingredient.items() if k not in ['createdAt', 'updatedAt', 'imageUrl','description']}
        for ingredient in ingredients
    ])
    
    return df

def load_data(file_path):
    '''Load JSON data from a specified file path into a DataFrame'''
    return pd.read_json(file_path)

def save_simplified_data(df, file_path):
    '''Save the simplified DataFrame to a JSON file'''
    df.to_json(file_path, orient='records', indent=4)

@hydra.main(version_base=None, config_path="../../configs/preprocessing_configs", config_name="data_simplification_config")
def main(cfg: DictConfig):
    '''Main function to simplify the cocktail data'''

    input_file = 'data/raw/cocktail_dataset.json'
    output_file = 'data/processed/processed_cocktail_dataset.json'

    logging.debug("Loading data from %s", input_file)
    df = load_data(input_file)

    # Apply simplification if specified in the config
    if cfg.apply_simplification:
        logging.debug("Simplifying the data")
        simplified_df = simplify_cocktail_data(df)
        
        # Save the simplified data back to JSON
        logging.debug("Saving simplified data to %s", output_file)
        save_simplified_data(simplified_df, output_file)
    else:
        logging.info("Simplification not applied based on the config.")

    logging.info("Data processing complete!")

if __name__ == "__main__":
    main()
