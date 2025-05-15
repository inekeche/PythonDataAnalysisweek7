
import pandas as pd

# Load the dataset
df = pd.read_csv("Irissales.csv")

# Display the first few rows
print("First 5 rows:")
print(df.head())

# Check data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())



# Compute basic statistics for numerical columns
print(df.describe())


# Group by 'species' and get average of numerical columns
grouped = df.groupby('species').mean()
print(grouped)



print("Species with highest average petal length:")
print(grouped['petal_length'].idxmax())

print("Standard deviation of sepal width by species:")
print(df.groupby('species')['sepal_width'].std())



import matplotlib.pyplot as plt

# Sample time-series data (replace with your own CSV)
df = pd.read_csv('Irissales.csv')  # Should have 'date' and 'sales'


# Line chart
plt.figure(figsize=(10, 5))
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()



# Using Iris dataset as example
df = pd.read_csv('Irissales.csv')  # Has 'species' and 'petal_length'

# Group and calculate mean
avg_petal_length = df.groupby('species')['petal_length'].mean()

# Bar chart
avg_petal_length.plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.ylabel('Average Petal Length')
plt.xlabel('Species')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Histogram of sepal length
plt.hist(df['sepal_length'], bins=10, color='orange', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()


# Scatter plot: Sepal Length vs Petal Length
plt.scatter(df['sepal_length'], df['petal_length'], c='purple', alpha=0.6)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.grid(True)
plt.tight_layout()
plt.show()
