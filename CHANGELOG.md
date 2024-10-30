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



## [0.1.8] - 2024-10-26
### Added
- Implemented a function in the `ingredient_analysis.py` script to print unique ingredients from the dataset, enhancing data visibility and analysis.
- Included logging statements to track the unique ingredient extraction process.

### Changed
- Adjusted the overall logging format for consistency across analysis scripts.
- Updated configuration files to include settings for the new unique ingredients function.

### Notes
- The unique ingredients functionality allows for a quick overview of distinct ingredients in the dataset.
- Ensure that the configuration file is updated to enable the new function as needed.

## [0.1.9] - 2024-10-26
### Added
- Introduced a configuration file for tag definitions using Hydra, enabling dynamic assignment of tags based on specified ingredients and thresholds.
- Implemented the structure for tag definitions in YAML format, allowing easy modification and expansion of tagging rules.

### Changed
- Adjusted the tagging mechanism to utilize the new configuration, improving flexibility and maintainability in the tagging process.


# [0.2.0] - 2024-10-28
### Added
- Documented the process of preparing for cocktail tagging, including ingredient classification and alcohol content analysis.
- Developed functions  in `ingredient_analysis.py` to analyze unique ingredients based on their alcohol content.

### Changed
- Refined tagging definitions and criteria based on user feedback and ingredient analysis.

### Notes
- The tagging preparation process has established a framework for categorizing ingredients and tagging cocktails based on their characteristics.
- Future developments will focus on implementing the tagging logic and refining classifications based on further data analysis.


# [0.2.1] - 2024-10-30
### Added
- Implemented tagging logic in `tagging_script.py` with functions to assign tags based on ingredient classifications, including classic, contemporary classic, new era, vegan, vegetarian, and other custom tags.
- Added configuration options in `tagging_config.yaml` to enable/disable specific tagging functions, allowing for flexible tagging logic adjustments.
- Developed functionality in `tagging_script.py` to deduplicate tags, ensuring unique tag assignments for each cocktail.

### Changed
- Refined the classic and contemporary classic tagging criteria, using a threshold approach to distinguish between tags based on ingredient presence.
- Updated `tagging_config.yaml` with more detailed tag definitions and thresholds for each tag type, enhancing customization options.

### Fixed
- Resolved an issue with duplicate tag assignments by implementing a set-based deduplication method, which ensures each tag is added only once per cocktail.

### Notes
- The tagging implementation is now operational, creating a foundation for analyzing cocktail characteristics and enabling targeted categorization based on user-defined criteria.
- Future updates will refine tag definitions further and expand the tagging framework to support more complex categorization as ingredient analysis evolves.
