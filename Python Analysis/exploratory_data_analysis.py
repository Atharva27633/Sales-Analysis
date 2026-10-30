import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("SampleSuperstore_cleaned.csv")

# Display the first five rows
df.head()




print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())





region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
)

region_analysis["Profit_Margin"] = (
    region_analysis["Total_Profit"]
    / region_analysis["Total_Sales"]
) * 100

region_analysis = region_analysis.sort_values(
    "Total_Sales",
    ascending=False
)

print(region_analysis.round(2))




region_analysis["Total_Sales"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()



region_analysis["Total_Profit"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()



segment_analysis = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

segment_analysis["Profit_Margin"] = (
    segment_analysis["Total_Profit"]
    / segment_analysis["Total_Sales"]
) * 100

print(segment_analysis.sort_values(
    "Total_Profit",
    ascending=False
).round(2))



plt.figure(figsize=(9, 5))

sns.barplot(
    data=segment_analysis.reset_index(),
    x="Segment",
    y="Total_Sales"
)

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()



plt.figure(figsize=(9, 5))

sns.barplot(
    data=segment_analysis.reset_index(),
    x="Segment",
    y="Total_Profit"
)

plt.title("Profit by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.show()





category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

category_analysis["Profit_Margin"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"]
) * 100

print(category_analysis.sort_values(
    "Total_Profit",
    ascending=False
).round(2))



category_analysis["Total_Profit"].sort_values().plot(
    kind="barh",
    figsize=(10, 5)
)

plt.title("Total Profit by Category")
plt.xlabel("Total Profit")
plt.ylabel("Category")

plt.tight_layout()
plt.show()



subcategory_analysis = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)




subcategory_analysis["Profit_Margin"] = (
    subcategory_analysis["Total_Profit"]
    / subcategory_analysis["Total_Sales"]
) * 100

subcategory_analysis = subcategory_analysis.sort_values(
    "Total_Profit",
    ascending=False
)

print(subcategory_analysis.round(2))



print("Top 5 sub-categories by profit:")

print(
    subcategory_analysis.nlargest(
        5, "Total_Profit"
    ).round(2)
)



print("Bottom 5 sub-categories by profit:")

print(
    subcategory_analysis.nsmallest(
        5, "Total_Profit"
    ).round(2)
)



plt.figure(figsize=(12, 8))

sns.barplot(
    data=subcategory_analysis.reset_index(),
    x="Total_Profit",
    y="Sub-Category"
)

plt.title("Profitability by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.show()





discount_analysis = df.groupby("Discount").agg(
    Average_Profit=("Profit", "mean"),
    Total_Profit=("Profit", "sum"),
    Total_Sales=("Sales", "sum"),
    Number_of_Lines=("Profit", "size")
)

print(discount_analysis.round(2))



plt.figure(figsize=(10, 6))

sns.lineplot(
    data=discount_analysis.reset_index(),
    x="Discount",
    y="Average_Profit",
    marker="o"
)

plt.title("Relationship Between Discount and Average Profit")
plt.xlabel("Discount")
plt.ylabel("Average Profit")

plt.axhline(y=0, linestyle="--", linewidth=1)

plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.4
)

plt.title("Discount vs. Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.axhline(y=0, linestyle="--", linewidth=1)

plt.tight_layout()
plt.show()



correlation = df["Discount"].corr(df["Profit"])

print("Discount-Profit Correlation:", round(correlation, 3))



category_discount = df.groupby(
    ["Category", "Discount"]
).agg(
    Average_Profit=("Profit", "mean"),
    Total_Profit=("Profit", "sum"),
    Total_Sales=("Sales", "sum")
).reset_index()

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=category_discount,
    x="Discount",
    y="Average_Profit",
    hue="Category",
    marker="o"
)

plt.title("Discount vs. Average Profit by Category")
plt.xlabel("Discount")
plt.ylabel("Average Profit")

plt.axhline(y=0, linestyle="--", linewidth=1)

plt.tight_layout()
plt.show()




total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else np.nan
)




print("=" * 40)
print("SUPERSTORE BUSINESS SUMMARY")
print("=" * 40)

print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Profit Margin: {profit_margin:.2f}%")


discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

discount_analysis["Profit_Margin"] = (
    discount_analysis["Total_Profit"]
    / discount_analysis["Total_Sales"]
) * 100

print(discount_analysis.round(2))