# Trading Agents - AI-Powered Crypto Trading Analysis System

A comprehensive multi-agent AI system for cryptocurrency trading analysis that combines technical analysis, news sentiment, and market research to provide actionable trading decisions for crypto futures markets.

## 🎯 Overview

This project implements a sophisticated trading workflow using multiple specialized AI agents that work together to analyze cryptocurrency markets and generate trading recommendations. The system analyzes BTC and altcoins using technical indicators, news sentiment, and fundamental analysis to provide Long/Short/Hold recommendations with specific entry, stop loss, and take profit levels.

## ✨ Features

- **Multi-Agent Architecture**: Specialized agents for different aspects of market analysis
- **BTC-First Analysis**: BTC market analysis as the foundation for altcoin trading decisions
- **Technical Analysis**: Integration with Binance Futures and technical indicators (RSI, MACD, EMA, SMA, etc.)
- **News & Sentiment Analysis**: Real-time news aggregation and sentiment analysis
- **Debate-Based Decision Making**: Bull, Bear, and Neutral researchers debate before final decision
- **Risk Management**: Comprehensive risk assessment with leverage recommendations
- **RESTful API**: Flask-based API server for market data and technical indicators

## 🏗️ Architecture

### Trading Workflow Pipeline

```
User Request → @market_analyst_btc → market_analyst → news_analyst → 
bear_researcher → bull_researcher → neutral_researcher → research_manager → trader
```

### Flow Diagram

```
┌─────────────────────┐
│  User Request       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ @market_analyst_btc │ → BTC Market Report
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ market_analyst      │ → Market Report (for altcoins)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ news_analyst        │ → News Report
└──────────┬──────────┘
           │
           ├─────────────────┬─────────────────┐
           ▼                 ▼                 ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ bear_researcher  │ │ bull_researcher  │ │neutral_researcher│
│ (Short case)     │ │ (Long case)      │ │ (Hold case)      │
└────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                             ▼
                    ┌──────────────────┐
                    │ research_manager │ → Investment Plan
                    └────────┬─────────┘
                             ▼
┌──────────────────┐
│ trader           │ → Trading Decision
└──────────────────┘
```

## 🤖 Agents

| Agent | Role | Documentation |
|-------|------|---------------|
| **@market_analyst_btc** | Analyze BTC market with BTC-specific indicators | `.cursor/agents/market_analyst_btc.md` |
| **market_analyst** | Analyze market for altcoins with technical indicators | `.cursor/agents/market_analyst.md` |
| **news_analyst** | Analyze news and trends for trading implications | `.cursor/agents/news_analyst.md` |
| **bear_researcher** | Build case for short positions | `.cursor/agents/bear_researcher.md` |
| **bull_researcher** | Build case for long positions | `.cursor/agents/bull_researcher.md` |
| **neutral_researcher** | Build case for holding/avoiding positions | `.cursor/agents/neutral_researcher.md` |
| **research_manager** | Evaluate debate and create investment plan | `.cursor/agents/research_manager.md` |
| **trader** | Make leveraged trading decision | `.cursor/agents/trader.md` |
| **aggressive_debator** | Advocate for high-leverage strategies | `.cursor/agents/aggressive_debator.md` |
| **conservative_debator** | Advocate for low-risk strategies | `.cursor/agents/conservative_debator.md` |
| **risk_manager** | Final risk assessment and trade decision | `.cursor/agents/risk_manager.md` |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- API keys (optional, for advanced features):
  - TAAPI.io secret (for technical indicators)
  - Data backend URL (for news aggregation)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cursor_trading_agents
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)
   Create a `.env` file:
   ```env
   TAAPI_SECRET=your_taapi_secret
   ```

5. **Start the API server**
   ```bash
   python server.py
   ```
   
   The server will start on `http://127.0.0.1:5000` by default.

### Verify Installation

Test the health endpoint:
```bash
curl http://127.0.0.1:5000/health
```

Expected response:
```json
{"status": "ok"}
```

## 📖 Usage

### Using the Trading Command

In Cursor IDE, use the `/trading` command to analyze any cryptocurrency:

```
/trading Should I long or short BTC right now?
```

