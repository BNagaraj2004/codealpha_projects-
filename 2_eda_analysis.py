import pandas as pd

file_path = r"C:\Users\mohan\Pictures\Acer\nagaraj\datasets\books_raw_data.csv"

df = pd.read_csv(file_path, encoding="utf-8")


# ---- CLEAN PRICE ----
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("[^0-9.]", "", regex=True)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Price"].fillna(0, inplace=True)

# ---- CLEAN RATING ----
rating_map = {
    "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map).fillna(0).astype(int)

# ---- STOCK FLAG ----
df["In_Stock"] = df["Availability"].apply(
    lambda x: 1 if "In stock" in str(x) else 0
)

# ---- BASIC VALIDATION ----
assert df["Price"].dtype in ["float64", "int64"]
assert df["Rating"].dtype == "int64"

print("Total Books:", len(df))
print("Average Price:", round(df["Price"].mean(), 2))
print("Rating Distribution:\n", df["Rating"].value_counts())

df.to_csv("books_cleaned_data.csv", index=False, encoding="utf-8")

print("✅ EDA completed successfully.")

