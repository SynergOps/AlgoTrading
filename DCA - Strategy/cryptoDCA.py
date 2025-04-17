# Description: This script calculates the performance of a Dollar-Cost Averaging (DCA)
# strategy for various cryptocurrencies over a specified period.
# It reads historical price data from CSV files, computes the total investment,
# final value of the investment, and the return on investment (ROI).
# The results are displayed in a tabular format in the console.
# LICENSE: MIT
# Copyright: Salih Emin
# Date: 2025-04-01
# Website: https://cerebrux.net
import pandas as pd
import os
from datetime import datetime
from tabulate import tabulate

# List of symbols and corresponding CSV filenames
symbols = ['BTC', 'ETH', 'LTC', 'XRP', 'ADA']
csv_files = {sym: f'data/{sym}.csv' for sym in symbols}
monthly_investment = 20  # Monthly investment amount in euros
results = []

for sym, path in csv_files.items():
    if not os.path.exists(path):
        # Skip symbols without uploaded CSV
        continue
    
    # Read CSV, parse dates
    df = pd.read_csv(path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    
    # Sort the index to ensure it's monotonic
    df.sort_index(inplace=True)
    
    # Filter period Jan 2018 - Mar 2025
    start, end = '2018-01-01', '2025-03-31'
    df = df.loc[start:end]
    
    # Get month-end closing prices
    monthly_close = df['Close'].resample('ME').last()
    
    # Calculate DCA: invested each month
    coins_accumulated = (monthly_investment / monthly_close).cumsum()
    print(f"Coins accumulated for {sym}: {coins_accumulated.iloc[-1]}")
    # Calculate total months and final price
    total_months = len(monthly_close)
    total_invested = total_months * monthly_investment
    final_price = monthly_close.iloc[-1]
    print(f"Final price for {sym}: {final_price}")
    # Calculate final value and ROI
    final_value = coins_accumulated.iloc[-1] * final_price
    roi = (final_value - total_invested) / total_invested * 100

    results.append({
        'Σύμβολο': sym,
        'Μήνες': total_months,
        'Τελική Τιμή (€)': round(final_price, 2),
        'Συγκεντρωμένα crypto': round(coins_accumulated.iloc[-1], 4),
        'Τελική Αξία Επένδυσης (€)': round(final_value, 2),
        'ROI (%)': round(roi, 2)
    })

# Create DataFrame and display
results_df = pd.DataFrame(results)
#tools.display_dataframe_to_user("DCA Performance (Jan 2018 – Mar 2025)", results_df)

print("Επιδόσεις του DCA (Ιαν 2018 – Μαρ 2025)")
print(tabulate(
    results_df, 
    headers='keys', 
    tablefmt='grid', 
    numalign='right',
    stralign='center'
))
