# -*- coding: utf-8 -*-


# Loading Libraries
"""

# Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""# Loading Dataset"""

# Load the dataset
data = pd.read_csv("Hospital.csv")

data

"""# Display First 5 Rows"""

# Display first 5 rows
data.head()

"""# Display Last 5 Rows"""

# Display last 5 rows
data.tail()

"""# Display Data Types Of Columns"""

# Display data types of columns
data.dtypes

"""# Display Five Point Summary"""

# Five point summary
data.describe(include='all')

"""#Removing Outlier

"""

from scipy.stats import zscore
z_scores = data.select_dtypes(include=['number']).apply(zscore)
data_no_outliers = data[(z_scores < 3).all(axis=1)]

"""# Display Total Number Of Rows & Columns"""

# Display total number of rows and columns
data.shape

"""# Finding Duplicates Values"""

# Finding duplicate values count
data.duplicated().sum()

"""# Finding Missing Values"""

# Finding missing values summary
data.isnull().sum()

"""# Dropping Missing Values"""

# Dropping Missing Values
data = data.dropna(axis=1)

"""# Finding Uniques Values For Each Columns"""

# Finding unique values for each column
data.nunique()

"""# Finding object columns"""

# Finding object columns
object_cols = data.select_dtypes(include=['object']).columns.tolist()
object_cols

"""# Finding numerical columns"""

# Finding numerical columns
numerical_cols = data.select_dtypes(include=['number']).columns.tolist()
numerical_cols

"""# Calculate & Display the Correlation Matrix for the Numeric Columns"""

# Step 1: Select only numeric columns
numeric_cols = data.select_dtypes(include=['number']).columns

# Step 2: Compute the correlation matrix for numeric columns
correlation_matrix = data[numeric_cols].corr()

# Step 3: Display the correlation matrix
print(correlation_matrix)

"""# Display Heatmap for Numeric Columns"""

# Select only numeric columns before calculating correlations
numeric_data = data.select_dtypes(include=['number'])

# Calculate the correlation matrix
corr_matrix = numeric_data.corr()

# Plot the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

"""# Count Plots For Each Object Type Columns"""

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame and 'object_columns' is a list of categorical column names
for col in object_columns:
    plt.figure(figsize=(8, 6))  # Increase plot size
    top_categories = data[col].value_counts().nlargest(10).index  # Limit to top 10 categories
    sns.countplot(y=col, data=data, order=top_categories)  # Use order for more clarity
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

"""# Top 10 Object-Type BarPlot"""

for col in object_columns:
    plt.figure(figsize=(8, 6))
    top_values = data[col].value_counts().head(10)  # Get the top 10 most frequent values
    sns.barplot(y=top_values.index, x=top_values.values)
    plt.title(f'Top 10 Categories in {col}')
    plt.xlabel('Count')
    plt.ylabel(col)
    plt.show()

"""# Numeric Columns Boxplot"""

for col in numerical_columns:
    sns.boxplot(x=data[col])
    plt.show()

"""# Histograms with a Kernel Density Estimate (KDE)"""

for col in numerical_columns:
    sns.histplot(data[col], kde=True)
    plt.show()

sns.scatterplot(data=data, x='OrganisationID', y='Sector')

sns.lineplot(data=data, x='OrganisationID', y='Sector')

sns.boxplot(data=data, x='OrganisationID', y='Sector')

sns.barplot(data=data, x='OrganisationCode', y='OrganisationID')

"""#Removing Outliers"""

import matplotlib.pyplot as plt
import seaborn as sns

# Boxplot before removing outliers
plt.figure(figsize=(8, 4))
sns.boxplot(data=data)
plt.title("Before Removing Outliers")
plt.show()

# Boxplot after removing outliers
plt.figure(figsize=(8, 4))
sns.boxplot(data=data_no_outliers)
plt.title("After Removing Outliers")
plt.show()

import pandas as pd

# Load the dataset
df = pd.read_csv("Hospital.csv")

# Print the column names
print("Column names in the dataset:")
print(df.columns)

# Correct the column names
columns_to_check = ['OrganisationID', 'Latitude', 'Longitude']  # Update with actual names

# Function to remove outliers
def remove_outliers(df, columns):
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    return df

# Apply the function to remove outliers
df_no_outliers = remove_outliers(df, columns_to_check)

# Display results
print("\nDataset after removing outliers:")
print(df_no_outliers.head())
print("\nOriginal dataset shape:", df.shape)
print("Dataset shape after removing outliers:", df_no_outliers.shape)

numerical_columns = ['OrganisationID']  # Replace with actual column names

# Plot histograms for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(8, 5))
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot for OrganisationID by OrganisationType
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='OrganisationType', y='OrganisationID', palette='pastel')
plt.title('Boxplot of OrganisationID by OrganisationType')
plt.xlabel('OrganisationType')
plt.ylabel('OrganisationID')
plt.xticks(rotation=45)
plt.show()

# Scatterplot for OrganisationID and OrganisationCode
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='OrganisationID', y='OrganisationCode', hue='OrganisationType', palette='viridis', s=50)
plt.title('Scatterplot of OrganisationID vs OrganisationCode')
plt.xlabel('OrganisationID')
plt.ylabel('OrganisationCode')
plt.legend(title='OrganisationType')
plt.show()

