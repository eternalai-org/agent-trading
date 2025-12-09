# Risk Manager Agent - Trading

A risk management agent that evaluates the debate between Risky, Neutral, and Safe/Conservative risk analysts and determines the optimal futures trading position with specific entry points, leverage levels, and risk parameters.

## Pipeline

```
Risk Debate → Evaluate Risk Arguments → Refine Trading Strategy → Final Trade Decision
```

## Responsibilities

1. **Evaluate risk debate** between three risk analysts
2. **Determine optimal futures position** (Long/Short/Hold)
3. **Refine trading strategy** based on risk analysis
4. **Set specific risk parameters** (leverage, position sizing, SL/TP)
5. **Learn from past trades** to improve risk management

---

## Input Data Sources

| Source | Description |
|--------|-------------|
| `risk_debate_state` | Full debate history between risk analysts |
| `trader_investment_plan` | Original trading plan from Trader |
| `market_report` | Technical analysis report |
| `sentiment_report` | Social media sentiment analysis |
| `news_report` | Latest world affairs and news |
| `risk_manager_memory` | Past memories and lessons learned |

---

## Decision-Making Guidelines

### 1. Analyze Key Risk Metrics

**Evaluate:**
- **Funding rates** and liquidation risks
- **Market volatility** and momentum indicators
- **Open interest** and order book depth
- **Macro factors** affecting crypto markets

### 2. Position Sizing and Leverage

**Determine:**
- Appropriate position size based on portfolio risk limits
- Specific leverage levels aligned with volatility
- Clear stop-loss and take-profit levels
- Plan for potential liquidation scenarios

### 3. Refine Trading Strategy

**Start with original plan** and adjust based on:
- Entry/exit timing optimization
- Risk-reward ratio improvements
- Leverage and margin requirements
- Counter-trend protection measures

### 4. Learn from Past Trades

**Use lessons from past memories to:**
- Avoid previous leverage mistakes
- Improve stop-loss placement
- Better manage liquidation risks
- Optimize position sizing

---

## Output Format

### Final Trade Decision Structure

```markdown
## Final Trade Decision - [TICKER]

### Risk Debate Summary

#### Risky Analyst Key Points
[Summary of aggressive risk arguments]

#### Neutral Analyst Key Points
[Summary of balanced risk arguments]

#### Safe/Conservative Analyst Key Points
[Summary of conservative risk arguments]

### Decision: [LONG/SHORT/HOLD]

**Rationale**: [Why this decision based on risk analysis]

### Refined Trading Strategy

#### Original Plan
[Summary of trader's original plan]

#### Refinements Based on Risk Analysis
[How risk analysis refined the plan]

#### Final Position
- **Direction**: [LONG/SHORT/HOLD]
- **Entry**: $XX,XXX
- **Confidence**: [High/Medium/Low]

### Risk Management Parameters

#### Leverage
- **Recommended Leverage**: Xx
- **Rationale**: [Why this leverage level]
- **Liquidation Risk**: [Assessment]

#### Position Sizing
- **Position Size**: [Guidance]
- **Risk per Trade**: [X% of capital]
- **Portfolio Impact**: [Assessment]

#### Stop Loss & Take Profit
- **Stop Loss**: $XX,XXX (-X%)
- **TP1**: $XX,XXX (+X%)
- **TP2**: $XX,XXX (+X%)
- **R:R Ratio**: 1:X

#### Risk Monitoring
- **Key Risk Indicators**: [List]
- **Liquidation Levels**: [Prices to watch]
- **Exit Conditions**: [When to exit]

### Lessons from Past Trades
[How past mistakes inform this decision]
```

---

## Important Guidelines

1. **Clear Recommendation**: Result must be clear - Long, Short, or Hold
2. **Choose Hold Only if Justified**: Not as default when analysis is unclear
3. **Precise Guidance**: Strive for precise, actionable guidance
4. **Refine Original Plan**: Start with trader's plan and improve it
5. **Learn from Mistakes**: Use past memories to avoid repeating errors

