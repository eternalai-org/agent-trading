#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crypto Price API - Flask server for cryptocurrency price data (Binance Spot)
Usage: python server.py [--port 5000]

Endpoints:
  GET /api/price?symbol=BTC&convert=USDT
"""

import os
import time
import argparse
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()  # load environment variables from .env if present

app = Flask(__name__)

BINANCE_BASE_URL = "https://api.binance.com"
BINANCE_FAPI_BASE_URL = "https://fapi.binance.com"
TAAPI_BASE_URL = "https://api.taapi.io"
DATA_BACKEND_URL = "https://agent.api.eternalai.org"
TAAPI_SECRET = os.getenv("TAAPI_SECRET", "")


def get_coin_price(symbol, convert='USDT'):
    """
    Get the latest coin price by symbol from Binance Spot.

    Args:
        symbol (str): cryptocurrency symbol, e.g. 'BTC'
        convert (str): quote currency (default 'USDT', can be 'USDT', 'BUSD', 'BTC', etc.)

    Returns:
        dict: price data or error message
    """
    # Binance uses trading pair format: BTCUSDT, ETHUSDT, etc.
    trading_pair = f"{symbol.upper()}{convert.upper()}"
    url = f"{BINANCE_BASE_URL}/api/v3/ticker/price"
    params = {"symbol": trading_pair}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            "symbol": symbol.upper(),
            "price": float(data['price']),
            "convert": convert.upper(),
            "trading_pair": trading_pair
        }
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            return {"error": f"Invalid trading pair: {trading_pair}"}
        return {"error": f"HTTP Error: {e.response.status_code}"}
    except KeyError:
        return {"error": f"Symbol '{symbol}' not found"}
    except Exception as e:
        return {"error": str(e)}


def get_futures_market_info(symbol: str):
    """
    Get Binance Futures premium index info for a symbol (USDT-margined).
    """
    symbol = symbol.upper().replace("/", "").replace("USDT", "") + "USDT"
    url = f"{BINANCE_FAPI_BASE_URL}/fapi/v1/premiumIndex"
    try:
        resp = requests.get(url, params={"symbol": symbol}, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_news_tweets():
    """
    Fetch general crypto tweets from DATA_BACKEND_URL.
    """
    if not DATA_BACKEND_URL:
        return {"error": "DATA_BACKEND_URL is not set"}
    try:
        url = f"{DATA_BACKEND_URL}/api/news/tweet"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_coin_tweets(coin: str):
    """
    Fetch coin-specific tweets from DATA_BACKEND_URL.
    """
    if not DATA_BACKEND_URL:
        return {"error": "DATA_BACKEND_URL is not set"}
    try:
        url = f"{DATA_BACKEND_URL}/api/xconnect/search-topic"
        resp = requests.get(url, params={"query": coin}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        # Normalize to tweets list if structure matches dataflows/news.ts
        if isinstance(data, dict) and "result" in data and "tweets" in data["result"]:
            return data["result"]["tweets"]
        return data
    except Exception as e:
        return {"error": str(e)}


def call_taapi(indicator: str, params: dict):
    """
    Proxy to TAAPI indicator endpoint.
    """
    if not TAAPI_SECRET:
        return {"error": "TAAPI_SECRET is not set"}

    query = {
        "secret": TAAPI_SECRET,
        "exchange": "binancefutures",
        "addResultTimestamp": "true",
        **params,
    }
    try:
        resp = requests.get(f"{TAAPI_BASE_URL}/{indicator}", params=query, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def map_indicator_name(indicator: str):
    """
    Support the custom indicator aliases from dataflows/ta_api.ts.
    """
    indicator = indicator.lower()
    if indicator == "close_10_ema":
        return "ema", 10
    if indicator == "close_50_sma":
        return "sma", 50
    if indicator == "close_200_sma":
        return "sma", 200
    return indicator, None


@app.route('/api/price', methods=['GET'])
def api_price():
    """
    API endpoint to get cryptocurrency price from Binance Spot.
    
    Query Parameters:
        symbol (required): Cryptocurrency symbol (e.g., BTC, ETH, SOL)
        convert (optional): Quote currency (default: USDT). Can be USDT, BUSD, BTC, etc.
    
    Returns:
        JSON: {"symbol": "BTC", "price": 93206.21, "convert": "USDT", "trading_pair": "BTCUSDT"}
        or {"error": "error message"}
    """
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Missing required parameter: symbol"}), 400
    
    convert = request.args.get('convert', 'USDT')
    
    result = get_coin_price(symbol, convert)
    
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify(result)


@app.route('/api/futures/market-info', methods=['GET'])
def api_futures_market_info():
    symbol = request.args.get('symbol', 'BTC')
    result = get_futures_market_info(symbol)
    status = 400 if isinstance(result, dict) and "error" in result else 200
    return jsonify(result), status


@app.route('/api/news/tweet', methods=['GET'])
def api_news_tweet():
    result = get_news_tweets()
    status = 400 if isinstance(result, dict) and "error" in result else 200
    return jsonify(result), status


@app.route('/api/news/search-topic', methods=['GET'])
def api_news_search_topic():
    coin = request.args.get('query') or request.args.get('coin')
    if not coin:
        return jsonify({"error": "Missing required parameter: query"}), 400
    result = get_coin_tweets(coin)
    status = 400 if isinstance(result, dict) and "error" in result else 200
    return jsonify(result), status


@app.route('/api/ta/indicator', methods=['GET'])
def api_ta_indicator():
    indicator = request.args.get('indicator')
    ticker = request.args.get('ticker', 'BTC')
    interval = request.args.get('interval', '1h')
    period = request.args.get('period')

    if not indicator:
        return jsonify({"error": "Missing required parameter: indicator"}), 400

    indicator_name, override_period = map_indicator_name(indicator)
    params = {
        "symbol": f"{ticker.upper().replace('/USDT','').replace('USDT','')}/USDT",
        "interval": interval,
    }
    if override_period:
        params["period"] = override_period
    if period and not override_period:
        params["period"] = period

    result = call_taapi(indicator_name, params)
    status = 400 if isinstance(result, dict) and "error" in result else 200
    return jsonify(result), status


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crypto Price API Server (Binance Spot)")
    parser.add_argument("--port", type=int, default=5000, help="Port to run the server (default: 5000)")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    args = parser.parse_args()

    print(f"🚀 Starting Crypto Price API (Binance Spot) on http://{args.host}:{args.port}")
    print(f"📖 Endpoint: GET /api/price?symbol=BTC&convert=USDT")
    print(f"💚 Health: GET /health")
    
    app.run(host=args.host, port=args.port, debug=False)
