import pandas as pd


def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(file_path)

       
        print("Dataset loaded successfully.")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
       

        return df

    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return None

    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None