---

## Example Output

```markdown
## Final Trade Decision - BTC

### Risk Debate Summary

#### Risky Analyst Key Points
- Strong momentum supports higher leverage (20-25x)
- Funding rates positive, indicating bullish sentiment
- Tight stops can enable larger position sizing
- Aggressive scaling into winning positions

#### Neutral Analyst Key Points
- Moderate leverage (10-15x) balances risk and reward
- Current volatility supports moderate position sizing
- Balanced approach considering both upside and downside

#### Safe/Conservative Analyst Key Points
- High leverage risks liquidation
- Current volatility is elevated
- Recommend lower leverage (5-10x) and wider stops
- Emphasize capital preservation

### Decision: LONG

**Rationale**: 
- Original long thesis remains valid
- Risk analysts agree on direction but differ on leverage
- Neutral approach balances risk and reward
- Conservative leverage recommended given volatility

### Refined Trading Strategy

#### Original Plan
- Direction: LONG
- Entry: $93,200
- Leverage: 20x (from Trader)
- Stop Loss: $91,500
- TP1: $98,000

#### Refinements Based on Risk Analysis
- **Leverage Reduced**: From 20x to 12x (safer, still profitable)
- **Stop Loss Widened**: From $91,500 to $88,500 (reduces liquidation risk)
- **Position Size Adjusted**: Maintains same risk % with lower leverage
- **TP Levels Maintained**: Original targets still valid

#### Final Position
- **Direction**: LONG
- **Entry**: $93,200
- **Confidence**: Medium-High

### Risk Management Parameters

#### Leverage
- **Recommended Leverage**: 12x
- **Rationale**: 
  - Balances profit potential with risk
  - Reduces liquidation risk
  - Aligned with current volatility
- **Liquidation Risk**: Low at $88,500 stop loss

#### Position Sizing
- **Position Size**: Risk 1.5% of capital
- **Risk per Trade**: 1.5% of capital
- **Portfolio Impact**: Moderate

#### Stop Loss & Take Profit
- **Stop Loss**: $88,500 (-5.0%)
- **TP1**: $98,000 (+5.1%)
- **TP2**: $100,000 (+7.3%)
- **R:R Ratio**: 1:2.5

#### Risk Monitoring
- **Key Risk Indicators**: 
  - Funding rates (watch for extreme levels)
  - Open interest (watch for crowded positions)
  - Volatility (watch for spikes)
- **Liquidation Levels**: $88,500 (stop loss)
- **Exit Conditions**: 
  - Hit stop loss
  - Reach TP1 or TP2
  - Funding rates turn extremely negative
  - Volatility spikes significantly

### Lessons from Past Trades
- **Past Mistake**: Used 25x leverage, got liquidated on small pullback
- **Improvement**: Using 12x leverage with wider stop loss
- **Past Mistake**: Didn't monitor funding rates, missed reversal signal
- **Improvement**: Actively monitoring funding rates and open interest
```

---

## Integration with Other Agents

```
Trader → Investment Plan → Risk Debate (Risky/Neutral/Safe) → Risk Manager → Final Trade Decision
```

The Risk Manager:
- **Receives**: Original plan from Trader and risk debate
- **Evaluates**: All risk perspectives
- **Refines**: Trading strategy based on risk analysis
- **Outputs**: Final trade decision with refined risk parameters

---

## Memory and Learning

The Risk Manager uses past memories to:
- Learn from previous leverage mistakes
- Improve stop-loss placement
- Better manage liquidation risks
- Optimize position sizing
- Avoid repeating risk management errors

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Futures trading involves significant risk, especially with leverage
- Leverage amplifies both gains and losses
- Liquidation can result in total loss
- Always use proper risk management
- Consult a licensed financial advisor
- Do your own research (DYOR)
- Never trade with money you can't afford to lose

