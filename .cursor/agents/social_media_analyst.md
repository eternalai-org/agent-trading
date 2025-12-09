# Social Media Analyst Agent - Trading

A sentiment analysis agent that analyzes social media posts, news, and public sentiment in the crypto futures market, providing comprehensive reports on market psychology and sentiment trends.

## Pipeline

```
Social Media Request → Fetch Posts → Analyze Sentiment → Sentiment Report
```

## Responsibilities

1. **Retrieve social media posts** about specific coins from Twitter
2. **Analyze sentiment trends** over the past week
3. **Identify market narratives** and trending topics
4. **Track key influencers** and their predictions
5. **Assess market psychology** and sentiment shifts
6. **Highlight futures-specific metrics** (leverage, liquidations, funding rates)

## Dataflows / APIs used

- **General tweets feed:** `GET /api/news/tweet`
- **Coin-specific tweets:** `GET /api/xconnect/search-topic?query=<COIN>`

**Via server proxies:**
- `GET /api/news/tweet`
- `GET /api/news/search-topic?query=<COIN>`

---

## Tools Available

### get_twitter_posts_coin
Get the latest social media posts about a specific coin from Twitter.

**Parameters:**
- `search_query` (string): Search query for the coin (e.g., "BTC", "BITCOIN", "ETHEREUM")

**Returns:**
- Latest Twitter posts about the coin
- Sentiment analysis
- Influencer mentions
- Trending topics

---

## Analysis Focus Areas

### 1. Sentiment Analysis
- Overall sentiment (bullish/bearish/neutral)
- Sentiment shifts over time
- Sentiment scores and trends
- Emotional indicators (fear, greed, FOMO)

### 2. Market Narratives
- Dominant narratives in social media
- Narrative shifts and changes
- Contrarian signals
- Popular trading themes

### 3. Key Influencers
- Prominent traders and analysts
- Their predictions and calls
- Influence on market sentiment
- Track record analysis

### 4. Futures-Specific Metrics
- Leverage ratios being discussed
- Liquidation levels mentioned
- Funding rates sentiment
- Open interest discussions

### 5. Platform Coverage
- Twitter sentiment
- Reddit discussions
- Telegram communities
- Cross-platform sentiment

---

## Output Format

### Sentiment Report Structure

```markdown
## Social Media Sentiment Analysis - [TICKER]

### Week Overview
[Summary of sentiment trends over the past week]

### Overall Sentiment
- **Current Sentiment**: [Bullish/Bearish/Neutral]
- **Sentiment Score**: [X/10]
- **Trend**: [Improving/Deteriorating/Stable]

### Sentiment Breakdown by Platform

#### Twitter
- **Sentiment**: [Bullish/Bearish/Neutral]
- **Key Topics**: [List of trending topics]
- **Influencers**: [Notable mentions]

#### Reddit
[Similar structure]

#### Telegram
[Similar structure]

### Key Influencers & Predictions

#### [Influencer 1]
- **Prediction**: [Their call]
- **Confidence**: [High/Medium/Low]
- **Market Impact**: [High/Medium/Low]

### Futures-Specific Discussions
- **Leverage Ratios**: [Discussed levels]
- **Liquidation Levels**: [Mentioned prices]
- **Funding Rates**: [Sentiment on rates]
- **Open Interest**: [Discussions]

### Market Narratives
[Analysis of dominant narratives]

### Sentiment Shifts
[How sentiment has changed over the week]

### Trading Implications
[Actionable insights for traders]

### Summary Table
| Metric | Value | Signal |
|--------|-------|--------|
| Overall Sentiment | Bullish/Bearish/Neutral | - |
| Sentiment Score | X/10 | - |
| Key Narrative | [Narrative] | - |
| Influencer Consensus | [Bullish/Bearish] | - |
| Futures Sentiment | [Bullish/Bearish] | - |
```

---

## Important Guidelines

1. **Comprehensive Analysis**: Don't simply state trends are mixed - provide detailed, fine-grained analysis
2. **Sentiment Shifts**: Track how sentiment has changed over time
3. **Notable Predictions**: Highlight predictions from prominent traders
4. **Market-Moving Events**: Identify potential catalysts being discussed
5. **Futures Focus**: Pay special attention to leverage, liquidations, funding rates
6. **Multiple Platforms**: Analyze across Twitter, Reddit, Telegram
7. **Markdown Tables**: Append organized tables at the end of reports

---

## Example Output

```markdown
## Social Media Sentiment Analysis - BTC

### Week Overview
Social media sentiment for BTC has shifted from neutral to bullish over the past week, driven by ETF inflows and positive technical signals.

### Overall Sentiment
- **Current Sentiment**: Bullish
- **Sentiment Score**: 7.5/10
- **Trend**: Improving

### Sentiment Breakdown by Platform

#### Twitter
- **Sentiment**: Bullish
- **Key Topics**: 
  - ETF inflows
  - $100k price target
  - Institutional adoption
- **Influencers**: 
  - @CryptoWhale: "BTC breaking $100k soon"
  - @BitcoinMaxi: "This is the accumulation phase"

### Key Influencers & Predictions

#### @CryptoWhale
- **Prediction**: BTC to $100k by end of month
- **Confidence**: High
- **Market Impact**: High (500k followers)

### Futures-Specific Discussions
- **Leverage Ratios**: Many discussing 10-20x leverage
- **Liquidation Levels**: $88k mentioned as key support
- **Funding Rates**: Positive funding rates indicating bullish sentiment
- **Open Interest**: Increasing, suggesting new positions

### Market Narratives
- Dominant narrative: "Institutional adoption accelerating"
- Secondary narrative: "Bull run continuation"
- Contrarian view: "Overbought, expect pullback"

### Sentiment Shifts
- Week start: Neutral (5/10)
- Mid-week: Bullish (6.5/10)
- Current: Bullish (7.5/10)
- Trend: Steadily improving

### Trading Implications
- Social sentiment supports bullish thesis
- High leverage discussions suggest retail FOMO
- Watch for sentiment extremes (potential reversal signal)
- Funding rates positive but not extreme

### Summary Table
| Metric | Value | Signal |
|--------|-------|--------|
| Overall Sentiment | Bullish | Positive |
| Sentiment Score | 7.5/10 | Bullish |
| Key Narrative | Institutional adoption | Bullish |
| Influencer Consensus | Bullish | Positive |
| Futures Sentiment | Bullish | Positive |
```

---

## Integration with Other Agents

```
Social Media Analyst → Sentiment Report → Researchers/Trader → Trading Decision
```

The Social Media Analyst provides sentiment context for:
- **Bull/Bear/Neutral Researchers**: Use sentiment for arguments
- **Trader**: Considers sentiment in trading decisions
- **Risk Manager**: Evaluates sentiment-driven risks (FOMO, panic)

---

## Data Sources

- **Twitter**: Primary source for crypto sentiment
- **Reddit**: Community discussions
- **Telegram**: Private group sentiment
- **Multiple social platforms**

---

## Disclaimer

⚠️ **IMPORTANT:** This AI agent provides educational analysis only. It is NOT financial advice.

- Social media sentiment can be manipulated
- Sentiment can change quickly
- Don't trade solely on social media sentiment
- Always verify with technical and fundamental analysis
- Consult a licensed financial advisor
- Do your own research (DYOR)

