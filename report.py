"""One-page report for a daily price file (final project of the course).

Usage:
  python report.py data/btc_daily_sample.csv "Simulated BTC" report.png

The CSV needs the columns date,open,high,low,close,volume.
"""
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def load_daily(path):
    """Read daily candles; stop loudly if the data is not usable."""
    df = pd.read_csv(path, parse_dates=["date"], index_col="date").sort_index()
    if df.index.duplicated().any():
        raise ValueError("duplicate dates")
    if df["close"].isna().any() or (df["close"] <= 0).any():
        raise ValueError("close has missing or non-positive values")
    return df


def add_columns(df):
    out = df.copy()
    out["ret"] = out["close"].pct_change()
    out["ma20"] = out["close"].rolling(20).mean()
    out["ma50"] = out["close"].rolling(50).mean()
    out["drawdown"] = out["close"] / out["close"].cummax() - 1
    return out


def summarize(df):
    r = df["ret"].dropna()
    return {
        "days": len(df),
        "total_return": df["close"].iloc[-1] / df["close"].iloc[0] - 1,
        "daily_vol": r.std(),
        "annual_vol": r.std() * np.sqrt(365),
        "best_day": (r.idxmax().date(), r.max()),
        "worst_day": (r.idxmin().date(), r.min()),
        "up_days_share": (r > 0).mean(),
        "max_drawdown": df["drawdown"].min(),
        "max_drawdown_date": df["drawdown"].idxmin().date(),
    }


def print_summary(s):
    print(f"Days: {s['days']}")
    print(f"Total return: {s['total_return']:.2%}")
    print(f"Daily volatility: {s['daily_vol']:.2%}")
    print(f"Annualized volatility: {s['annual_vol']:.1%}")
    print(f"Best day: {s['best_day'][0]} ({s['best_day'][1]:.2%})")
    print(f"Worst day: {s['worst_day'][0]} ({s['worst_day'][1]:.2%})")
    print(f"Share of up days: {s['up_days_share']:.1%}")
    print(f"Max drawdown: {s['max_drawdown']:.2%} on {s['max_drawdown_date']}")


def plot_report(df, title, filename):
    fig, axes = plt.subplots(3, 1, figsize=(10, 9), gridspec_kw={"height_ratios": [3, 1.6, 1.6]})

    ax = axes[0]
    ax.plot(df.index, df["close"], label="Close", linewidth=1.4)
    ax.plot(df.index, df["ma20"], label="MA20", linewidth=1.1)
    ax.plot(df.index, df["ma50"], label="MA50", linewidth=1.1)
    ax.set_title(title)
    ax.set_ylabel("Price (USDT)")
    ax.grid(alpha=0.3)
    ax.legend()

    ax = axes[1]
    ax.hist(df["ret"].dropna() * 100, bins=40, edgecolor="white")
    ax.axvline(0, color="black", linewidth=1)
    ax.set_xlabel("Daily return (%)")
    ax.set_ylabel("Days")

    ax = axes[2]
    ax.fill_between(df.index, df["drawdown"] * 100, 0, alpha=0.5)
    ax.set_ylabel("Drawdown (%)")
    ax.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(filename, dpi=130, bbox_inches="tight")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/btc_daily_sample.csv"
    title = sys.argv[2] if len(sys.argv) > 2 else "One-page report"
    out = sys.argv[3] if len(sys.argv) > 3 else "report.png"
    df = add_columns(load_daily(path))
    print_summary(summarize(df))
    plot_report(df, title, out)
    print(f"Saved {out}")
