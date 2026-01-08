# =========================================
# ALL-IN-ONE ERROR-FREE DATA VISUALIZATION
# =========================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------- PATH SETUP ----------
BASE_DIR = os.getcwd()
file_path = os.path.join(BASE_DIR, "books_cleaned_data.csv")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

df = pd.read_csv(file_path, encoding="utf-8")

# ---------- BASIC VALIDATION ----------
for col in ["Price", "Rating", "In_Stock"]:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# ==================================================
# VISUAL 1: Rating Distribution (Bar Chart)
# ==================================================
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(6,4))
bars = plt.bar(
    rating_counts.index.astype(str),
    rating_counts.values,
    color=plt.cm.tab10.colors[:len(rating_counts)]
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center", va="bottom"
    )

plt.tight_layout()
plt.show()

# ==================================================
# VISUAL 2: Price Distribution (Histogram)
# ==================================================
counts, bins, patches = plt.hist(
    df["Price"],
    bins=20,
    color="#2196F3",
    edgecolor="black"
)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

for count, patch in zip(counts, patches):
    if count > 0:
        plt.text(
            patch.get_x() + patch.get_width()/2,
            count,
            int(count),
            ha="center", va="bottom"
        )

plt.tight_layout()
plt.show()

# ==================================================
# VISUAL 3: Average Price by Rating (Line Chart)
# ==================================================
avg_price = df.groupby("Rating")["Price"].mean()

plt.figure(figsize=(6,4))
plt.plot(
    avg_price.index,
    avg_price.values,
    marker="o",
    color="#E91E63"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price")

for x, y in zip(avg_price.index, avg_price.values):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")

plt.tight_layout()
plt.show()

# ==================================================
# VISUAL 4: Stock Availability (Pie Chart)
# ==================================================
stock_counts = df["In_Stock"].value_counts()

labels = ["In Stock" if i == 1 else "Out of Stock" for i in stock_counts.index]

plt.figure(figsize=(5,5))
plt.pie(
    stock_counts.values,
    labels=labels,
    autopct="%1.1f%%",
    colors=["#4CAF50", "#F44336"],
    startangle=90
)

plt.title("Stock Availability")
plt.tight_layout()
plt.show()

# ==================================================
# VISUAL 5: Price Distribution by Rating (Box Plot)
# ==================================================
ratings_sorted = sorted(df["Rating"].unique())
price_data = [df[df["Rating"] == r]["Price"] for r in ratings_sorted]

plt.figure(figsize=(6,4))
box = plt.boxplot(price_data, patch_artist=True, labels=ratings_sorted)

for patch in box["boxes"]:
    patch.set_facecolor("#90CAF9")

plt.title("Price Distribution by Rating")
plt.xlabel("Rating")
plt.ylabel("Price")

plt.tight_layout()
plt.show()

# ==================================================
# VISUAL 6: Top 10 Most Expensive Books (Horizontal Bar)
# ==================================================
top10 = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(8,4))
bars = plt.barh(
    top10["Title"],
    top10["Price"],
    color="#FF9800"
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price")
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height()/2,
        f"{bar.get_width():.2f}",
        va="center"
    )

plt.tight_layout()
plt.show()

# ==================================================
# VISUAL 7: Rating Percentage Distribution
# ==================================================
rating_percent = (rating_counts / rating_counts.sum()) * 100

plt.figure(figsize=(6,4))
bars = plt.bar(
    rating_percent.index.astype(str),
    rating_percent.values,
    color="#9C27B0"
)

plt.title("Rating Percentage Distribution")
plt.xlabel("Rating")
plt.ylabel("Percentage (%)")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():.1f}%",
        ha="center", va="bottom"
    )

plt.tight_layout()
plt.show()

print("✅ All 7 visualizations generated successfully without errors.")

