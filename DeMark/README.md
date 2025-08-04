# DeMark Pivot Points Strategy

## Overview
This Pine Script strategy implements a complete trading system based on Tom DeMark's pivot point methodology. The strategy focuses exclusively on daily DeMark pivots with bias-based signal detection and automated risk management.

## Key Features

### **DeMark-Specific Implementation**
- Uses Thomas DeMark's specialized pivot calculation method
- Fixed to daily timeframe pivots only
- Displays 3 core levels: Pivot Point (P), Support 1 (S1), and Resistance 1 (R1)

### **Bias Detection System**
- **Bullish Bias**: Current PP > Previous PP
- **Bearish Bias**: Current PP < Previous PP
- **Signal Filtering**: Only shows signals that align with the current bias direction

### 💹 **Trading Strategy Logic**

#### Entry Conditions
- **Entry Location**: Always at the Pivot Point (P) price level using limit orders
- **Long Entry**: Bullish bias + price touches P line + no existing position + no trade executed today
- **Short Entry**: Bearish bias + price touches P line + no existing position + no trade executed today

#### Risk Management
- **Position Sizing**: Based on configurable risk percentage (default: 2% of equity)
- **Stop Loss**: 
  - Long positions: Stop at S1 level
  - Short positions: Stop at R1 level
- **Take Profit**:
  - Long positions: Target at R1 level  
  - Short positions: Target at S1 level

#### Trade Frequency Control
- **One Trade Per Pivot Day**: Prevents multiple entries on the same daily pivot period
- **Fresh Start**: Trade flag resets with each new daily pivot calculation

### 🔧 **Technical Implementation**

#### Cross-Timeframe Compatibility
- Works on intraday charts (4H, 1H, etc.) while using daily pivot calculations
- Proper timeframe change detection using `timeframe.change("1D")`
- Handles both daily-based and intraday pivot calculations

#### Signal Detection
- Price crossing logic: Detects when close crosses above/below PP
- Bias alignment: Only triggers signals when price movement aligns with bias
- Touch detection: Entries occur when price touches P line (high >= P >= low)

#### Debug Features
- Optional debug indicators for troubleshooting
- Real-time bias status display
- Previous/current PP value tracking
- Cross detection validation

## Usage Instructions

1. **Apply to Chart**: Add the strategy to any timeframe chart (recommended: 4H)
2. **Configure Risk**: Set your desired risk percentage per trade
3. **Enable Strategy**: Toggle "Enable Strategy Trading" to start automated trading
4. **Monitor Signals**: Watch for bias-aligned triangle signals
5. **Review Performance**: Use Pine Script's strategy tester for backtesting results

## Strategy Logic Flow

```
1. Daily pivot calculation (P, S1, R1)
2. Bias determination (current PP vs previous PP)
3. Price monitoring for P line touches
4. Entry signal generation (bias + touch + no existing trade)
5. Limit order placement at P price
6. Automatic stop/target placement
7. Trade completion and daily flag reset
```

## Risk Disclaimer

This strategy is for educational and backtesting purposes. Past performance does not guarantee future results. Always test thoroughly before using real capital and consider your risk tolerance.

## Version Information
- **Pine Script**: Version 6
- **Strategy Type**: Overlay with automated entry/exit
- **Calculation**: Based on Tom DeMark's pivot methodology

---
*© SynergOps - Mozilla Public License 2.0*
