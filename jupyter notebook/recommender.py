# recommender.py
import pandas as pd
import sys

def recommend_funds(risk_appetite):
    try:
        # Aapki uploaded file load karega
        df = pd.read_csv('07_scheme_performance.csv')
    except FileNotFoundError:
        print("Error: '07_scheme_performance.csv' file nahi mili! Please check karein.")
        return

    # User input ko normalize karna (e.g. low -> Low)
    risk_input = risk_appetite.strip().capitalize()
    
    # Matching risk grade filter karein
    filtered_df = df[df['risk_grade'].str.capitalize() == risk_input]
    
    if filtered_df.empty:
        print(f"\nNo funds found matching risk profile: '{risk_appetite}'")
        print("Available profiles: Low, Moderate, High, Very High, Moderately High")
        return
        
    # Top 3 funds by Sharpe Ratio select karein
    top_3 = filtered_df.sort_values(by='sharpe_ratio', ascending=False).head(3)
    
    print(f"\n=================== TOP 3 FUND RECOMMENDATIONS FOR: {risk_input.upper()} RISK ===================")
    print(top_3[['amfi_code', 'scheme_name', 'category', 'sharpe_ratio']].to_string(index=False))
    print("=====================================================================================")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_risk = sys.argv[1]
    else:
        user_risk = input("Enter risk appetite (Low / Moderate / High / Very High): ")
    recommend_funds(user_risk)