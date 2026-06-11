# Data Dictionary

## 01_fund_master.csv

| Column       | Data Type | Description                   |
| ------------ | --------- | ----------------------------- |
| amfi_code    | Integer   | Unique AMFI scheme identifier |
| scheme_name  | Text      | Name of mutual fund scheme    |
| fund_house   | Text      | Asset Management Company name |
| category     | Text      | Scheme category               |
| sub_category | Text      | Scheme sub-category           |

## 02_nav_history.csv

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Decimal   | Net Asset Value   |

## 03_aum_by_fund_house.csv

| Column     | Data Type | Description                         |
| ---------- | --------- | ----------------------------------- |
| fund_house | Text      | AMC name                            |
| aum_crore  | Decimal   | Assets Under Management (Crore INR) |
| date       | Date      | Reporting date                      |

## 04_monthly_sip_inflows.csv

| Column           | Data Type | Description               |
| ---------------- | --------- | ------------------------- |
| month            | Date      | SIP reporting month       |
| sip_amount_crore | Decimal   | Monthly SIP inflow amount |

## 05_category_inflows.csv

| Column           | Data Type | Description          |
| ---------------- | --------- | -------------------- |
| category         | Text      | Mutual fund category |
| net_inflow_crore | Decimal   | Net inflow amount    |

## 06_industry_folio_count.csv

| Column      | Data Type | Description           |
| ----------- | --------- | --------------------- |
| month       | Date      | Reporting month       |
| folio_count | Integer   | Total investor folios |

## 07_scheme_performance.csv

| Column            | Data Type | Description       |
| ----------------- | --------- | ----------------- |
| amfi_code         | Integer   | Scheme identifier |
| return_1yr_pct    | Decimal   | 1 Year Return (%) |
| return_3yr_pct    | Decimal   | 3 Year Return (%) |
| return_5yr_pct    | Decimal   | 5 Year Return (%) |
| expense_ratio_pct | Decimal   | Expense Ratio (%) |

## 08_investor_transactions.csv

| Column           | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| investor_id      | Text      | Unique investor identifier |
| amfi_code        | Integer   | Scheme identifier          |
| transaction_date | Date      | Transaction date           |
| transaction_type | Text      | SIP / Lumpsum / Redemption |
| amount_inr       | Decimal   | Transaction amount         |
| kyc_status       | Text      | Investor KYC status        |

## 09_portfolio_holdings.csv

| Column        | Data Type | Description          |
| ------------- | --------- | -------------------- |
| amfi_code     | Integer   | Scheme identifier    |
| security_name | Text      | Holding security     |
| sector        | Text      | Industry sector      |
| weight_pct    | Decimal   | Portfolio weight (%) |

## 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| index_name  | Text      | Benchmark index name |
| date        | Date      | Trading date         |
| close_value | Decimal   | Closing index value  |

## Source References

All datasets sourced from Bluestock Mutual Fund Analytics Project CSV files.

### Deliverables Generated

* Cleaned CSV files in `data/processed/`
* SQLite database: `bluestock_mf.db`
* SQL Schema: `sql/schema.sql`
* Analytical Queries: `sql/queries.sql`
* Data Dictionary: `data_dictionary.md`
