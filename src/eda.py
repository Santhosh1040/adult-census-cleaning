import os
import pandas as pd
import matplotlib.pyplot as plt


def create_reports_folder():
    """
    Create the reports/figures directory if it doesn't exist.
    """
    os.makedirs("reports/figures", exist_ok=True)


def dataset_overview(df):
    """
    Display the basic information about the dataset.
    """
    print("\nDataset Overview")
    print("-" * 40)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")


def summary_statistics(df):
    """
    Display summary statistics for numerical columns.
    """
    print("\nSummary Statistics")
    print("-" * 40)

    print(df.describe())


def income_distribution(df):
    """
    Generate and save the income distribution plot.
    """
    plt.figure(figsize=(6, 4))

    df["income"].value_counts().plot(kind="bar")

    plt.title("Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Count")

    plt.tight_layout()
    plt.savefig("reports/figures/income_distribution.png", dpi=300)
    plt.close()

    print("✓ Income distribution generated")


def age_distribution(df):
    """
    Generate and save the age distribution histogram.
    """
    plt.figure(figsize=(6, 4))

    plt.hist(df["age"], bins=20, edgecolor="black")

    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("reports/figures/age_distribution.png", dpi=300)
    plt.close()

    print("✓ Age distribution generated")


def education_distribution(df):
    """
    Generate and save the education distribution plot.
    """
    plt.figure(figsize=(10, 5))

    df["education"].value_counts().plot(kind="bar")

    plt.title("Education Distribution")
    plt.xlabel("Education")
    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("reports/figures/education_distribution.png", dpi=300)
    plt.close()

    print("✓ Education distribution generated")


def occupation_distribution(df):
    """
    Generate and save the occupation distribution plot.
    """
    plt.figure(figsize=(12, 5))

    df["occupation"].value_counts().plot(kind="bar")

    plt.title("Occupation Distribution")
    plt.xlabel("Occupation")
    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("reports/figures/occupation_distribution.png", dpi=300)
    plt.close()

    print("✓ Occupation distribution generated")


def correlation_heatmap(df):
    """
    Generate and save the correlation heatmap for numerical features.
    """
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    correlation = numeric_df.corr()

    plt.figure(figsize=(8, 6))

    plt.imshow(correlation, cmap="coolwarm", aspect="auto")
    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=90
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.savefig("reports/figures/correlation_heatmap.png", dpi=300)
    plt.close()

    print("✓ Correlation heatmap generated")


def perform_eda(df):
    """
    Run the complete Exploratory Data Analysis pipeline.
    """
    print("\nRunning Exploratory Data Analysis...")
    print("-" * 40)

    create_reports_folder()

    dataset_overview(df)
    summary_statistics(df)

    income_distribution(df)
    age_distribution(df)
    education_distribution(df)
    occupation_distribution(df)
    correlation_heatmap(df)

    print("\n✓ EDA completed successfully.")