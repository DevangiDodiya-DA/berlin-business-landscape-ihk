# Project: Berlin Business Landscape Analysis
# Data Source: IHK Berlin Open Data (CC0 1.0)
# Description: This script cleans raw commercial data for Tableau visualization.import pandas as pd
import pandas as pd

# ---------------------------------------------------------
# STEP 1 — Load dataset (correct Git LFS URL)
# ---------------------------------------------------------
url = "https://media.githubusercontent.com/media/IHKBerlin/IHKBerlin_Gewerbedaten/master/data/IHKBerlin_Gewerbedaten.csv"

print("Downloading dataset...")
df = pd.read_csv(url, encoding="utf-8")

print("\nColumns in dataset:")
print(df.columns.tolist())
print("\nInitial shape:", df.shape)

# ---------------------------------------------------------
# STEP 2 — Validate required columns (based on your dataset)
# ---------------------------------------------------------
required_cols = ["longitude", "latitude", "ihk_branch_desc"]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Dataset is missing required columns: {missing}")

# ---------------------------------------------------------
# STEP 3 — Drop rows missing coordinates or industry
# ---------------------------------------------------------
df = df.dropna(subset=["longitude", "latitude", "ihk_branch_desc"])

# ---------------------------------------------------------
# STEP 4 — Clean employees_range
# ---------------------------------------------------------
df["employees_range"] = df["employees_range"].fillna("Unknown")

# ---------------------------------------------------------
# STEP 5 — Create simplified industry name
# ---------------------------------------------------------
df["industry_clean"] = df["ihk_branch_desc"].astype(str).str.split(",").str[0]

# ---------------------------------------------------------
# STEP 6 — Convert business_age to numeric
# ---------------------------------------------------------
df["business_age"] = pd.to_numeric(df["business_age"], errors="coerce")

# ---------------------------------------------------------
# STEP 7 — Export cleaned dataset
# ---------------------------------------------------------
output_file = "berlin_business_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nSuccess! Cleaned file saved as:", output_file)
print("Final shape:", df.shape)
