import pandas as pd


def replace_question_marks(df):
    """
    Replace '?' placeholders with actual NaN values.
    """
    df = df.replace(r'^\s*\?$', pd.NA, regex=True)

    print("\nReplaced '?' placeholders with NaN.")

    return df


def standardize_categorical_values(df):
    """
    Standardize categorical columns by removing leading and trailing spaces.
    """
    categorical_columns = df.select_dtypes(include=["object", "string"]).columns

    print("\nStandardizing categorical values...")

    for column in categorical_columns:
        df.loc[:, column] = df[column].str.strip()

    print("Categorical values standardized.")

    return df


def handle_missing_values(df):
    """
    Fill missing values in categorical columns using the mode.
    """
    categorical_columns = [
        "workclass",
        "occupation",
        "native.country"
    ]

    print("\nHandling missing values...")

    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            mode_value = df[column].mode()[0]
            df.loc[:, column] = df[column].fillna(mode_value)

            print(f"{column} -> Filled missing values with '{mode_value}'")

    return df


def remove_duplicates(df):
    """
    Remove duplicate records from the dataset.
    """
    duplicate_count = df.duplicated().sum()

    print(f"\nDuplicate records found: {duplicate_count}")

    df = df.drop_duplicates().copy()

    print(f"Duplicate records removed: {duplicate_count}")

    return df