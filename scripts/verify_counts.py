import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "sip_inflows",
    "category_inflows",
    "folio_count",
    "fact_performance",
    "fact_transactions",
    "portfolio_holdings",
    "benchmark_indices"
]

for t in tables:
    print(f"\nTable: {t}")
    print(pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {t}",
        conn
    ))

conn.close()