### Example Workflow

**User:** "Long or short BTC?"

**Result Flow:**
1. **@market_analyst_btc** → Analyzes BTC market → BTC Market Report
2. **market_analyst** → Analyzes market (if altcoin) → Market Report
3. **news_analyst** → Analyzes news and trends → News Report
4. **bear_researcher** → Builds short case → Bear Arguments
5. **bull_researcher** → Builds long case → Bull Arguments
6. **neutral_researcher** → Builds hold case → Neutral Arguments
7. **research_manager** → Evaluates debate → Investment Plan (LONG/SHORT/HOLD)
8. **trader** → Makes trading decision → Trading Decision (Entry, Leverage, SL, TP)

### API Endpoints

#### Get Cryptocurrency Price
```bash
GET /api/price?symbol=BTC&convert=USDT
```

**Response:**
```json
{
  "symbol": "BTC",
  "price": 90449.17,
  "convert": "USDT",
  "trading_pair": "BTCUSDT"
}
```

#### Get Futures Market Info
```bash
GET /api/futures/market-info?symbol=BTC
```

#### Get Technical Indicator
```bash
GET /api/ta/indicator?indicator=rsi&ticker=BTC&interval=4h&period=14
```

**Supported Indicators:**
- `rsi` - Relative Strength Index
- `macd` - Moving Average Convergence Divergence
- `ema` - Exponential Moving Average
- `sma` - Simple Moving Average
- `bbands` - Bollinger Bands
- `atr` - Average True Range
- And more...

#### Get News
```bash
GET /api/news/tweet
GET /api/news/search-topic?query=ETHEREUM
```

## 📁 Project Structure

```
cursor_trading_agents/
├── .cursor/
│   ├── agents/              # Agent documentation
│   │   ├── market_analyst_btc.md
│   │   ├── market_analyst.md
│   │   ├── news_analyst.md
│   │   ├── bear_researcher.md
│   │   ├── bull_researcher.md
│   │   ├── neutral_researcher.md
│   │   ├── research_manager.md
│   │   ├── trader.md
│   │   └── ...
│   ├── commands/           # Cursor commands
│   │   └── trading.md
│   └── workflows/          # Workflow definitions
│       └── trading.md
├── server.py               # Flask API server
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

## 🔧 Configuration

### Server Configuration

The server can be configured via command-line arguments:

```bash
python server.py --port 5000 --host 127.0.0.1
```

### Environment Variables

- `TAAPI_SECRET`: API secret for TAAPI.io technical indicators

## 📊 Trading Decision Output

The system provides comprehensive trading recommendations including:

- **Position Direction**: LONG / SHORT / HOLD
- **Entry Price**: Specific entry levels with rationale
- **Stop Loss**: Risk management levels
- **Take Profit**: Multiple TP levels (TP1, TP2, TP3)
- **Leverage Recommendation**: Appropriate leverage (10x-50x)
- **Risk/Reward Ratio**: Calculated R:R ratios
- **Confidence Level**: High / Medium / Low
- **Market Analysis**: Technical, sentiment, and fundamental analysis

## 🛡️ Risk Management

The system emphasizes proper risk management:

- Position sizing: 1-2% risk per trade
- Stop loss placement: Below key support/resistance
- Leverage recommendations: Based on volatility and trend strength
- Multiple take profit levels: Scale out of positions
- BTC correlation analysis: Consider market leader impact

## ⚠️ Disclaimer

**IMPORTANT:** This AI system provides educational analysis only. It is NOT financial advice.

- Cryptocurrency trading involves significant risk
- Leverage amplifies both gains and losses
- Past performance doesn't guarantee future results
- Always use proper risk management
- Consult a licensed financial advisor
- Do your own research (DYOR)
- Never trade with money you can't afford to lose

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

[Add your license here]

## 🔗 Resources

- [Binance API Documentation](https://binance-docs.github.io/apidocs/)
- [TAAPI.io Documentation](https://taapi.io/documentation/)
- [Cursor IDE Documentation](https://cursor.sh/docs)

## 📧 Support

For issues, questions, or contributions, please open an issue on the repository.

---

**Built with ❤️ for the crypto trading community**