# Catplot for OrganisationType and OrganisationID
sns.catplot(data=df, x='OrganisationType', y='OrganisationID', kind='point', height=5, aspect=2, palette='coolwarm')
plt.title('Cat-plot of OrganisationID by OrganisationType')
plt.xlabel('OrganisationType')
plt.ylabel('OrganisationID')
plt.show()

# Countplot for OrganisationType
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='OrganisationType', palette='mako')
plt.title('Countplot of OrganisationType')
plt.xlabel('OrganisationType')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Bar-plot for OrganisationType and mean OrganisationID
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='OrganisationType', y='OrganisationID', ci='sd', palette='Blues_d')
plt.title('Barplot of OrganisationID by OrganisationType')
plt.xlabel('OrganisationType')
plt.ylabel('Mean OrganisationID')
plt.xticks(rotation=45)
plt.show()

import pandas as pd

# Load the dataset
data = pd.read_csv('Hospital.csv')

# Display the first few rows of the dataset
print("Initial Data:")
print(data.head())

# 1. Handle missing values:
# Drop rows with missing values
data = data.dropna()  # Option 1: Drop rows with any missing values

# Alternatively, you can fill missing values with a specific value (e.g., mean for numerical columns)
# data.fillna(data.mean(), inplace=True)  # Option 2: Fill missing values with the mean of each column

# 2. Remove duplicate rows
data.drop_duplicates(inplace=True)

# 3. Convert data types if necessary
# For example, convert 'Age' column to integer
data['OrganisationID'] = data['OrganisationID'].astype(int)

# 4. Remove unnecessary columns (e.g., index columns like 'Unnamed: 0')
data.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')

# 5. Reset index after dropping rows or duplicates
data.reset_index(drop=True, inplace=True)

# Display the cleaned data
print("Cleaned Data:")
print(data.head())

# Save the cleaned dataset
data.to_csv('Cleaned_Hospital.csv', index=False)

import pandas as pd

# Load the dataset
data = pd.read_csv('Hospital.csv')

# Display the first few rows of the dataset
print("Initial Data:")
print(data.head())

# 1. Handling Missing Values:
# Impute missing values with the mean for numerical columns and mode for categorical columns.
# For numerical columns, we use the median (or mean, depending on your preference).
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    data[column].fillna(data[column].median(), inplace=True)  # Impute with median for numerical columns

for column in data.select_dtypes(include=['object']).columns:
    data[column].fillna(data[column].mode()[0], inplace=True)  # Impute with mode for categorical columns

# Alternatively, drop rows with missing values (uncomment if needed)
# data = data.dropna()  # Drop rows with any missing values

# 2. Removing Duplicates:
# Remove duplicate rows, keeping the first occurrence.
data.drop_duplicates(inplace=True)

# 3. Data Type Conversion:
# Ensure columns are of the correct data type (e.g., numerical data for scores).
# Convert columns to appropriate types if needed.
data['Age'] = data['Age'].astype(int)  # Example: Convert Age to integer if it's a float
data['Gender'] = data['Gender'].astype('category')  # Convert categorical column to 'category' type

# If any other column needs type conversion, handle it similarly.
# For example, converting a date column to datetime format
# data['Date'] = pd.to_datetime(data['Date'])

# Display the cleaned data
print("Cleaned Data:")
print(data.head())

# Save the cleaned dataset
data.to_csv('Cleaned_Hospital.csv', index=False)

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
data = pd.read_csv('Hospital.csv')

# Display the first few rows of the dataset
print("Initial Data:")
print(data.head())

# 1. Handling Missing Values:
# Impute missing values with the median for numerical columns
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    data[column].fillna(data[column].median(), inplace=True)  # Impute with median for numerical columns

# Impute missing values with the mode for categorical columns
for column in data.select_dtypes(include=['object']).columns:
    data[column].fillna(data[column].mode()[0], inplace=True)  # Impute with mode for categorical columns

# Alternatively, drop rows with missing values (uncomment if needed)
# data = data.dropna()  # Drop rows with any missing values

# 2. Removing Duplicates:
# Remove duplicate rows
data.drop_duplicates(inplace=True)

# 3. Data Type Conversion:
# Convert columns to appropriate types if needed
data['OrganisationID'] = data['OrganisationID'].astype(int)  # Example: Convert 'Age' to integer
data['OrganisationCode'] = data['OrganisationCode'].astype('category')  # Example: Convert 'Gender' to category type

# 4. Handle Outliers (Optional): For example, capping values in 'Age' column
data['OrganisationID'] = data['OrganisationID'].clip(lower=data['OrganisationID'].quantile(0.05), upper=data['OrganisationID'].quantile(0.95))

# 5. Feature Engineering (Example):
# Create a new feature based on existing columns (e.g., BMI from height and weight)
# data['BMI'] = data['Weight'] / (data['Height']**2)  # Example formula for BMI

# 6. Data Scaling (Standardization):
# Standardize numerical features using StandardScaler
scaler = StandardScaler()
numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# 7. Encoding Categorical Variables:
# If 'Gender' is categorical, encode it as numerical (0 and 1)
label_encoder = LabelEncoder()
data['OrganisationCode'] = label_encoder.fit_transform(data['OrganisationCode'])

# 8. Reset Index After Cleaning:
data.reset_index(drop=True, inplace=True)

# Display the cleaned and preprocessed data
print("Cleaned and Preprocessed Data:")
print(data.head())

# Save the cleaned and preprocessed dataset
data.to_csv('Preprocessed_Hospital.csv', index=False)

