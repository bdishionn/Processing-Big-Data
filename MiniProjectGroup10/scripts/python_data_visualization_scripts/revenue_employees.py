import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import polyfit, poly1d

# Load the dataset
df_employees_revenue = pd.read_csv("top_employees_revenue.csv")

df_employees_revenue.columns = df_employees_revenue.columns.str.strip()

# Calculate the coefficients of the linear fit
coefficients = polyfit(df_employees_revenue['revenues'], df_employees_revenue['employees'], 1)

# Create a polynomial object from the coefficients
polynomial = poly1d(coefficients)

# Generate x values for the trend line (from min to max revenues)
x_values = range(int(df_employees_revenue['revenues'].min()), int(df_employees_revenue['revenues'].max()))

# Calculate the y values from the polynomial
y_values = polynomial(x_values)

# Create the scatter plot again
plt.figure(figsize=(10, 6))
plt.scatter(df_employees_revenue['revenues'], df_employees_revenue['employees'], color='green', alpha=0.6)

# Plot the trendline
plt.plot(x_values, y_values, color='red', linestyle='--')

# Set the labels for the axes
plt.xlabel('Revenues')
plt.ylabel('Number of Employees (in millions)')

# Add a title to the plot
plt.title('Scatter Plot of Top 25 Revenues w/ Number of Employees & Trendline')

# Show a grid for better readability
plt.grid(True)

# Display the plot
plt.show()



