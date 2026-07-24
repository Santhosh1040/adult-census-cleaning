def validate_dataset(df):

    print("\nValidation Report")
    print("-" * 40)

    print(f"Missing Values : {df.isnull().sum().sum()}")

    print(f"Duplicate Rows : {df.duplicated().sum()}")

    print(f"Final Shape    : {df.shape}")