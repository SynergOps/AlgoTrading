# Lorentzian Classification: Background

When using Machine Learning algorithms like K-Nearest Neighbors, choosing an appropriate distance metric is essential. Euclidean Distance is often used as the default, but it may not always be the best choice for financial market data. This is because market data is significantly impacted by proximity to major world events (e.g., FOMC Meetings, Black Swan events), which can warp the "Price-Time" continuum, similar to gravitational warping in Space-Time.

To better account for this warping effect, Lorentzian Distance can be used as an alternative metric. The geometry of Lorentzian Space can be difficult to visualize, so an example with two features (RSI and ADX) is provided below. In practice, 3-8 features are optimal, but for simplicity, only 2 are shown here.

**Fundamental Assumptions:**
1. RSI and ADX can be calculated for a given chart.
2. For simplicity, RSI and ADX values are assumed to follow a Gaussian distribution in the range 0-100.
3. The most recent RSI and ADX value is considered the origin of a coordinate system (ADX on x-axis, RSI on y-axis).

---

## Distances in Euclidean Space
Measuring Euclidean Distances of historical values with the most recent point at the origin yields a distribution like:

```
                       [RSI]
                         |                      
                         |                   
                         |                 
                     ...:::....              
               .:.:::••••••:::•::..             
             .:•:.:•••::::••::••....::.            
            ....:••••:••••••••::••:...:•.          
           ...:.::::::•••:::•••:•••::.:•..          
           ::•:.:•:•••••••:.:•::::::...:..         
 |--------.:•••..•••••••:••:...:::•:•:..:..----------[ADX]    
 0        :•:....:•••••::.:::•••::••:.....            
          ::....:.:••••••••:•••::••::..:.          
           .:...:••:::••••••••::•••....:          
             ::....:.....:•::•••:::::..             
               ..:..::••..::::..:•:..              
                   .::..:::.....:                
                         |            
                         |                   
                         |
                         |
                        _|_ 0        
```
*Figure 1: Neighborhood in Euclidean Space*

---

## Distances in Lorentzian Space
Measuring the same set of historical values using Lorentzian Distance yields a different distribution:

```
                        [RSI] 
 ::..                     |                    ..:::  
  .....                   |                  ......
   .••••::.               |               :••••••. 
    .:•••••:.             |            :::••••••.  
      .•••••:...          |         .::.••••••.    
        .::•••••::..      |       :..••••••..      
           .:•••••••::.........::••••••:..         
             ..::::••••.•••••••.•••••••:.            
               ...:•••••••.•••••••••::.              
                 .:..••.••••••.••••..                
 |---------------.:•••••••••••••••••.---------------[ADX]          
 0             .:•:•••.••••••.•••••••.                
             .••••••••••••••••••••••••:.            
           .:••••••••••::..::.::••••••••:.          
         .::••••••::.     |       .::•••:::.       
        .:••••••..        |          :••••••••.     
      .:••••:...          |           ..•••••••:.   
    ..:••::..             |              :.•••••••.   
   .:•....                |               ...::.:••.  
  ...:..                  |                   :...:••.     
 :::.                     |                       ..::  
                        _|_ 0
```
*Figure 2: Neighborhood in Lorentzian Space*

---

### Observations
1. In Lorentzian Space, the shortest distance between two points is not necessarily a straight line, but a geodesic curve.
2. The warping effect of Lorentzian distance reduces the overall influence of outliers and noise.
3. Lorentzian Distance becomes increasingly different from Euclidean Distance as the number of nearest neighbors used for comparison increases.

---

## Backtesting

This repository includes a backtesting adapter (`backtesting stream.pine`) that allows you to test the Lorentzian Classification strategy with historical data.

### Setup Instructions

1. **Load the Main Indicator**: First, add the main Lorentzian Classification indicator (`ML-lorentzian-classification.pine`) to your chart.

2. **Configure Source Selection**: In the backtesting adapter, select the source from the dropdown menu and choose **"Lorentzian Clas. Backtest Stream"** to connect it with the main indicator signals.

3. **Adjust Backtest Start Date**: When setting the backtest start date, ensure you account for the **Max bars to lookback** parameter of the main Lorentzian Classification indicator. The backtest start date should be set sufficiently far from the beginning of your data to allow the indicator to gather enough historical data points for accurate classification.

   **Important**: If your main indicator uses a lookback period of 500 bars, ensure your backtest start date is at least 500+ bars after the beginning of your dataset to avoid inaccurate results during the initial period.

4. **Signal Mapping**: The backtesting adapter interprets the following signal values:
   - `1`: Start Long Trade
   - `2`: End Long Trade  
   - `-1`: Start Short Trade
   - `-2`: End Short Trade

### Backtest Parameters
- Initial Capital: $1,000
- Position Size: 10% of equity per trade
- Commission: 0.05%
- No pyramiding allowed
- Margin requirements: 10x leverage for both long and short positions

---
- Original Author: https://www.tradingview.com/u/jdehorty/
- License: Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
- Youtube Video: https://www.youtube.com/watch?v=AdINVvnJfX4