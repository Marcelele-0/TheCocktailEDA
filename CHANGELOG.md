## [0.1.1] - 2024-10-10
### Added
- Automatic tag assignment based on ingredients in `data_augmentation.py`.
- Added tags such as `Vegan`, `Vegetarian`, `Strong`, `Fruity`, `Nutty`, etc., based on ingredient definitions.

## [0.1.2] - 2024-10-10

### Added
- Automatic tag assignment based on ingredients in `preprocessing_scripts/data_augmentation.py`.

### Changed
- Moved the script for data augmentation from the `src` directory to `preprocessing_scripts`.

## [0.1.3] - 2024-10-10

### Removed
- The `Alcoholic` tag has been identified as unnecessary since every cocktail in the dataset contains alcohol. This simplification allows for a more focused analysis on other characteristics of the cocktails.

## [0.1.4]

### Changed
- Removed the "Vegetarian" tag from cocktail classification. It turned out that all cocktails marked as vegetarian are also vegan, making the "Vegetarian" tag redundant. Only the "Vegan" tag is retained, which fully reflects the absence of animal-derived ingredients.

- Updated data analysis code for JSON files:
- Added logging configuration using the logging module to improve clarity and usability of messages in the code.

- New functions added for data analysis:
- Created the function analyze_data(data) to calculate and log descriptive statistics and missing values.

## [0.1.5]
- Concept failed, starting from scratch.

## [0.1.6] - 2024-10-15
### Added
- Implemented a general analysis file 
- reated an ingredient analysis file 

### Changed
- Updated the code structure to improve modularity and readability, ensuring that functions are clearly defined and documented for future reference.
- Enhanced logging capabilities to provide more detailed output regarding the analyses performed and the findings derived from the data.

### To Do
- Hydra config for ingredients_analysis.py

### Removed
Removed any redundant or unnecessary functions that were identified during the development of the new analysis features, streamlining the codebase. 

# Changelog

## [0.1.7] - 2024-10-20
### Added
- Implemented global configuration management to handle input data type selection across different analysis files.
- Created local configurations for individual analysis scripts to control the execution of specific functions.
- Added functionality to the `ingredient_analysis.py` script to load and analyze ingredient data.
- Introduced data simplification functionality in a dedicated script for removing unnecessary columns from cocktail data.
- Enhanced logging for better visibility into data loading and analysis processes.

### Changed
- Updated `general_analysis.py` to conditionally load data based on the selected data type (original or processed).
- Modified the configuration files to accommodate function-specific settings alongside the global settings.

### Removed
- Removed unnecessary columns (`createdAt`, `updatedAt`, `imageUrl`) from cocktail and ingredient datasets during data simplification.

### Notes
- Data processed by the new simplification function will be saved in the `data/processed/` directory.
- Hydras output directory is now included in `.gitignore` to prevent clutter in the repository.
