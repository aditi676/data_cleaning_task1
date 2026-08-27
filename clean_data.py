import pandas as pd

# CSV load
df = pd.read_csv("netflix_titles.csv")

# original info
print("Original Shape:", df.shape)
print(df.isnull().sum())

# duplicates remove
df = df.drop_duplicates()

# column names clean
df.columns = df.columns.str.lower().str.replace(" ", "_")

# text columns strip
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("string").str.strip()

# date column convert
if "date_added" in df.columns:
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# fill missing values
for col in ["director", "cast", "country", "rating"]:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

# save cleaned file
df.to_csv("netflix_titles_cleaned.csv", index=False)

print("Cleaned Shape:", df.shape)
print("File saved as netflix_titles_cleaned.csv")