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
        

def analyze_columns(data):
    """Analyze each column in the dataset."""
    logging.info("Analyzing each column in the dataset:")
    
    for column in data.columns:
        logging.info(f"\nAnalyzing column: {column}")
        
        # Check if the column contains lists or dicts
        if data[column].apply(lambda x: isinstance(x, list)).any():
            # Flatten the lists
            flat_list = data[column].explode().dropna()

            # Handle cases where the exploded elements are dicts
            if flat_list.apply(lambda x: isinstance(x, dict)).any():
                # Extract specific keys from dicts for analysis
                dict_df = pd.json_normalize(flat_list)
                unique_count = dict_df.nunique()
                logging.info(f"Unique counts for dict elements:\n{unique_count}")

                # Check the most common entries for each key
                for key in dict_df.columns:
                    most_common_value = dict_df[key].mode()[0] if not dict_df[key].isnull().all() else None
                    most_common_freq = dict_df[key].value_counts().max() if not dict_df[key].isnull().all() else 0
                    logging.info(f"Key: {key}, Most common value: {most_common_value}, Frequency: {most_common_freq}")
            else:
                # Regular list handling
                non_null_count = flat_list.notnull().sum()
                unique_count = flat_list.nunique()
                most_common_value = flat_list.mode()[0] if unique_count > 0 else None
                most_common_freq = flat_list.value_counts().max() if unique_count > 0 else 0
                
                logging.info(f"Non-null count: {non_null_count}")
                logging.info(f"Unique count: {unique_count}")
                logging.info(f"Most common value: {most_common_value}")
                logging.info(f"Frequency of the most common value: {most_common_freq}")

        else:
            # Analyze regular columns
            non_null_count = data[column].notnull().sum()
            unique_count = data[column].nunique()
            most_common_value = data[column].mode()[0] if unique_count > 0 else None
            most_common_freq = data[column].value_counts().max() if unique_count > 0 else 0
            
            logging.info(f"Non-null count: {non_null_count}")
            logging.info(f"Unique count: {unique_count}")
            logging.info(f"Most common value: {most_common_value}")
            logging.info(f"Frequency of the most common value: {most_common_freq}")

            # Basic statistics for numerical columns
            if pd.api.types.is_numeric_dtype(data[column]):
                stats = data[column].describe()
                logging.info(f"Statistics:\n{stats}")

        logging.info("\n")



def analyze_data(data):
    """Analyze the dataset and print descriptive statistics and missing values."""
    descriptive_stats = data.describe(include='all')  # Include all data types
    logging.info(f"Descriptive Statistics:\n{descriptive_stats}")

    missing_values = data.isnull().sum()
    if missing_values.any():
        logging.debug(f"Missing Values:\n{missing_values}")
    else:
        logging.info("No missing values found.")

def main():
    data = load_data('data/raw/cocktail_dataset.json')
    if data is not None:
        analyze_data(data)
        analyze_columns(data)  # Call the function to analyze each column
    else:
        logging.error("No data to analyze.")


if __name__ == "__main__":
    main()
