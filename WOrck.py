import numpy as np 
import pandas as pd 
import matplotlib
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
