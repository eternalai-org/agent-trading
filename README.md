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

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- API keys (optional, for advanced features):
  - TAAPI.io secret (for technical indicators)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/eternalai-org/agent-trading.git
   cd agent-trading
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

In Cursor/Claude IDE, use the `/trading` command to analyze any cryptocurrency:

```
/trading Should I long or short BTC right now?
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

## 📧 Support

For issues, questions, or contributions, please open an issue on the repository.

---

**Built with ❤️ for the crypto trading community**
