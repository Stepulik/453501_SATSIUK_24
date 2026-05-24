"""
Lab Work 4 - Task 6 - Variant 24
Topic: Working with files, classes, serializers, regex, and standard libraries
Task: Pandas analysis of the Supermarket Sales dataset
Datasets:
  a) https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales/data
  b) https://www.kaggle.com/aungpyaeap/supermarket-sales
Developer: [Your Name]
Version: 1.2
Date: 2026
"""

import pandas as pd

# 
# 1. Import pandas (required step shown explicitly)
# 
# pandas is already imported above as 'pd'

CSV_PATH = "SuperMarket_Analysis.csv"


def load_data(path):
    """Load the CSV file and return a DataFrame."""
    df = pd.read_csv(path)
    return df

def display(obj):
    """print the object with a blank line after."""
    print(obj)
    print()


def task_a(df):
    """
    Task A: Series and DataFrame — all required steps.

    Steps covered:
      1. pandas imported at the top of the file
      2. Series structure (dtype, index, values)
      3. Creating a Series
      4. display() function
      5. Accessing elements with .loc and .iloc
      6. DataFrame creation

    Variant 24 specific task:
      From 'Product line' create a categorical Series with a defined
      category order, convert to codes, build a new DataFrame with
      the codes and the original category names.
    """

    #  2-3. Series structure and creation 
    # Create a plain Series from the 'Product line' column
    plain_series = pd.Series(df["Product line"].values, name="Product line")

    print("\n 2-3. Series structure ")
    print(f"Name  : {plain_series.name}")
    print(f"dtype : {plain_series.dtype}")
    print(f"Length: {len(plain_series)}")
    print(f"Index : {plain_series.index}")
    print(f"Values (first 5): {plain_series.values[:5]}")

    #  4. display() 
    print("\n 4. display() — Series preview ")
    display(plain_series.head(10))

    #  5. Accessing elements with .loc and .iloc 
    print(" 5. Element access ")

    # .iloc — access by integer position
    print(f".iloc[0]  → {plain_series.iloc[0]}")
    print(f".iloc[1:4] →")
    display(plain_series.iloc[1:4])

    # .loc  — access by label (here labels are integers 0, 1, 2...)
    print(f".loc[0]   → {plain_series.loc[0]}")
    print(f".loc[0:2] →")
    display(plain_series.loc[0:2])

    #  categorical Series 
    print(" Variant 24: Categorical Series with defined order ")

    # Custom category order
    category_order = [
        "Food and beverages",
        "Fashion accessories",
        "Electronic accessories",
        "Sports and travel",
        "Home and lifestyle",
        "Health and beauty",
    ]

    # 3. Create a categorical Series with ordered categories
    cat_series = pd.Categorical(
        df["Product line"],
        categories=category_order,
        ordered=True
    )
    product_series = pd.Series(cat_series, name="Product line (categorical)")

    print("\nCategory order defined:")
    for i, cat in enumerate(category_order):
        print(f"  {i} — {cat}")

    # 4. display() the categorical Series
    print("\ndisplay() — Categorical Series (first 10 rows):")
    display(product_series.head(10))

    # 5.loc and .iloc on the categorical Series
    print(".iloc[0:3] on categorical Series:")
    display(product_series.iloc[0:3])

    print(".loc[0:2] on categorical Series:")
    display(product_series.loc[0:2])

    # Convert categories to integer codes (0-5)
    codes = product_series.cat.codes

    #  6. DataFrame creation 
    print(" 6. DataFrame — codes and category names ")

    df_coded = pd.DataFrame({
        "code": codes.values,
        "product_line": product_series.values
    })

    print("\ndisplay() — DataFrame with codes (first 10 rows):")
    display(df_coded.head(10))

    # Unique mapping table
    print("Unique code → category mapping:")
    mapping = df_coded.drop_duplicates().sort_values("code").reset_index(drop=True)
    display(mapping)


def task_b(df):
    """
    Task B: Info and statistical analysis.
    - Print DataFrame info (shape, dtypes, non-null counts, describe)
    - Extract the hour from the 'Time' column
    - Group by hour, compute mean Sales (receipt total)
    - Find most and least profitable hours
    - Calculate how many times best > worst (rounded to hundredths)

    Note: Time format in this dataset is "H:MM:SS AM/PM" (12-hour).
          'Sales' column = receipt total (called 'Total' in some dataset versions).
    """

    #  DataFrame info per parameter 
    print("\n Shape ")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n Column dtypes ")
    print(df.dtypes.to_string())

    print("\n Null values per column ")
    print(df.isnull().sum().to_string())

    print("\n Basic statistics (describe) ")
    print(df.describe().to_string())

    #  Extract hour from Time column 
    # Time stored as "1:08:00 PM" — use 12-hour format with seconds
    df = df.copy()
    df["hour"] = pd.to_datetime(df["Time"], format="%I:%M:%S %p").dt.hour

    #  Average Sales grouped by hour 
    hourly_avg = df.groupby("hour")["Sales"].mean().round(2)

    print("\n Average Sales per hour ")
    print(hourly_avg.to_string())

    #  Most and least profitable hours 
    best_hour  = hourly_avg.idxmax()
    worst_hour = hourly_avg.idxmin()

    best_avg  = hourly_avg[best_hour]
    worst_avg = hourly_avg[worst_hour]

    print(f"\nMost profitable hour : {best_hour}:00  → avg Sales = {best_avg}")
    print(f"Least profitable hour: {worst_hour}:00  → avg Sales = {worst_avg}")

    #  Answer 
    ratio = round(best_avg / worst_avg, 2)
    print(f"\nAnswer: avg Sales at {best_hour}:00 is {ratio} times greater"
          f" than at {worst_hour}:00.")



def task6_run():
    """Entry point: load data and run both tasks."""
    print("Loading dataset...")
    try:
        df = load_data(CSV_PATH)
        print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns.")
    except FileNotFoundError:
        print(f"ERROR: '{CSV_PATH}' not found. Place the CSV next to this script.")
        return

    task_a(df)
    task_b(df)
