import pandas as pd

def load_and_analyze_data(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Display the first 5 rows
    print("First 5 Rows:")
    print(data.head())
    
    # Count the number of missing values in each column
    missing_values = data.isnull().sum()
    print("\nNumber of missing values in each column:")
    print(missing_values)

# File path to the health_data.csv
file_path = 'data/health_data.csv'

# Load and analyze the data
load_and_analyze_data(file_path)