## [0.1.1] - 2024-10-10

### Added
- Automatic tag assignment based on ingredients in `data_augmentation.py`.
- Added tags such as `Vegan`, `Vegetarian`, `Strong`, `Fruity`, `Nutty`, etc., based on ingredient definitions.

## [0.1.2] - 2024-10-10

### Added
Automatic tag assignment based on ingredients in preprocessing_scripts/data_augmentation.py.

### Changed
Moved the script for data augmentation from the src directory to preprocessing_scripts.

## [0.1.3] - 2024-10-10

### Removed
- The `Alcoholic` tag has been identified as unnecessary since every cocktail in the dataset contains alcohol. This simplification allows for a more focused analysis on other characteristics of the cocktails.
