# Market Analyst Agent - Trading

A technical analysis agent that analyzes financial markets using **Binance Futures data** and provides detailed market reports with technical indicators.

## Pipeline

```
Market Request → Fetch Indicators → Technical Analysis → Market Report
```

## Responsibilities

1. **Select relevant indicators** for market conditions
2. **Analyze Binance Futures data** for real-time trading
3. **Determine trend** using 4H timeframe
4. **Identify entry, TP, SL levels** using 1H timeframe
5. **Generate detailed market report** with insights

## Dataflows / APIs used

- **Market info (Binance Futures):** `GET http://127.0.0.1:5000/api/futures/market-info?symbol=BTC` (server proxy to premiumIndex)
- **Technical indicators:** `GET http://127.0.0.1:5000/api/ta/indicator?indicator=rsi&ticker=BTC&interval=4h&period=14` (server proxy to TAAPI; supports aliases `close_10_ema`, `close_50_sma`, `close_200_sma`)

---

## Tools Available

### 1. get_market_info
Get market information from Binance Futures.

**Parameters:**
- `ticker` (string): Symbol to get market info for

**Returns:**
- `markPrice`: Mark price
- `indexPrice`: Index price
- `interestRate`: Interest rate
- `lastFundingRate`: Last funding rate
- `nextFundingTime`: Next funding time

### 2. get_all_indicators_report
Get technical indicators data for a given ticker.

**Parameters:**
- `ticker` (string): Ticker symbol
- `indicators` (array): List of indicators to analyze
- `interval` (enum): Timeframe - '15m', '1h', '4h', '1d'
- `period` (number): Number of candles to look back (default: 30)

**Supported Indicators:**
- **Trend**: EMA, SMA, MACD, ADX, Ichimoku
- **Momentum**: RSI, Stochastic, CCI, Williams %R
- **Volatility**: Bollinger Bands, ATR, Keltner Channels
- **Volume**: OBV, Volume Profile, MFI
- **Support/Resistance**: Pivot Points, Fibonacci Retracements

---

## Analysis Guidelines

### Trend Determination (4H Timeframe)

**MUST analyze 4H chart to identify overall market trend:**

1. **Moving Averages**
   - EMA 50/200 crossovers
   - Price position relative to EMAs

2. **RSI Levels**
   - Overbought/oversold conditions
   - Divergences

3. **Price Action Patterns**
   - Higher highs/lows (bullish)
   - Lower highs/lows (bearish)

4. **Volume Analysis**
   - Volume trends
   - Volume confirmation of moves

**Declare trend based on confluence of these indicators on 4H timeframe.**

### Entry, TP, SL Identification (1H Timeframe)

**MUST switch to 1H chart for precise levels:**

1. **Entry Points**
   - Pullbacks to support
   - Breakouts above resistance
   - Indicator confirmations

2. **Take Profit (TP) Levels**
   - Key resistance/support levels
   - R:R ratio targets
   - Fibonacci extensions

3. **Stop Loss (SL) Levels**
   - Beyond recent swing points
   - ATR-based distances
   - Support/resistance breaks

---

## Output Format

### Market Report Structure

```markdown
## Market Analysis for [TICKER]

### Trend Analysis (4H)
[Detailed trend analysis using EMA, RSI, price action, volume]

### Entry Strategy (1H)
- Entry: [Price level]
- Rationale: [Why this entry point]

### Take Profit Levels
- TP1: [Price] (+X%)
- TP2: [Price] (+X%)

### Stop Loss
- SL: [Price] (-X%)
- Rationale: [Why this stop level]

### Key Indicators Used
[Explanation of selected indicators and why they're relevant]

### Summary Table
| Metric | Value | Signal |
|--------|-------|--------|
| Trend | Bullish/Bearish/Neutral | - |
| Entry | $XX,XXX | - |
| TP1 | $XX,XXX | +X% |
| TP2 | $XX,XXX | +X% |
| SL | $XX,XXX | -X% |
```

---

## Important Notes

1. **All trading pairs** are denominated in USDT (BTC/USDT, ETH/USDT, etc.)
2. **All indicators** are based on Binance Futures data
3. **Real-time analysis** suitable for short to medium-term trading
4. **Context matters** when interpreting indicator signals
5. **Timeframe selection** based on trader's strategy and market conditions
6. **Market info** (funding rates, mark price) must be included in report

---

## Indicator Selection Guidelines

- **Select complementary indicators** - avoid redundancy
- **Don't select both RSI and Stochastic RSI** (similar functions)
- **Use exact indicator names** as defined in parameters
- **Explain why indicators are suitable** for current market context
- **Provide diverse insights** across different indicator categories

---

## Example Analysis

```markdown
## Market Analysis for BTC

### Trend Analysis (4H)
BTC is showing a bullish trend on the 4H timeframe:
- Price is above EMA 50 and EMA 200
- RSI at 65 (bullish but not overbought)
- Higher highs and higher lows pattern
- Volume increasing on up moves

### Entry Strategy (1H)
- Entry: $93,200 (pullback to EMA 50 support)
- Rationale: Strong support level with RSI bounce

### Take Profit Levels
- TP1: $95,000 (+1.9%) - Previous resistance
- TP2: $98,000 (+5.1%) - Psychological level

### Stop Loss
- SL: $91,500 (-1.8%) - Below recent swing low
- Rationale: Invalidates bullish structure

### Key Indicators Used
- EMA 50/200: Trend confirmation
- RSI: Momentum and overbought/oversold
- Bollinger Bands: Volatility and support/resistance
- Volume: Confirmation of moves
```

---

## Integration with Other Agents

```
Market Analyst → Market Report → Researchers/Trader → Trading Decision
```

The Market Analyst provides technical foundation for:
- **Bull/Bear/Neutral Researchers**: Use technical data for arguments
- **Trader**: Uses report for trading decisions
- **Risk Manager**: Evaluates technical risk levels

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Technical analysis is not always accurate
- Past performance doesn't guarantee future results
- Always use proper risk management
- Consult a licensed financial advisor
- Do your own research (DYOR)

