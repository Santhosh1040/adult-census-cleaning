def show_basic_info(df):
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"Number of Rows    : {df.shape[0]}")
    print(f"Number of Columns : {df.shape[1]}")

    print("\nColumn Names:")
    for column in df.columns:
        print(f" - {column}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nMemory Usage:")
    print(df.memory_usage(deep=True))


def profile_data(df):
    """
    Run all profiling steps.
    """
    show_basic_info(df)
    check_missing_values(df)

def check_missing_values(df):
    """
    Check for missing values in the dataset.
    """

    print("\n" + "=" * 60)
    print("MISSING VALUE ANALYSIS")
    print("=" * 60)

    # Check actual NaN values
    print("\nActual Missing Values (NaN):")
    print(df.isnull().sum())

    # Check for '?' placeholders
    print("\n'?' Placeholder Counts:")

    for column in df.select_dtypes(include="object").columns:
        count = df[column].astype(str).str.strip().eq("?").sum()

        if count > 0:
            print(f"{column}: {count}")