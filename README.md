# AIPI510 Preassignment

## Heart Disease Data Processing

This Python project processes a CSV file containing heart disease data to calculate and analyze the average age of male and female stroke patients. Additionally, it creates a list of the yongest stroke patients by gender. Before using the dataset, all NaN values are dropped.

Author: Iara Ravagni

### Files
- preassignment.py: Main script that processes the CSV file, calculates average ages, and lists the youngest stroke patients.
- test_df.py & test_output.py: Pytests to validate the dataframe and output.
- setup.py: Script for setting up the project as a package.
- requirements.txt: List of Python packages required to run the project.
- heart_disease.csv: The dataset used in this project.(1)

### Requirements
- Python 3.12.5
- Packages listed in requirements.txt

### Usage
1. Run the setup.py file to install all the required packages. To do so use `python setup.py develop` command.
2. Run the main file script from the terminal, using the following code: `python preassignment.py`
3. Run the command  `pytest` to check if the dataframe loaded and outputs are the expected ones or not.

### Bibliography 
(1) Mazaharul Hasnine Mirza. (2023). Heart Disease Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/5146672