# Trader Agent - Trading Decisions

A crypto futures trading agent that analyzes comprehensive market data and makes leveraged trading decisions based on investment plans from research teams.

## Pipeline

```
Investment Plan → Trader Analysis → Trading Decision → Final Transaction Proposal
```

## Responsibilities

1. **Receive investment plan** from research manager/team
2. **Analyze comprehensive market data** (technical, sentiment, news, fundamentals)
3. **Make leveraged trading decisions** for futures positions
4. **Provide specific recommendations** (entry, leverage, SL, TP)
5. **Learn from past mistakes** using memory system

---

## Input Data Sources

| Source | Description |
|--------|-------------|
| `investment_plan` | Investment plan from research manager/team |
| `market_report` | Technical analysis report |
| `sentiment_report` | Social media sentiment analysis |
| `news_report` | Latest world affairs and news |
| `fundamentals_report` | Tokenomics and fundamental analysis |
| `trader_memory` | Past memories and lessons learned |

---

## Analysis Process

### Step 1: Receive Investment Plan

The Trader receives a comprehensive investment plan that incorporates:
- Current technical market trends
- Macroeconomic indicators
- Funding rates
- Open interest
- Social media sentiment

### Step 2: Analyze Market Context

**Current Situation Analysis:**
```
Current Situation = Market Report + Sentiment Report + News Report + Fundamentals Report
```

**Past Memories:**
- Retrieve similar past situations
- Learn from previous mistakes
- Apply lessons learned

### Step 3: Make Trading Decision

**Considerations:**
- Both long and short positions
- Leverage levels (10x-50x)
- Volatility and risk management
- Liquidation risks
- Position sizing

### Step 4: Provide Final Recommendation

**Must conclude with:**
```
FINAL TRANSACTION PROPOSAL: **LONG/SHORT/HOLD** <leverage>x
```

---

## Output Format

### Trading Decision Structure

```markdown
## Trading Decision - [TICKER]

### Market Analysis Summary
[Summary of market conditions based on all reports]

### Investment Plan Review
[Review of the proposed investment plan]

### Trading Recommendation

#### Position
- **Direction**: LONG/SHORT/HOLD
- **Entry Price**: $XX,XXX
- **Leverage**: Xx (10x-50x)
- **Confidence**: [High/Medium/Low]

#### Risk Management
- **Stop Loss**: $XX,XXX (-X%)
- **Take Profit 1**: $XX,XXX (+X%)
- **Take Profit 2**: $XX,XXX (+X%)
- **Position Sizing**: [Guidance]

#### Rationale
[Why this decision based on analysis]

### Lessons from Past Trades
[How past mistakes inform this decision]

### FINAL TRANSACTION PROPOSAL: **LONG/SHORT/HOLD** <leverage>x
```

---

## Key Features

### 1. Leveraged Trading Focus
- Focuses on **crypto futures trading**
- Considers **leverage levels** (10x-50x)
- Emphasizes **liquidation risk management**
- Provides **position sizing guidance**

### 2. Comprehensive Analysis
- Uses **all available market data**
- Combines technical, sentiment, news, fundamentals
- Considers **volatility** in decision-making
- Evaluates **risk/reward ratios**

### 3. Learning from Mistakes
- Uses **past memories** to avoid repeating errors
- Applies **lessons learned** from similar situations
- Improves decision quality over time
- Refines risk management based on experience

### 4. Clear Decision Making
- Provides **firm decisions** (not wishy-washy)
- Includes **specific entry, SL, TP levels**
- Recommends **leverage levels**
- Concludes with **clear transaction proposal**

---

## Important Guidelines

1. **Futures Trading Focus**: All recommendations are for crypto futures trading
2. **Leverage Consideration**: Always consider appropriate leverage (10x-50x)
3. **Risk Management**: Pay special attention to volatility and liquidation risks
4. **Learn from Past**: Utilize lessons from past decisions
5. **Clear Conclusion**: Always end with FINAL TRANSACTION PROPOSAL format
6. **Position Sizing**: Consider liquidation risks and appropriate position sizing

---

## Example Output

```markdown
## Trading Decision - BTC

### Market Analysis Summary
Based on comprehensive analysis:
- Technical analysis shows bullish trend on 4H timeframe
- Social media sentiment is bullish (7.5/10)
- News flow is positive (ETF inflows, regulatory clarity)
- Fundamentals are strong (network growth, adoption)

### Investment Plan Review
The investment plan recommends LONG position with:
- Entry: $93,200
- Target: $98,000-$100,000
- Rationale: Strong technical setup, positive sentiment, favorable fundamentals

### Trading Recommendation

#### Position
- **Direction**: LONG
- **Entry Price**: $93,200
- **Leverage**: 15x
- **Confidence**: Medium-High

#### Risk Management
- **Stop Loss**: $88,500 (-5.0%)
- **Take Profit 1**: $98,000 (+5.1%)
- **Take Profit 2**: $100,000 (+7.3%)
- **Position Sizing**: Risk 1.5% of capital

#### Rationale
- Strong technical momentum supports long position
- Positive sentiment and news flow confirm bullish thesis
- Funding rates are positive but not extreme
- Leverage of 15x balances profit potential with risk
- Stop loss placed below key support to avoid liquidation on normal volatility

### Lessons from Past Trades
- Past mistake: Used 25x leverage, got liquidated on small pullback
- Improvement: Using 15x leverage with wider stop loss
- Past mistake: Didn't respect stop loss, held losing position
- Improvement: Strict stop loss at $88,500, no exceptions

### FINAL TRANSACTION PROPOSAL: **LONG** 15x
```

---

## Integration with Other Agents

```
Research Manager → Investment Plan → Trader → Trading Decision → Risk Manager
```

The Trader:
- **Receives**: Investment plan from Research Manager
- **Analyzes**: All market data (technical, sentiment, news, fundamentals)
- **Decides**: Long/Short/Hold with leverage recommendation
- **Outputs**: Trading decision for Risk Manager to refine

---

## Memory and Learning

The Trader uses past memories to:
- Learn from previous trading mistakes
- Avoid repeating errors
- Improve leverage decisions
- Refine stop loss placement
- Better assess risk/reward ratios
- Improve position sizing

---

## Leverage Guidelines

### Leverage Levels (10x-50x)

| Leverage | Risk Level | Use Case |
|----------|------------|----------|
| 10-15x | Low-Medium | Conservative, strong trends |
| 15-25x | Medium | Moderate volatility, clear setups |
| 25-35x | Medium-High | High conviction, low volatility |
| 35-50x | High | Very high conviction, experienced traders |

### Leverage Considerations
- **Volatility**: Higher volatility = lower leverage
- **Trend Strength**: Stronger trend = can use higher leverage
- **Risk Tolerance**: Lower tolerance = lower leverage
- **Liquidation Risk**: Always consider liquidation distance

---

## Risk Management

### Stop Loss Placement
- Place below key support (longs) or above key resistance (shorts)
- Consider ATR for volatility-based stops
- Avoid tight stops in volatile markets
- Ensure liquidation distance is reasonable

### Position Sizing
- Risk 1-2% of capital per trade
- Adjust position size based on leverage
- Consider liquidation risk
- Maintain portfolio balance

### Take Profit Levels
- Set multiple TP levels
- Consider key resistance/support levels
- Use R:R ratios (minimum 1:2)
- Scale out of positions

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Futures trading with leverage involves extreme risk
- Leverage amplifies both gains and losses
- Liquidation can result in total loss
- Never trade with money you can't afford to lose
- Always use proper risk management
- Consult a licensed financial advisor
- Do your own research (DYOR)

