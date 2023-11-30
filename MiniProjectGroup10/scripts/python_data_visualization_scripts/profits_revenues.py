import pandas as pd
import matplotlib.pyplot as plt

df_new = pd.read_csv('cleaned_top_revenue_profits.csv')

# Strip any whitespace from the column names
df_new.columns = df_new.columns.str.strip()

# Now we will try to plot the data again
plt.figure(figsize=(10, 6))
plt.scatter(df_new['profits'], df_new['revenues'], color='blue', alpha=0.6)

# Set the labels for the axes based on the file content
plt.xlabel('Profits')
plt.ylabel('Revenues')

# Add a title to the plot
plt.title('Scatter Plot of Revenues vs Profits')

# Show a grid for better readability
plt.grid(True)

# Display the plot
plt.show()
