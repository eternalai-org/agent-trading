## Trading Workflow

### Pipeline

```
User Request → @market_analyst_btc → market_analyst → news_analyst → bear_researcher → bull_researcher → neutral_researcher → research_manager → trader
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

### Agents

| Agent | Role | Documentation |
|-------|------|---------------|
| **@market_analyst_btc** | Analyze BTC market with BTC-specific indicators | See `.cursor/agents/market_analyst_btc.md` |
| **market_analyst** | Analyze market for altcoins with technical indicators | See `.cursor/agents/market_analyst.md` |
| **news_analyst** | Analyze news and trends for trading implications | See `.cursor/agents/news_analyst.md` |
| **bear_researcher** | Build case for short positions | See `.cursor/agents/bear_researcher.md` |
| **bull_researcher** | Build case for long positions | See `.cursor/agents/bull_researcher.md` |
| **neutral_researcher** | Build case for holding/avoiding positions | See `.cursor/agents/neutral_researcher.md` |
| **research_manager** | Evaluate debate and create investment plan | See `.cursor/agents/research_manager.md` |
| **trader** | Make leveraged trading decision | See `.cursor/agents/trader.md` |
| **aggressive_debator** | Advocate for high-leverage strategies | See `.cursor/agents/aggressive_debator.md` |
| **conservative_debator** | Advocate for low-risk strategies | See `.cursor/agents/conservative_debator.md` |
| **risk_manager** | Final risk assessment and trade decision | See `.cursor/agents/risk_manager.md` |

---

## Example Usage

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