# Bluestock Mutual Fund Analytics Platform

Professional portfolio analytics engine for risk profiling and investor cohort analysis.

## 🚀 Setup Instructions
1. Clone the repository: `git clone <your-repo-url>`
2. Install dependencies: `pip install pandas numpy matplotlib`
3. Generate data: `python generate_data.py`
4. Run analysis: `python run_pipeline.py`

## 📊 Deliverables
- **ETL Pipeline:** `run_pipeline.py` handles end-to-end data processing.
- **Risk Report:** `var_cvar_report.csv` contains tail-risk metrics.
- **Charts:** `rolling_sharpe_chart.png` visualizes fund efficiency.

## 📝 Analysis Highlights
- **VaR/CVaR:** Computed for 40 schemes using historical simulation.
- **Sharpe Ratio:** 90-day rolling window with annualization factor (sqrt(252)).
- **Continuity Analysis:** Investors with >35 day gaps flagged as "At-Risk".
