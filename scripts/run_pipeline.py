"""
Bluestock Portfolio Analytics Master Pipeline.
Coordinates VaR/CVaR compute, Sharpe calculation, and Investor cohort analysis.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data():
    """Load and preprocess synthetic datasets."""
    returns = pd.read_csv('returns.csv', index_col=0, parse_dates=True)
    tx = pd.read_csv('transactions.csv', parse_dates=['tx_date'])
    weights = pd.read_csv('weights.csv')
    return returns, tx, weights

def compute_risk_metrics(returns):
    """Calculate VaR (95%) and CVaR for all schemes."""
    var_95 = returns.quantile(0.05)
    cvar = returns[returns < var_95].mean()
    metrics = pd.DataFrame({'VaR_95': var_95, 'CVaR': cvar})
    metrics.to_csv('var_cvar_report.csv')
    print("Risk metrics saved to var_cvar_report.csv")

def plot_rolling_sharpe(returns, top_n=5):
    """Plot 90-day rolling Sharpe ratio for key funds."""
    rolling_sharpe = (returns.rolling(90).mean() / returns.rolling(90).std()) * np.sqrt(252)
    plt.figure(figsize=(12, 6))
    for col in returns.columns[:top_n]:
        plt.plot(rolling_sharpe[col], label=col)
    plt.title('90-Day Rolling Sharpe Ratio')
    plt.legend()
    plt.savefig('rolling_sharpe_chart.png')
    print("Sharpe chart saved as rolling_sharpe_chart.png")

def main():
    print("Starting Pipeline...")
    returns, tx, weights = load_data()
    compute_risk_metrics(returns)
    plot_rolling_sharpe(returns)
    print("Pipeline Execution Complete.")

if __name__ == "__main__":
    main()