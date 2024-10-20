import pandas as pd
import logging
import hydra
from omegaconf import DictConfig, OmegaConf

# Configure logging with a custom format
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def load_data(file_path):
    """Load JSON data from a specified file."""
    try:
        data = pd.read_json(file_path)
        logging.info(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        logging.critical(f"Error loading data: {e}")
        return None


def analyze_columns(data):
    """Analyze each column in the dataset."""
    logging.info("Analyzing each column in the dataset:")
    
    for column in data.columns:
        logging.info(f"\nAnalyzing column: {column}")
        
        if data[column].apply(lambda x: isinstance(x, list)).any():
            flat_list = data[column].explode().dropna()

            if flat_list.apply(lambda x: isinstance(x, dict)).any():
                dict_df = pd.json_normalize(flat_list)
                unique_count = dict_df.nunique()
                logging.info(f"Unique counts for dict elements:\n{unique_count}")

                for key in dict_df.columns:
                    most_common_value = dict_df[key].mode()[0] if not dict_df[key].isnull().all() else None
                    most_common_freq = dict_df[key].value_counts().max() if not dict_df[key].isnull().all() else 0
                    logging.info(f"Key: {key}, Most common value: {most_common_value}, Frequency: {most_common_freq}")
            else:
                non_null_count = flat_list.notnull().sum()
                unique_count = flat_list.nunique()
                most_common_value = flat_list.mode()[0] if unique_count > 0 else None
                most_common_freq = flat_list.value_counts().max() if unique_count > 0 else 0
                
                logging.info(f"Non-null count: {non_null_count}")
                logging.info(f"Unique count: {unique_count}")
                logging.info(f"Most common value: {most_common_value}")
                logging.info(f"Frequency of the most common value: {most_common_freq}")

        else:
            non_null_count = data[column].notnull().sum()
            unique_count = data[column].nunique()
            most_common_value = data[column].mode()[0] if unique_count > 0 else None
            most_common_freq = data[column].value_counts().max() if unique_count > 0 else 0
            
            logging.info(f"Non-null count: {non_null_count}")
            logging.info(f"Unique count: {unique_count}")
            logging.info(f"Most common value: {most_common_value}")
            logging.info(f"Frequency of the most common value: {most_common_freq}")

            if pd.api.types.is_numeric_dtype(data[column]):
                stats = data[column].describe()
                logging.info(f"Statistics:\n{stats}")

        logging.info("\n")


def generate_descriptive_stats(data):
    """Analyze the dataset and print descriptive statistics and missing values."""
    descriptive_stats = data.describe(include='all')
    logging.info(f"Descriptive Statistics:\n{descriptive_stats}")

    missing_values = data.isnull().sum()
    if missing_values.any():
        logging.debug(f"Missing Values:\n{missing_values}")
    else:
        logging.info("No missing values found.")


@hydra.main(version_base=None, config_path="../../configs/analysis_config", config_name="general_analysis_configs")
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

    # Load data
    if cfg.functions.load_data:
        data = load_data(file_path)
    else:
        logging.info("Data loading is disabled.") 
        return None

    if data is not None:
        # Analyze general data if enabled
        if cfg.functions.generate_descriptive_stats:
            generate_descriptive_stats(data)
        
        # Analyze columns if enabled
        if cfg.functions.analyze_columns:
            analyze_columns(data)
    else:
        logging.error("No data to analyze.")


if __name__ == "__main__":
    main()
