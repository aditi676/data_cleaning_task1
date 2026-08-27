# Task 1: Data Cleaning and Preprocessing — Netflix Movies and TV Shows

## 📌 Objective
Clean and prepare the **Netflix Movies and TV Shows** dataset (from Kaggle) by handling missing values, duplicates, inconsistent formatting, and incorrect data types — making it analysis-ready.

## 🛠 Tools Used
- Python (Pandas)
- VS Code

## 📁 Files in this Repository
| File | Description |
|---|---|
| `netflix_titles.csv` | Original raw dataset |
| `clean_data.py` | Python script used to clean the data |
| `netflix_titles_cleaned.csv` | Final cleaned dataset |
| `README.md` | This file — summary of the cleaning process |

## 🔍 Dataset Overview
- **Rows (original):** 8,807
- **Columns:** 12 (`show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`)

## 🧹 Steps Performed

### 1. Identified Missing Values
Used `.isnull().sum()` to find nulls in each column:
- `director` — 2,634 missing
- `cast` — 825 missing
- `country` — 831 missing
- `date_added` — 10 missing
- `rating` — 4 missing
- `duration` — 3 missing

### 2. Handled Missing Values
- Filled `director`, `cast`, and `country` with `"Unknown"` since dropping them would remove too much data.
- Dropped rows with missing `rating`, `duration`, and `date_added` since these were very few (under 15 rows total) and hard to infer accurately.

### 3. Removed Duplicate Rows
Checked with `.duplicated().sum()` and removed exact duplicate rows using `.drop_duplicates()`.

### 4. Cleaned Column Headers
Standardized all column names to lowercase with underscores instead of spaces, using:
```python
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
```

### 5. Standardized Text Values
- Trimmed extra whitespace from `type` and `country` columns.
- Applied consistent casing (e.g., `Movie` / `TV Show`) using `.str.title()`.

### 6. Fixed Date Format
Converted `date_added` from string to proper `datetime` type using `pd.to_datetime()`, replacing inconsistent text formats with a single standard format.

### 7. Fixed Data Types
- Converted `release_year` to integer type.
- Extracted numeric duration (in minutes, for movies) into a new column for easier numerical analysis.

### 8. Exported Cleaned Data
Saved the final cleaned dataset as `netflix_titles_cleaned.csv` using `.to_csv()`.

## ✅ Result
- **Rows before cleaning:** 8,807
- **Rows after cleaning:** *(update with your final count after running the script)*
- **Duplicates removed:** *(update with your actual count)*
- Dataset is now free of missing critical values, duplicate rows, and formatting inconsistencies — ready for analysis or visualization.

## 📚 Key Learnings
- Difference between `dropna()` (removes data) and `fillna()` (imputes data), and when to use each.
- How to identify and standardize inconsistent text and date formats.
- Importance of checking data types before analysis to avoid downstream errors.

