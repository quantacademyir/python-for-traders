"""Builds the simulated sample data used by the course "Python for Traders".

The numbers are SIMULATED (seeded random walk), not real market data. They are
made to look like crypto daily/hourly candles so lessons can run without any API.

Outputs (committed):
  data/btc_daily_sample.csv   365 clean daily candles
  data/btc_hourly_sample.csv  30 days of hourly candles with deliberate flaws

Run: python3 scripts/make_sample_data.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent / "data"
OUT.mkdir(parents=True, exist_ok=True)


def candles(index, start_price, sigma, df, rng, volume_mean):
    """Random walk with fat tails (Student t) -> OHLCV candles."""
    n = len(index)
    t = rng.standard_t(df, size=n) * sigma / np.sqrt(df / (df - 2))
    close = start_price * np.exp(np.cumsum(t))
    open_ = np.concatenate([[start_price], close[:-1]])
    spread = np.abs(rng.normal(0, sigma * 0.6, size=n))
    high = np.maximum(open_, close) * (1 + spread)
    low = np.minimum(open_, close) * (1 - spread)
    volume = rng.lognormal(mean=np.log(volume_mean), sigma=0.35, size=n)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume}, index=index
    )


# --- daily: 2025-01-01 .. 2025-12-31 -----------------------------------------
rng = np.random.default_rng(12)
days = pd.date_range("2025-01-01", periods=365, freq="D", tz="UTC")

# Lesson 2 uses this exact first week of closes; the sample starts with it,
# then continues as a fat-tailed random walk.
week = [98500, 99200, 97800, 99900, 101200, 100400, 102000]
closes = list(week)
for r in rng.standard_t(4, size=365 - len(week)) * 0.022 / np.sqrt(2):
    closes.append(closes[-1] * float(np.exp(r)))
daily = pd.DataFrame({"close": closes}, index=days)
daily["open"] = [98000] + closes[:-1]
body_hi = daily[["open", "close"]].max(axis=1)
body_lo = daily[["open", "close"]].min(axis=1)
daily["high"] = body_hi * (1 + np.abs(rng.normal(0, 0.012, size=365)))
daily["low"] = body_lo * (1 - np.abs(rng.normal(0, 0.012, size=365)))
daily["volume"] = rng.lognormal(mean=np.log(1250), sigma=0.35, size=365)
daily = daily[["open", "high", "low", "close", "volume"]]

daily_out = daily.copy()
daily_out.index = daily_out.index.strftime("%Y-%m-%d")
daily_out.index.name = "date"
daily_out.round({"open": 1, "high": 1, "low": 1, "close": 1, "volume": 2}).to_csv(
    OUT / "btc_daily_sample.csv"
)

# --- hourly: 2025-03-01 .. 2025-03-30 with deliberate flaws -------------------
rng = np.random.default_rng(2025)
hours = pd.date_range("2025-03-01 00:00", periods=30 * 24, freq="h", tz="UTC")
hourly = candles(hours, 86000, 0.004, 4, rng, 55)
hourly = hourly.round({"open": 1, "high": 1, "low": 1, "close": 1, "volume": 3})
hourly.index = hourly.index.strftime("%Y-%m-%d %H:%M:%S+00:00")
hourly.index.name = "timestamp"

flawed = hourly.copy()
flawed.iloc[[50, 51, 300], flawed.columns.get_loc("close")] = np.nan  # missing closes
flawed.iloc[410, flawed.columns.get_loc("close")] = 0.0  # impossible price
flawed = flawed.drop(flawed.index[[120, 121]])  # two hours missing entirely
flawed = pd.concat([flawed, flawed.iloc[[200]]])  # one duplicated row
order = list(range(len(flawed)))
order[500], order[501] = order[501], order[500]  # two rows out of order
flawed = flawed.iloc[order]
flawed.to_csv(OUT / "btc_hourly_sample.csv")

print("daily", len(daily), "hourly", len(flawed))
