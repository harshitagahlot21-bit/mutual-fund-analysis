import pandas as pd
import os

print("=" * 60)
print("DAY 1 - DATA INGESTION")
print("=" * 60)

# Folder Path
folder = "data/raw"

# Load all CSV files
for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n" + "=" * 60)
        print("FILE :", file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

# ==================================================
# FUND MASTER ANALYSIS
# ==================================================

print("\n" + "=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

# ==================================================
# AMFI CODE VALIDATION
# ==================================================

print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\nMissing AMFI Codes:")
print(missing_codes)

print("\nTotal Missing Codes:")
print(len(missing_codes))

# ==================================================
# DATA QUALITY SUMMARY
# ==================================================

print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print("Fund Master Records :", len(fund_master))
print("NAV History Records :", len(nav_history))

print("Unique AMFI Codes in Fund Master :",
      fund_master["amfi_code"].nunique())

print("Unique AMFI Codes in NAV History :",
      nav_history["amfi_code"].nunique())

if len(missing_codes) == 0:
    print("\nAll AMFI codes successfully validated.")
else:
    print("\nSome AMFI codes are missing in NAV history.")