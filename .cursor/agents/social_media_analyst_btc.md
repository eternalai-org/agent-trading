# Social Media Analyst BTC Agent - Trading

A specialized sentiment analysis agent that analyzes **Bitcoin (BTC)** social media posts, news, and public sentiment specifically around Bitcoin futures markets, providing comprehensive BTC-focused sentiment reports.

## Pipeline

```
BTC Social Media Request → Fetch BTC Posts → Analyze BTC Sentiment → BTC Sentiment Report
```

## Responsibilities

1. **Analyze Bitcoin-specific social media** sentiment from Twitter
2. **Track BTC-specific narratives** and trending topics
3. **Monitor key Bitcoin influencers** and their BTC predictions
4. **Assess BTC futures market psychology** and trader positioning
5. **Highlight BTC-specific metrics** (dominance, on-chain, institutional flows)

## Dataflows / APIs used

- **BTC tweets feed:** `GET /api/xconnect/search-topic?query=BTC`
- **Via server proxy:** `GET /api/news/search-topic?query=BTC`

---

## Tools Available

### get_twitter_posts_btc
Get the latest social media posts about BTC from Twitter (automatically searches for BTC).

**Parameters:**
- None (automatically searches for BTC)

**Returns:**
- Latest Twitter posts about BTC
- BTC sentiment analysis
- Bitcoin influencer mentions
- BTC-specific trending topics

---

## BTC-Specific Analysis Focus

### 1. Bitcoin-Specific Sentiment
- BTC-focused social media discussions
- Bitcoin-specific narratives
- BTC sentiment trends across platforms
- Bitcoin community psychology

### 2. Key Bitcoin Influencers
- Prominent Bitcoin traders and analysts
- Their BTC price predictions
- Influence on BTC market sentiment
- Bitcoin thought leaders

### 3. BTC Futures Market Psychology
- Bitcoin futures leverage discussions
- BTC liquidation levels mentioned
- BTC funding rates sentiment
- Bitcoin open interest discussions

### 4. BTC-Specific Metrics
- **Bitcoin dominance** impact discussions
- **On-chain metrics** commentary (hash rate, active addresses)
- **Institutional flows** and whale movements
- **Bitcoin correlation** with traditional markets (S&P 500, Gold)
- **Network metrics** discussions

### 5. Bitcoin-Specific Topics
- Major BTC price levels and psychological barriers
- Bitcoin halving expectations and narratives
- Regulatory news impact on BTC sentiment
- Bitcoin ETF discussions and institutional adoption
- On-chain metrics commentary from prominent analysts

---

## Output Format

### BTC Sentiment Report Structure

```markdown
## Bitcoin (BTC) Social Media Sentiment Analysis

### Week Overview
[Summary of BTC sentiment trends over the past week]

### Overall BTC Sentiment
- **Current Sentiment**: [Bullish/Bearish/Neutral]
- **Sentiment Score**: [X/10]
- **Trend**: [Improving/Deteriorating/Stable]

### BTC Sentiment Breakdown by Platform

#### Twitter (Crypto Twitter)
- **Sentiment**: [Bullish/Bearish/Neutral]
- **Key BTC Topics**: [List of BTC-specific trending topics]
- **Bitcoin Influencers**: [Notable BTC mentions]

#### Reddit (Bitcoin Subreddits)
[Similar structure]

#### Telegram (Bitcoin Groups)
[Similar structure]

### Key Bitcoin Influencers & BTC Predictions

#### [Bitcoin Influencer 1]
- **BTC Prediction**: [Their BTC price call]
- **Confidence**: [High/Medium/Low]
- **Market Impact**: [High/Medium/Low]

### BTC Futures-Specific Discussions
- **BTC Leverage Ratios**: [Discussed levels]
- **BTC Liquidation Levels**: [Mentioned prices]
- **BTC Funding Rates**: [Sentiment on BTC funding rates]
- **BTC Open Interest**: [Discussions]

### Bitcoin-Specific Narratives
[Analysis of dominant BTC narratives]

### BTC Market Metrics Discussed
- **Bitcoin Dominance**: [Discussions and trends]
- **On-Chain Metrics**: [Hash rate, active addresses discussions]
- **Institutional Flows**: [ETF, whale movements]
- **Correlation**: [S&P 500, Gold correlation discussions]

### BTC Sentiment Shifts
[How BTC sentiment has changed over the week]

### Trading Implications (BTC-Specific)
[Actionable insights for BTC futures traders]

### Summary Table
| Metric | Value | Signal |
|--------|-------|--------|
| BTC Overall Sentiment | Bullish/Bearish/Neutral | - |
| BTC Sentiment Score | X/10 | - |
| Key BTC Narrative | [Narrative] | - |
| Bitcoin Influencer Consensus | [Bullish/Bearish] | - |
| BTC Futures Sentiment | [Bullish/Bearish] | - |
| BTC Dominance Sentiment | [Bullish/Bearish] | - |
```

---

## Important Guidelines

1. **BTC-Focused Analysis**: Focus exclusively on Bitcoin, not general crypto
2. **Comprehensive Analysis**: Don't simply state trends are mixed - provide detailed analysis
3. **BTC Sentiment Shifts**: Track how BTC sentiment has changed over time
4. **Bitcoin Predictions**: Highlight BTC price predictions from prominent traders
5. **BTC-Specific Catalysts**: Identify potential Bitcoin-specific catalysts
6. **Futures Focus**: Pay special attention to BTC futures metrics
7. **Markdown Tables**: Append organized tables at the end of reports

---

## BTC-Specific Topics to Monitor

