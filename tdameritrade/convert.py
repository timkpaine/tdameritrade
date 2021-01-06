#
# Convert API responses to Pandas DataFrames
#

import pandas as pd


def accounts(data):
    """accounts as dataframe"""
    account_dataframes = []
    for accountId, value in data.items():
        account_dataframes.append(pd.io.json.json_normalize(value))
        account_dataframes[-1].columns = [
            c.replace("securitiesAccount.", "")
            for c in account_dataframes[-1].columns
        ]
    return pd.concat(account_dataframes)


def transactions(data):
    """transaction information as Dataframe"""
    return pd.json_normalize(data)


def search(data):
    """search for symbol as a dataframe"""
    ret = []
    for symbol in data:
        ret.append(data[symbol])

    return pd.DataFrame(ret)


def instrument(data):
    """instrument info from cusip as dataframe"""
    return pd.DataFrame(data)


def quote(data):
    """quote as dataframe"""
    return pd.DataFrame(data).T.reset_index(drop=True)


def history(data):
    """get history as dataframe"""
    df = pd.DataFrame(data["candles"])
    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")
    return df


def options(data):
    """options chain as dataframe"""
    ret = []
    for date in data["callExpDateMap"]:
        for strike in data["callExpDateMap"][date]:
            ret.extend(data["callExpDateMap"][date][strike])
    for date in data["putExpDateMap"]:
        for strike in data["putExpDateMap"][date]:
            ret.extend(data["putExpDateMap"][date][strike])

    df = pd.DataFrame(ret)
    for col in (
        "tradeTimeInLong",
        "quoteTimeInLong",
        "expirationDate",
        "lastTradingDay",
    ):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], unit="ms")

    for col in ("delta", "gamma", "theta", "vega", "rho", "volatility"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
