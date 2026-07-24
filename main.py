from src.loader import load_data
from src.profiling import profile_data
from src.cleaning import (
    replace_question_marks,
    standardize_categorical_values,
    handle_missing_values,
    remove_duplicates
)
from src.validation import validate_dataset
from src.save_data import save_cleaned_data
from src.eda import perform_eda


def main():
    
    df = load_data("data/raw/adult.csv")

    
    print("\nRaw Dataset Profile")
    print("=" * 40)
    profile_data(df)

    # Data Cleaning Pipeline
    df = replace_question_marks(df)
    df = standardize_categorical_values(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    # Validate cleaned dataset
    print("\nCleaned Dataset Validation")
    print("=" * 40)
    validate_dataset(df)

    
    save_cleaned_data(df, "data/processed/adult_cleaned.csv")
    perform_eda(df)


if __name__ == "__main__":
    main()