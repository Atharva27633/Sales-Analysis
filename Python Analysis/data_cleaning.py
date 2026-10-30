import pandas as pd
import numpy as np

print("Libraries imported successfully!")

df = pd.read_excel("SampleSuperstore.xlsx")

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

df.head()

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Cells:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNumerical Summary:")
print(df.describe())

print("\n--- Duplicate Inspection ---")

duplicate_rows = df[df.duplicated(keep=False)]

print("Rows involved in duplicates:", len(duplicate_rows))
print(duplicate_rows.head(10))

# Create a separate working copy
df_clean = df.copy()

# Record the original row count
original_rows = len(df_clean)

# Remove exact duplicate rows from the working copy
df_clean = df_clean.drop_duplicates()

# Compare the results
print("\n--- Cleaning Results ---")
print("Original rows:", original_rows)
print("Rows after removing duplicates:", len(df_clean))
print("Rows removed:", original_rows - len(df_clean))
print("Remaining duplicate rows:", df_clean.duplicated().sum())

df_clean.to_csv("SampleSuperstore_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")

print("\n--- Numerical Summary ---")

columns = ["Sales", "Profit", "Quantity", "Discount"]

print(df_clean[columns].describe())

print("\n--- IQR Outlier Analysis ---")

for column in ["Sales", "Profit", "Quantity", "Discount"]:
    Q1 = df_clean[column].quantile(0.25)
    Q3 = df_clean[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df_clean[
        (df_clean[column] < lower_bound) |
        (df_clean[column] > upper_bound)
    ]

    print(f"\nColumn: {column}")
    print("Lower bound:", round(lower_bound, 2))
    print("Upper bound:", round(upper_bound, 2))
    print("Potential outliers:", len(outliers))


    print("\n--- Five Largest Losses ---")

largest_losses = df_clean.nsmallest(5, "Profit")

print(largest_losses[
    ["Category", "Sub-Category", "Sales", "Quantity", "Discount", "Profit"]
])



print("\n--- Sales and Profit by Sub-Category ---")

subcategory_analysis = (
    df_clean.groupby("Sub-Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("Sales", "count")
    )
    .round(2)
)

subcategory_analysis = subcategory_analysis.sort_values(
    by="Total_Profit"
)

print(subcategory_analysis)




print("\n--- Least Profitable Sub-Categories ---")
print(subcategory_analysis.head(5))

print("\n--- Most Profitable Sub-Categories ---")
print(subcategory_analysis.tail(5).sort_values(
    by="Total_Profit",
    ascending=False
))


print("\n--- Category-Level Analysis ---")

category_analysis = (
    df_clean.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .round(2)
    .sort_values(by="Total_Sales", ascending=False)
)

print(category_analysis)






print("\n--- Final Results Verification ---")

# Verify sub-category profitability
subcategory_analysis = (
    df_clean.groupby("Sub-Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .round(2)
)

print("\nLowest-profit sub-category:")
print(subcategory_analysis["Total_Profit"].idxmin())
print(subcategory_analysis["Total_Profit"].min())

print("\nHighest-profit sub-category:")
print(subcategory_analysis["Total_Profit"].idxmax())
print(subcategory_analysis["Total_Profit"].max())

# Verify Machines
print("\nMachines results:")
print(subcategory_analysis.loc["Machines"])

# Verify category sales
category_sales = df_clean.groupby("Category")["Sales"].sum()

print("\nCategory with highest sales:")
print(category_sales.idxmax())
print("Total sales:", round(category_sales.max(), 2))





print("\n--- Final Dataset Summary ---")

print("Original row count:", len(df))
print("Cleaned row count:", len(df_clean))

print("\nOriginal dataset:")
print("Total sales:", round(df["Sales"].sum(), 2))
print("Total profit:", round(df["Profit"].sum(), 2))

print("\nCleaned dataset:")
print("Total sales:", round(df_clean["Sales"].sum(), 2))
print("Total profit:", round(df_clean["Profit"].sum(), 2))

print("\nCleaned dataset profit margin:")
profit_margin = (
    df_clean["Profit"].sum() / df_clean["Sales"].sum()
) * 100

print(round(profit_margin, 2), "%")

print("\n--- Row Count Verification ---")

print("Original dataset rows:", len(df))
print("Original duplicate rows:", df.duplicated().sum())

df_check = df.copy()
df_check = df_check.drop_duplicates()

print("Rows after removing duplicates:", len(df_check))
print("Duplicate rows remaining:", df_check.duplicated().sum())

print("\nCurrent working dataset rows:", len(df_clean))
print("Current working dataset duplicates:", df_clean.duplicated().sum())