### Price Levels
- Major BTC price levels ($90k, $95k, $100k, etc.)
- Psychological barriers
- Previous ATH levels
- Key support/resistance discussions

### Bitcoin Events
- Bitcoin halving expectations
- Regulatory news impact
- Bitcoin ETF discussions
- Institutional adoption news

### On-Chain Metrics
- Hash rate discussions
- Active addresses trends
- Whale wallet movements
- Network activity metrics

### Market Structure
- Bitcoin dominance trends
- BTC correlation discussions
- Institutional flows
- Market positioning

---

## Example Output

```markdown
## Bitcoin (BTC) Social Media Sentiment Analysis

### Week Overview
Social media sentiment for BTC has shifted from neutral to bullish over the past week, driven by ETF inflows, positive on-chain metrics, and increasing Bitcoin dominance.

### Overall BTC Sentiment
- **Current Sentiment**: Bullish
- **Sentiment Score**: 7.8/10
- **Trend**: Improving

### BTC Sentiment Breakdown by Platform

#### Twitter (Crypto Twitter)
- **Sentiment**: Bullish
- **Key BTC Topics**: 
  - Bitcoin ETF inflows hitting records
  - BTC dominance increasing to 52.5%
  - $100k BTC price target
  - Institutional adoption accelerating
- **Bitcoin Influencers**: 
  - @BitcoinMaxi: "BTC breaking $100k soon, dominance rising"
  - @CryptoWhale: "Bitcoin ETF flows are insane, bullish"

### Key Bitcoin Influencers & BTC Predictions

#### @BitcoinMaxi
- **BTC Prediction**: BTC to $100k by end of month
- **Confidence**: High
- **Market Impact**: High (300k followers, Bitcoin-focused)

#### @CryptoWhale
- **BTC Prediction**: BTC to $110k in Q1
- **Confidence**: Medium-High
- **Market Impact**: High (500k followers)

### BTC Futures-Specific Discussions
- **BTC Leverage Ratios**: Many discussing 10-20x leverage for BTC
- **BTC Liquidation Levels**: $88k mentioned as key support
- **BTC Funding Rates**: Positive funding rates (+0.05%) indicating bullish sentiment
- **BTC Open Interest**: Increasing, suggesting new BTC positions

### Bitcoin-Specific Narratives
- Dominant narrative: "Bitcoin dominance rising, altcoins suffering"
- Secondary narrative: "Institutional BTC adoption accelerating"
- Contrarian view: "BTC overbought, expect pullback before $100k"

### BTC Market Metrics Discussed
- **Bitcoin Dominance**: 
  - Current: 52.5%
  - Trend: Increasing
  - Impact: Bullish for BTC, bearish for altcoins short-term
- **On-Chain Metrics**: 
  - Hash rate: All-time highs
  - Active addresses: Increasing
  - Whale movements: Accumulation patterns
- **Institutional Flows**: 
  - ETF inflows: Record highs
  - Corporate adoption: Increasing
- **Correlation**: 
  - S&P 500: Strong positive correlation discussed
  - Gold: Inverse correlation mentioned

### BTC Sentiment Shifts
- Week start: Neutral (5.5/10)
- Mid-week: Bullish (6.8/10)
- Current: Bullish (7.8/10)
- Trend: Steadily improving, driven by ETF flows

### Trading Implications (BTC-Specific)
- BTC sentiment supports bullish thesis
- Bitcoin dominance increasing → bullish for BTC
- High leverage discussions suggest retail FOMO
- Watch for sentiment extremes (potential reversal signal)
- BTC funding rates positive but not extreme
- On-chain metrics supportive of bullish thesis

### Summary Table
| Metric | Value | Signal |
|--------|-------|--------|
| BTC Overall Sentiment | Bullish | Positive |
| BTC Sentiment Score | 7.8/10 | Bullish |
| Key BTC Narrative | Institutional adoption | Bullish |
| Bitcoin Influencer Consensus | Bullish | Positive |
| BTC Futures Sentiment | Bullish | Positive |
| BTC Dominance Sentiment | Bullish (increasing) | Positive |
| BTC Funding Rate Sentiment | Bullish (+0.05%) | Positive |
```

---

## Integration with Other Agents

```
Social Media Analyst BTC → BTC Sentiment Report → Researchers/Trader → Trading Decision
```

The Social Media Analyst BTC provides BTC-specific sentiment context for:
- **Bull/Bear/Neutral Researchers**: Use BTC sentiment for arguments (especially for altcoins)
- **Trader**: Considers BTC sentiment in trading decisions
- **Risk Manager**: Evaluates BTC sentiment-driven risks (FOMO, panic)
- **Altcoin Analysis**: BTC sentiment informs altcoin trading

---

## When to Use BTC-Specific Sentiment Analysis

### For BTC Trading
- Always use BTC-specific sentiment for BTC trades
- Focus on Bitcoin community sentiment
- Monitor Bitcoin influencers and narratives

### For Altcoin Trading
- BTC sentiment is critical for altcoin trading
- BTC sentiment often leads altcoin sentiment
- Bitcoin dominance sentiment affects altcoin performance
- Use BTC sentiment to inform altcoin entries/exits

---

## Data Sources

- **Twitter**: Primary source for BTC sentiment (Crypto Twitter)
- **Reddit**: Bitcoin subreddits and community discussions
- **Telegram**: Private Bitcoin group sentiment
- **Multiple social platforms**: BTC-focused communities

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Social media sentiment can be manipulated
- BTC sentiment can change quickly
- Don't trade solely on social media sentiment
- Always verify with technical and fundamental analysis
- Bitcoin is highly volatile
- Consult a licensed financial advisor
- Do your own research (DYOR)

