## Ichimoku TK Cross Strategy

__version 1.2.0__

This strategy is developed for swing trading on BTC spot accounts. Thus, use it only for buying and holding it until the exit signal tells you to sell your entire position.


Long only Position:

- Buy at the next candle after Tenkan/Kijun-sen bullish cross happens
- Sell at the next candle after Tenkan/Kijun-sen bearish cross occurs.
- Re-buy if you get Tenkan/Kijun-sen bullish cross again and Sell your holding when Tenkan/Kijun-sen bearish cross occurs.


__NOTE:__ This strategy is only for daily timeframe. The exit signals refer to the entire position.
This strategy incorporates alerts. Click on Alert menu in trading view and in the conditions dropdown select "Ichimoku Kinko Hyo: TK Cross Strategy (9, 26, 52, 26, 26)". Then select "alert() functions only. For expiration, just make sure that it is set in far future date. In the Notifications tab, select at least Email and Push notifications
Alert Documentation: https://www.tradingview.com/chart/?solution=43000597494

This strategy also incorporates alerts and a Monthly Performance Table. 

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
