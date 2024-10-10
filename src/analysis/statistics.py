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


def analyze_data(data):
    """Analyze the dataset and print descriptive statistics and missing values."""
    descriptive_stats = data.describe(include='all')  # Include all data types
    logging.info(f"Descriptive Statistics:\n{descriptive_stats}")

    missing_values = data.isnull().sum()
    if missing_values.any():
        logging.debug(f"Missing Values:\n{missing_values}")
    else:
        logging.info("No missing values found.")

    numeric_stats = data.describe()  # Numeric statistics only
    logging.info(f"Numeric Statistics:\n{numeric_stats}")


def main():
    data = load_data('data/processed/processed_data.json')
    if data is not None:
        analyze_data(data)
    else:
        logging.error("No data to analyze.")


if __name__ == "__main__":
    main()
