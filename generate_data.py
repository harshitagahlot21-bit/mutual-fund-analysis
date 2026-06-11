"""
Synthetic Data Generator for Bluestock MF Capstone.
Creates mock CSV files for returns, transactions, and sector weights.
"""
import pandas as pd
import numpy as np
import os

def generate_mock_datasets():
    # 1. Daily Returns (40 schemes)
    dates = pd.date_range(start="2023-01-01", periods=500, freq='D')
    schemes = [f"Fund_{i}" for i in range(1, 41)]
    returns_data = np.random.normal(0.0005, 0.015, (500, 40))
    df_returns = pd.DataFrame(returns_data, index=dates, columns=schemes)
    df_returns.to_csv('returns.csv')

    # 2. Transactions
    investors = [f"INV_{i}" for i in range(100, 200)]
    tx_data = {
        'investor_id': np.random.choice(investors, 1000),
        'tx_date': np.random.choice(dates, 1000),
        'amount': np.random.randint(1000, 50000, 1000),
        'fund_name': np.random.choice(schemes, 1000)
    }
    pd.DataFrame(tx_data).to_csv('transactions.csv', index=False)

    # 3. Sector Weights
    sectors = ['Tech', 'Fin', 'Health', 'Energy', 'Cons']
    weights = []
    for fund in schemes:
        w = np.random.dirichlet(np.ones(5), size=1)[0]
        for s, val in zip(sectors, w):
            weights.append({'fund_name': fund, 'sector': s, 'weight': val})
    pd.DataFrame(weights).to_csv('weights.csv', index=False)
    print("Mock datasets generated: returns.csv, transactions.csv, weights.csv")

if __name__ == "__main__":
    generate_mock_datasets()