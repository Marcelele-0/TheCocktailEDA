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

### - Data shema
#### Cocktail

- **id** (integer): Unique identifier of the cocktail  
  Example: 11000, 11001

- **name** (string): Name of the cocktail  
  Example: "Mojito", "Old Fashioned"

- **instructions** (string, nullable): Instructions on how to prepare the cocktail  
  Example: "Muddle mint leaves with sugar and lime juice..."

- **alcoholic** (boolean): Indicates whether the cocktail contains alcohol  
  Example: true, false

- **category** (enum, nullable): Category of the cocktail  
  Example: "Cocktail", "Ordinary Drink", "Shot"

- **glass** (enum, nullable): Type of glass used for serving  
  Example: "Highball glass", "Old-fashioned glass"

- **imageUrl** (string, nullable): URL of the cocktail image  
  Example: https://cocktails.solvro.pl/images/cocktails/mojito.png

- **createdAt** (string, nullable): Record creation date  
  Example: "2024-08-19 18:39:58"

- **updatedAt** (string, nullable): Record update date  
  Example: "2024-08-21 10:12:58"

### Ingredients

- **id** (integer): Unique identifier of the ingredient  
  Example: 10, 11

- **name** (string): Name of the ingredient  
  Example: "Red wine", "Grapefruit juice"

- **description** (string, nullable): Description of the ingredient  
  Example: "Red wine is a type of wine made from dark-colored grape varieties..."

- **alcohol** (boolean, nullable): Indicates whether the ingredient contains alcohol  
  Example: true, false

- **type** (enum, nullable): Type of ingredient  
  Example: "Vodka", "Gin", "Juice"

- **percentage** (number, nullable): Alcohol percentage of the ingredient  
  Example: 40, null

- **imageUrl** (string, nullable): URL of the ingredient image  
  Example: https://cocktails.solvro.pl/images/ingredients/rose.png

- **createdAt** (string, nullable): Record creation date for the ingredient  
  Example: "2024-08-19 18:39:58"

- **updatedAt** (string, nullable): Record update date for the ingredient  
  Example: "2024-08-21 10:12:58"

- **measure** (string): Measurement or quantity of the ingredient used  
  Example: "1/2 oz"


- #### Unique ingredients in the dataset: 
  ['Soda water', 'Light Rum', 'Lime', 'Mint', 'Sugar', 'Water', 'Angostura Bitters', 'Bourbon', 'lemon', 'Vodka',
   'Gin', 'Tequila', 'Coca-Cola', 'Sweet Vermouth', 'Campari', 'Powdered Sugar', 'Blended Whiskey', 'Cherry', 'Dry Vermouth', 
   'Olive', 'Lime Juice', 'Salt', 'Triple Sec', 'Ice', 'Maraschino Cherry', 'Orange Peel', 'Ginger Ale', 'Apricot Brandy', 
   'Lemon Juice', 'Amaretto', 'Sloe Gin', 'Southern Comfort', 'Lemon Peel', 'Orange Bitters', 'Yellow Chartreuse', 
   'Creme De Cacao', 'Light Cream', 'Nutmeg', 'Brandy', 'Lemon vodka', 'Pineapple Juice', 'Blackberry Brandy', 'Kummel', 
   'Dark Rum', 'Egg White', 'Kahlua', 'Club Soda', 'White Creme de Menthe', 'Tea', 'Whipped Cream', 'Apple Brandy', 
   'Applejack', 'Orange', 'Benedictine', 'Wine', 'Champagne', 'Green Creme de Menthe', 'Grand Marnier', 'Bitters', 
   'Scotch', 'Banana', 'Carbonated Water', 'Coffee Liqueur', 'Celery Salt', 'Tabasco Sauce', 'Tomato Juice', 'Worcestershire Sauce', 
   'Blue Curacao', 'Lemonade', 'Anejo Rum', 'Orange Juice', 'Tia Maria', 'Maraschino Liqueur', 'Grenadine', 'Egg', 
   'Cachaca', 'Egg Yolk', 'Cognac', 'Cherry Brandy', 'Port', 'Chocolate Ice-cream', 'Dubonnet Rouge', 'Sugar Syrup', 
   'Pineapple', 'Tonic Water', 'Orange spiral', 'Strawberries', 'Heavy cream', 'Galliano', 'Irish Whiskey', 
   'Peach brandy', 'Sweet and Sour', 'Green Chartreuse', 'Drambuie', 'Orgeat Syrup', 'Grapefruit Juice', 'Red Wine', 
   'Raspberry syrup', 'Sherry', 'Coffee Brandy', 'Lime vodka', 'Lemon-lime soda']   

- ####  Unique tags in the dataset: 
  ['IBA' 'ContemporaryClassic' 'Alcoholic' 'USA' 'Asia' 'Vegan' 'Citrus'
  'Brunch' 'Hangover' 'Mild' 'Classic' 'Expensive' 'Savory' 'Strong'
  'StrongFlavor' 'Vegetarian' 'Sour' 'Christmas' 'Beach' 'DinnerParty'
  'Summer' 'Chilli' 'Dairy' 'Nutty' 'Cold' 'Fruity' 'Breakfast' 'NewEra']