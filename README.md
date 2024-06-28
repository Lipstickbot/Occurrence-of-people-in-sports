Age Analysis of Athletes
This Python script loads a dataset of athletes, calculates the mean age, and visualizes the age distribution.

Requirements
NumPy
Pandas
Matplotlib
Installation
Make sure you have the required libraries installed. You can install them using pip:

bash
pip install numpy pandas matplotlib
Description
The script performs the following steps:

Import Libraries:

numpy for numerical operations.
pandas for data manipulation.
matplotlib.pyplot for plotting.
Load Data:

The dataset Athletes.csv is loaded into a pandas DataFrame from the specified file path.
Calculate Mean Age:

The mean age of the athletes is calculated using the .mean() method on the 'Age' column of the DataFrame.
Plot Age Distribution:

C:\Users\vovot\OneDrive\Pictures\Screenshots

A histogram of the age distribution is plotted.
The mean age is indicated on the histogram with a dashed red line.
The plot includes labels for the x-axis (Age), y-axis (Frequency), and a title (Age Distribution of Athletes).
A legend is added to show the mean age value.
Code
python

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('C:\\Users\\vovot\\Downloads\\Athletes.csv')

# Calculate the mean age
mean_age = df['Age'].mean()
print(f"The mean age of the athletes is: {mean_age:.2f}")

# Plot the age distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('Age Distribution of Athletes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.axvline(mean_age, color='r', linestyle='dashed', linewidth=1, label=f'Mean Age: {mean_age:.2f}')
plt.legend()

plt.show()
Usage
Ensure the CSV file: Ensure that the file path to Athletes.csv is correct in the pd.read_csv function.
Run the script: Execute the script in a Python environment to see the mean age printed and the age distribution histogram displayed.
