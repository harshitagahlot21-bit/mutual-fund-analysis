SELECT fund_house,aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT strftime('%Y-%m',date)
AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

SELECT month,yoy_growth_pct
FROM sip_inflows;

SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT category,
AVG(return_5yr_pct)
FROM fact_performance
GROUP BY category;

SELECT transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

SELECT state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

SELECT sector,
AVG(weight_pct)
FROM portfolio_holdings
GROUP BY sector;

SELECT index_name,
AVG(close_value)
FROM benchmark_indices
GROUP BY index_name;