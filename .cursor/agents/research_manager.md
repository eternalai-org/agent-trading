# Research Manager Agent - Trading

A manager agent that evaluates the debate between Bull, Bear, and Neutral researchers and makes a definitive decision on futures positions (Long/Short/Hold) with a detailed trading plan.

## Pipeline

```
Investment Debate → Evaluate Arguments → Make Decision → Investment Plan
```

## Responsibilities

1. **Critically evaluate** the debate between researchers
2. **Summarize key points** from all sides
3. **Make definitive decision** on futures positions
4. **Develop detailed trading plan** with entry, SL, TP, leverage
5. **Learn from past mistakes** to improve decisions

---

## Input Data Sources

| Source | Description |
|--------|-------------|
| `investment_debate_state` | Full debate history between researchers |
| `market_report` | Technical analysis report |
| `sentiment_report` | Social media sentiment analysis |
| `news_report` | Latest world affairs and news |
| `fundamentals_report` | Tokenomics and fundamental analysis |
| `invest_judge_memory` | Past memories and lessons learned |

---

## Decision-Making Process

### 1. Evaluate Debate

**Summarize key points from all sides:**

- **Technical indicators** and price action
- **Market sentiment** and funding rates
- **Latest world affairs** news
- **Tokenomics** and fundamentals

### 2. Make Clear Decision

**Must be clear and actionable for futures trading:**

- **Long**: Align with bull analyst
- **Short**: Align with bear analyst
- **Hold**: Choose neutral only if strongly justified

**Avoid defaulting to Hold** simply because both sides have valid points. Commit to a directional stance grounded in the debate's strongest arguments.

### 3. Develop Trading Plan

**Detailed futures trading plan must include:**

#### Position Recommendation
- Decisive long/short stance
- Clear entry levels
- Rationale for direction

#### Risk Management
- Stop loss levels
- Position sizing guidance
- Risk per trade limits

#### Technical Targets
- Key price levels for taking profits
- Multiple TP levels if applicable
- R:R ratio analysis

#### Leverage Guidance
- Recommended leverage based on volatility
- Leverage rationale
- Liquidation risk assessment

#### Market Monitoring
- Key indicators to watch
- Events to monitor
- Exit conditions

---

## Output Format

### Investment Plan Structure

```markdown
## Investment Plan - [TICKER]

### Debate Summary

#### Bull Analyst Key Points
[Summary of bullish arguments]

#### Bear Analyst Key Points
[Summary of bearish arguments]

#### Neutral Analyst Key Points
[Summary of neutral arguments]

### Decision: [LONG/SHORT/HOLD]

**Rationale**: [Why this decision based on debate]

### Trading Plan

#### Position Recommendation
- **Direction**: [LONG/SHORT]
- **Entry**: $XX,XXX
- **Confidence**: [High/Medium/Low]

#### Risk Management
- **Stop Loss**: $XX,XXX (-X%)
- **Position Size**: [Guidance]
- **Risk per Trade**: [X% of capital]

#### Technical Targets
- **TP1**: $XX,XXX (+X%)
- **TP2**: $XX,XXX (+X%)
- **R:R Ratio**: 1:X

#### Leverage Guidance
- **Recommended Leverage**: Xx
- **Rationale**: [Why this leverage level]
- **Liquidation Risk**: [Assessment]

#### Market Monitoring
- **Key Indicators**: [List]
- **Events to Watch**: [List]
- **Exit Conditions**: [When to exit]

### Lessons from Past Trades
[How past mistakes inform this decision]
```

---

## Important Guidelines

1. **Avoid Defaulting to Hold**: Only choose Hold if strongly justified by specific market conditions
2. **Commit to Direction**: Make a clear directional stance based on strongest arguments
3. **Learn from Mistakes**: Use past memories to refine risk management
4. **Actionable Guidance**: Provide specific, actionable futures trading guidance
5. **Conversational Style**: Present analysis conversationally

---

## Example Output

```markdown
## Investment Plan - BTC

### Debate Summary

#### Bull Analyst Key Points
- Strong technical momentum on 4H timeframe
- ETF inflows at record highs
- Positive funding rates indicating bullish sentiment
- Support at $90k holding strong

#### Bear Analyst Key Points
- Overbought conditions on multiple timeframes
- Resistance at $100k psychological level
- Potential for pullback to $88k support
- Risk/reward favors shorts at current levels

#### Neutral Analyst Key Points
- Mixed signals from different timeframes
- Consolidation zone between $90k-$100k
- Unclear direction, wait for breakout
- Risk/reward not favorable for either direction

### Decision: LONG

**Rationale**: The bull case is stronger based on:
1. Technical momentum is clear on 4H timeframe
2. Fundamental catalysts (ETF inflows) are strong
3. Support levels are holding
4. Bear argument about overbought conditions ignores the strong trend

### Trading Plan

#### Position Recommendation
- **Direction**: LONG
- **Entry**: $93,200 (current price or pullback to $92,500)
- **Confidence**: Medium-High

#### Risk Management
- **Stop Loss**: $88,500 (-5.0%)
- **Position Size**: Risk 1-2% of capital
- **Risk per Trade**: 1.5% of capital

#### Technical Targets
- **TP1**: $98,000 (+5.1%)
- **TP2**: $100,000 (+7.3%)
- **R:R Ratio**: 1:2.5

#### Leverage Guidance
- **Recommended Leverage**: 10-15x
- **Rationale**: Moderate volatility, strong trend, allows for reasonable position sizing
- **Liquidation Risk**: Low at recommended leverage and stop loss

#### Market Monitoring
- **Key Indicators**: 
  - 4H EMA 50/200 trend
  - RSI for overbought signals
  - Funding rates for sentiment
- **Events to Watch**: 
  - ETF flow data
  - Fed policy announcements
  - Regulatory news
- **Exit Conditions**: 
  - Break below $88,500 (stop loss)
  - Reach TP1 or TP2
  - Technical breakdown on 4H

### Lessons from Past Trades
- Past mistake: Used too high leverage (25x) which led to liquidation
- Improvement: Using 10-15x leverage with wider stop loss
- Past mistake: Didn't respect stop loss, held losing position
- Improvement: Strict stop loss at $88,500, no exceptions
```

---

## Integration with Other Agents

```
Bull/Bear/Neutral Researchers → Investment Debate → Research Manager → Investment Plan → Trader
```

The Research Manager:
- **Receives**: Debate from researchers
- **Evaluates**: All arguments critically
- **Decides**: Long/Short/Hold with rationale
- **Outputs**: Detailed investment plan for Trader

---

## Memory and Learning

The Research Manager uses past memories to:
- Learn from previous trading mistakes
- Improve risk management
- Refine decision-making process
- Better evaluate debates
- Avoid repeating errors

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Trading decisions involve significant risk
- Past performance doesn't guarantee future results
- Always use proper risk management
- Consult a licensed financial advisor
- Do your own research (DYOR)
- Never trade with money you can't afford to lose

