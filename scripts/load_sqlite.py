import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {
"dim_fund":"data/processed/01_fund_master_clean.csv",
"fact_nav":"data/processed/02_nav_history_clean.csv",
"fact_aum":"data/processed/03_aum_by_fund_house_clean.csv",
"sip_inflows":"data/processed/04_monthly_sip_inflows_clean.csv",
"category_inflows":"data/processed/05_category_inflows_clean.csv",
"folio_count":"data/processed/06_industry_folio_count_clean.csv",
"fact_performance":"data/processed/07_scheme_performance_clean.csv",
"fact_transactions":"data/processed/08_investor_transactions_clean.csv",
"portfolio_holdings":"data/processed/09_portfolio_holdings_clean.csv",
"benchmark_indices":"data/processed/10_benchmark_indices_clean.csv"
}

for table,file in files.items():
    df = pd.read_csv(file)
    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

print("SQLite DB Created")
