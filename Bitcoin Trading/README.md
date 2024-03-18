## BTC Ichimoku Momentum Strategy

__version 3.3.0__

This strategy is developed for swing trading on BTC spot accounts. Thus, use it only for buying and holding it until the exit signal tells you to sell your entire position. The main advantage of this system in my opinion is in limiting the max drawdown significantly versus buy & hodl. Theoretically much better returns can be made by just holding, but that's also a good way to lose 70%+ of your capital in the inevitable bear markets (also speaking from experience). In saying all of that, the future is fundamentally unknowable and past results in no way guarantee future performance.
Last but not least, the code also incorporates alerts and a monthly view of performance based on the results of the closing trades

It is based on 2 strategies: 
- Ichimoku Kinko Hyo Tenkan/Kijunsen Cross strategy
- Bitcoin Momentum Strategy by ZenAndTheArtOfTrading

Basically, the system "ratchets" up the stop-loss to be much tighter during high bearish volatility to protect open profits from downside moves, but loosens the stop loss during sustained bullish momentum to let the position ride.


Long only Position:

- Buy at the next candle after Tenkan/Kijun-sen bullish cross happens
- Sell at the next candle after Tenkan/Kijun-sen bearish cross occurs.
- Re-buy if you get Tenkan/Kijun-sen bullish cross again and Sell your holding when Tenkan/Kijun-sen bearish cross occurs.

Default parameters:
- HTF: Weekly Chart
- EMA: 20-Period
- ATR: 5-period
- Bar Lookback: 7
- Ichimoku : Tenkan and Kijunsen
- Trailing Take Profit Stop loss: 0.2
- Hard Stop loss: -10% from entry price
- Commission Fees: -0.8% per trade based on Binances Taker fees. Change it according your exchanges 

Conditions and Entry:

1. Condition #1:
Bitcoin's current price must be trading above its higher-timeframe EMA (Weekly 20 EMA). 
2. Condition #2: 
Bitcoin must not be in 'caution' condition (no large bearish volatility swings recently).
3. Condition #3: Tenkan must cross above the Kijunsen
4. Conditions met:
Enter at next bar's open if conditions are met and we are not already involved in a trade.

**"Caution" Condition:**
Defined as true if BTC's recent 7-bar swing high minus current bar's low is > 1.5x ATR, or Daily close < Daily 20-EMA.

**Trailing Stop:**
Stop is trailed 1 ATR from recent swing high, or 20% of ATR if in caution condition (ie. 0.2 ATR).
Exit on next bar open upon a close below stop loss.

**Hard Stop Loss**: It's set 10% below the entry price. If you want to disable it, just put an number higher than 100, in the settings

**Cost of Trading:**
The script uses no leverage and a default total round-trip commission of 0.3% which is what I pay on my exchange based on their tier structure, but this can vary widely from exchange to exchange and higher commission fees will have a significantly negative impact on realized gains so make sure to always input the correct theoretical commission cost when backtesting any script.

### Alerts and Monthly Performance Table

This strategy also incorporates alerts and a Monthly Performance Table. 

For the alerts: 
- Click on Alert menu in trading view and in the conditions dropdown select "Ichimoku Kinko Hyo Momentum Strategy". 
- Then select "alert() functions only.
- For expiration, just make sure that it is set in far future date. 
- In the Notifications tab, select at least Email and Push notifications
- Alerts Documentation: https://www.tradingview.com/chart/?solution=43000597494


For the Monthly Performance Table:

This script code adds a Monthly Strategy Performance Table so you can see a month-by-month and year-by-year breakdown of your P&L as a percentage of your account balance.

The table is based on **realized equity** rather than open equity, so it only updates the metrics **when a trade is closed**.

That's why some numbers will not match the Strategy Tester metrics (such as max drawdown), as the Strategy Tester bases metrics like max drawdown on open trade equity and not realized equity (closed trades).

The TradingView Strategy Tester is severely limited in some important ways. And unless you use complex Excel formulas on exported test data, you can't see a granular perspective of your system's historical performance.

There is much more to creating profitable and tradeable systems than developing a strategy with a good win rate and a good return with a reasonable drawdown.

Some additional questions we need to ask ourselves are:

- What did the system's worst drawdown look like?
- How long did it last?
- How often do drawdowns occur, and how quickly are they typically recovered?
- How often do we have a break-even or losing month or year?
- What is our expected compounded annual growth rate, and how does that growth rate compare to our max drawdown?

And many more questions that are too long to list and take a lifetime of trading experience to answer.

Without answering these kinds of questions, we run the risk of developing systems that look good on paper, but when it comes to live trading, we are uncomfortable or incapable of enduring the system's granular characteristics.

This Monthly Performance Table script code is intended to help bridge some of that gap with the Strategy Tester's limited default performance data.
