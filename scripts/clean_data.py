import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# Load files
fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
txn = pd.read_csv("data/raw/08_investor_transactions.csv")
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
bench = pd.read_csv("data/raw/10_benchmark_indices.csv")

# NAV CLEANING
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code","date"])
nav = nav.drop_duplicates()
nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")
nav = nav[nav["nav"] > 0]
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# INVESTOR TRANSACTIONS
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .replace({
        "sip":"SIP",
        "SIP":"SIP",
        "lumpsum":"Lumpsum",
        "Lumpsum":"Lumpsum",
        "redemption":"Redemption",
        "Redemption":"Redemption"
    })
)

txn["amount_inr"] = pd.to_numeric(
    txn["amount_inr"], errors="coerce"
)

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified","Pending","Rejected"]

txn["kyc_valid"] = txn["kyc_status"].isin(valid_kyc)

# PERFORMANCE
returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_ratio_flag"] = ~(
    perf["expense_ratio_pct"]
    .between(0.1,2.5)
)

# Save cleaned files
fund.to_csv("data/processed/01_fund_master_clean.csv",index=False)
nav.to_csv("data/processed/02_nav_history_clean.csv",index=False)
aum.to_csv("data/processed/03_aum_by_fund_house_clean.csv",index=False)
sip.to_csv("data/processed/04_monthly_sip_inflows_clean.csv",index=False)
category.to_csv("data/processed/05_category_inflows_clean.csv",index=False)
folio.to_csv("data/processed/06_industry_folio_count_clean.csv",index=False)
perf.to_csv("data/processed/07_scheme_performance_clean.csv",index=False)
txn.to_csv("data/processed/08_investor_transactions_clean.csv",index=False)
holdings.to_csv("data/processed/09_portfolio_holdings_clean.csv",index=False)
bench.to_csv("data/processed/10_benchmark_indices_clean.csv",index=False)

print("All cleaned files saved.")