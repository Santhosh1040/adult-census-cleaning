def save_cleaned_data(df, output_path):
    """
    Save the cleaned dataset to a CSV file.
    """

    df.to_csv(output_path, index=False)

    print(f"\nCleaned dataset saved to: {output_path}")