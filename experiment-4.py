import pandas as pd

def load_dataset(file_path):
    # Load dataset into a Pandas DataFrame
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def export_dataset(df, file_path):
    # Export dataset to a CSV file
    try:
        df.to_csv(file_path, index=False)
        print(f"Dataset successfully exported to {file_path}")
    except Exception as e:
        print(f"Error exporting dataset: {e}")

def dataset_info(df):
    # Display basic information about the dataset
    print("\nNumber of rows and columns:")
    print(df.shape)
    
    print("\nFirst five rows of the dataset:")
    print(df.head())
    
    print("\nSize of the dataset (number of elements):")
    print(df.size)
    
    print("\nNumber of missing values in each column:")
    print(df.isnull().sum())
    
    print("\nSummary statistics for numerical columns:")
    print(df.describe())
    
    print("\nSum of numerical columns:")
    print(df.sum(numeric_only=True))
    
    print("\nAverage (mean) of numerical columns:")
    print(df.mean(numeric_only=True))
    
    print("\nMinimum values in numerical columns:")
    print(df.min(numeric_only=True))
    
    print("\nMaximum values in numerical columns:")
    print(df.max(numeric_only=True))

# Example usage
file_path = 'input_data.csv'  # Replace with your dataset path
df = load_dataset(file_path)

if df is not None:
    dataset_info(df)
    export_dataset(df, 'output_data.csv')  # Exporting the dataset to a new file
