# TheCocatailEDA

This project focuses on exploratory data analysis (EDA) and clustering of cocktail recipes, based on a dataset from TheCocktailDB.

## Table of Contents
1. Introduction
2. Installation
3. Dataset
4. EDA Conclusions

## 1. Introduction
This project performs EDA and clustering on a dataset of cocktails and their ingredients. The dataset is available in the `data/` folder.

### Project Structure
```txt
project-root/
├── configs/                # Configuration files
├── data/                   
│   ├── raw                 # Dataset in JSON format
│   ├── processed           # Processed dataset
├── notebooks/              # Jupyter notebooks for results visualization
├── src/                    # Core Python code
│   ├── datamodule.py       # Preprocessing logic
│   ├── clustering.py       # Clustering logic
├── README.md               # Project documentation
├── environment.yaml        # Conda environment setup
└── requirements.txt        # List of required dependencies
```

## 2. Installation

### Create Conda Environment
1. Clone this repository:
    ```bash
    git clone https://github.com/Solvro/rekrutacja/blob/main/machine_learning.md
    cd TheCocktailEDA
    ```
2. Create and activate the Conda environment:
     ```bash 
     conda env create -f environment.yaml
     conda activate cocktail-clustering
     ```

3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## 3. Dataset
The dataset is stored in JSON format in the `data/` folder. 

## 4. EDA Conclusions

### General Tags 
- During the preprocessing phase, relevant tags are automatically assigned to cocktails based on their ingredients. 
- This process ensures consistency and enriches the dataset by adding meaningful labels such as "Vegan", "Strong", or "Chilli". 
- The logic for this tagging system is located in the `preprocessing_scripts/data_augmentation.py` file, which analyzes the ingredients of each cocktail and updates the tags accordingly.

### Tag 'Alcoholic'
- During the exploratory data analysis, it was discovered that every cocktail in the dataset is alcoholic. As a result, the `Alcoholic` tag is deemed unnecessary for this dataset. This observation simplifies our analysis, as we can focus on other relevant attributes without redundancy.

### Tag 'Vegan'
- The analysis of cocktails revealed that all drinks labeled as vegetarian are also vegan. Therefore, the "Vegetarian" tag has been removed from the classification. Only the "Vegan" tag is retained, which better reflects the absence of animal-derived ingredients. This simplification allows for a clearer classification of cocktails in the project.
