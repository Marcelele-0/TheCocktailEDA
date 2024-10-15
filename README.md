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

