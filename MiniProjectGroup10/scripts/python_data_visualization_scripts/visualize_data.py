import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\bdish\\Downloads\\Group10 Nontrivial & Metadata\\Metadata & Nontrivial Info\\data\\processed.csv'

# Load the dataset from the processed CSV file
df = pd.read_csv(file_path, header=0,
                 converters={'profits_percent_change': lambda x: x.rstrip('%'),
                             'market_value': lambda x: x.replace('$', '').replace(',', '').strip()})

# Convert columns to numeric, coerce errors to NaN and drop rows with NaN values
df['profits_percent_change'] = pd.to_numeric(df['profits_percent_change'], errors='coerce')
df['market_value'] = pd.to_numeric(df['market_value'], errors='coerce')

# Create a scatter plot with specified axis limits
plt.figure(figsize=(14, 7))
plt.scatter(df['profits_percent_change'], df['market_value'], color='skyblue')

# Set the maximum value for x-axis at 500 to exclude outliers
plt.xlim(-50, 100)

# Set the maximum value for y-axis at 1 billion to exclude outliers
plt.ylim(0, 100000)

# Set axis labels and plot title
plt.title('Market Value by Profit Percent Change')
plt.xlabel('Profit Percent Change (%)')
plt.ylabel('Market Value ($)')

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()















 

