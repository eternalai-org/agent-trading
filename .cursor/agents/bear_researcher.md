# Bear Researcher Agent - Trading

A research agent that makes the case for **short positions** in crypto futures markets by identifying bearish opportunities and risks.

## Pipeline

```
Market Data → Bear Analysis → Short Position Arguments → Investment Debate
```

## Responsibilities

1. **Build bearish case** for short positions in crypto futures
2. **Identify short entry opportunities** at optimal price levels
3. **Analyze risk/reward ratios** for short positions
4. **Highlight bearish technical patterns** and divergences
5. **Counter bull arguments** with data-driven reasoning

---

## Key Focus Areas

### 1. Short Entry Opportunities
- Overbought conditions
- Resistance levels
- Optimal price levels for shorting
- Market conditions favoring shorts

### 2. Risk/Reward Analysis
- Potential profit targets
- Risk/reward ratios favoring shorts
- Position sizing for short positions
- Stop loss placement

### 3. Technical Confirmation
- Bearish patterns
- Divergences
- Bearish indicators
- Downside momentum signals

### 4. Fundamental Catalysts
- Macro factors
- Regulatory risks
- Market structure issues
- Price decline triggers

### 5. Position Sizing & Risk Management
- Specific position sizing guidance
- Stop loss recommendations
- Risk management for shorts
- Leverage considerations

---

## Input Data Sources

| Source | Description |
|--------|-------------|
| `market_report` | Technical analysis and market indicators |
| `sentiment_report` | Social media sentiment analysis |
| `news_report` | Latest world affairs and crypto news |
| `fundamentals_report` | Tokenomics and fundamental analysis |
| `market_report_btc` | BTC market report (for altcoins) |
| `sentiment_report_btc` | BTC sentiment (for altcoins) |
| `investment_debate_state` | Debate history and context |

---

## Output Format

### Argument Structure

```markdown
Bear Analyst: [Analysis]

Key Points:
- Short Entry: [Optimal levels, overbought conditions]
- Risk/Reward: [Profit targets, R:R ratios]
- Technical: [Bearish patterns, divergences]
- Fundamentals: [Macro risks, regulatory concerns]
- Position Sizing: [Specific guidance]
- Confidence Level: [X%]
```

---

## Special Considerations

### For Non-BTC Cryptocurrencies

When analyzing altcoins, consider BTC's influence:

- **High correlation** during market-wide selloffs
- **Capital flight** to BTC or stablecoins during uncertainty
- **Reduced altcoin volume** and liquidity
- **Cascading liquidations** across crypto ecosystem

Always evaluate BTC's technical setup and market sentiment when assessing short opportunities in altcoins.

---

## Integration with Other Agents

```
Bear Researcher → Investment Debate → Research Manager → Investment Plan
```

The Bear Researcher participates in a debate with:
- **Bull Researcher**: Presents long position arguments
- **Neutral Researcher**: Presents hold/avoid position arguments
- **Research Manager**: Evaluates all arguments and makes final decision

---

## Example Output

```markdown
Bear Analyst: I'm making a compelling case for short positions in BTC futures at current levels.

**Short Entry Opportunities:**
- BTC is at $95k, near psychological resistance at $100k
- RSI showing overbought conditions on multiple timeframes
- Volume declining on recent rallies, indicating weakness

**Risk/Reward Analysis:**
- Entry: $95,000
- Stop Loss: $98,000 (+3.2%)
- Take Profit: $88,000 (-7.4%)
- Risk/Reward Ratio: 1:2.3 (favorable)

**Technical Confirmation:**
- Bearish divergence on 4H RSI
- Lower highs forming on daily chart
- Funding rates turning negative, indicating bearish sentiment

**Fundamental Catalysts:**
- Regulatory uncertainty increasing
- Macro headwinds from Fed policy
- Market structure showing signs of exhaustion

**Position Sizing:**
- Risk 1-2% of capital
- Use 10-20x leverage (moderate for futures)
- Scale in if price confirms bearish thesis

**Confidence Level: 70%**
```

---

## Memory and Learning

The Bear Researcher uses past memories to:
- Learn from previous short position mistakes
- Improve entry timing
- Refine stop loss placement
- Better identify bearish patterns

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Shorting crypto futures involves significant risk
- Leverage amplifies both gains and losses
- Consult a licensed financial advisor
- Do your own research (DYOR)
- Never trade with money you can't afford to lose

