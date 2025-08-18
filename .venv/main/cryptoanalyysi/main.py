# Ai made this
import requests
import pandas as pd
import ta
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np


# 🔹 Hae historiallinen hintadata CoinGecko API:sta
def hae_historia_coinilla(coin_id='bitcoin', days=30):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {'vs_currency': 'usd', 'days': days}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
        prices.set_index('timestamp', inplace=True)
        return prices
    except Exception as e:
        print(f"⚠️ Virhe haettaessa dataa: {coin_id} - {e}")
        return pd.DataFrame()

# 🔹 Lisää tekniset indikaattorit
def analysoi_data(df):
    df['SMA_7'] = df['price'].rolling(window=7).mean()
    df['SMA_14'] = df['price'].rolling(window=14).mean()
    df['RSI'] = ta.momentum.RSIIndicator(close=df['price']).rsi()
    return df

# 🔹 Luo analyysivinkit
def anna_vinkki(df):
    viimeisin = df.iloc[-1]
    vinkit = []

    if viimeisin['RSI'] < 30:
        vinkit.append("📉 RSI < 30 → *Ylilyöty* → Mahdollinen ostopaikka")
    elif viimeisin['RSI'] > 70:
        vinkit.append("📈 RSI > 70 → *Ylisuosittu* → Mahdollinen myyntipaikka")
    else:
        vinkit.append("⚖️ RSI on neutraali")

    if viimeisin['SMA_7'] > viimeisin['SMA_14']:
        vinkit.append("🔼 Lyhyen aikavälin *nousutrendi* (SMA7 > SMA14)")
    else:
        vinkit.append("🔽 Lyhyen aikavälin *laskutrendi* (SMA7 < SMA14)")
    
    return vinkit

def ennusta_hinta(df):
    # Käytetään viimeisiä 7 datapistettä
    recent = df[['price']].dropna().tail(7)
    if len(recent) < 7:
        return None, None, None

    # Tee "päivänumero" X:ksi
    recent['days'] = np.arange(len(recent))
    X = recent['days'].values.reshape(-1, 1)  # Korjattu kohta
    y = recent['price'].values

    model = LinearRegression()
    model.fit(X, y)

    # Ennusta seuraava päivä (päivänumero 7)
    next_day = np.array([[7]])
    predicted_price = model.predict(next_day)[0]
    seuraava_pvm = df.index[-1] + pd.Timedelta(days=1)

    return model, seuraava_pvm, predicted_price


# 🔹 Näytä kuvaajat
def piirra_kuvaajat(df, coin_name):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    fig.suptitle(f"{coin_name.capitalize()} - Hintakehitys, Liukuvat keskiarvot ja RSI", fontsize=16)

    # Hintakäyrä ja liukuvat keskiarvot
    ax1.plot(df.index, df['price'], label='Hinta', color='black')
    ax1.plot(df.index, df['SMA_7'], label='SMA 7', color='blue', linestyle='--')
    ax1.plot(df.index, df['SMA_14'], label='SMA 14', color='orange', linestyle='--')

    # 🔮 Ennuste: viimeisten 7 päivän trendi + seuraava päivä
    ennuste, seuraava_pvm, ennustettu_hinta = ennusta_hinta(df)
    ax1.plot([df.index[-7], seuraava_pvm], [df['price'].iloc[-7], ennustettu_hinta],
             label='Ennuste (lineaarinen)', color='green', linestyle=':')

    ax1.set_ylabel("USD")
    ax1.legend()
    ax1.grid(True)

    # RSI
    ax2.plot(df.index, df['RSI'], label='RSI', color='purple')
    ax2.axhline(70, color='red', linestyle='--', alpha=0.5)
    ax2.axhline(30, color='green', linestyle='--', alpha=0.5)
    ax2.set_ylabel("RSI")
    ax2.set_xlabel("Päivämäärä")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()

# 🔹 Suorita analyysi usealle kryptolle
def analysoi_kryptot(coin_list, days=30):
    for coin in coin_list:
        print(f"\n🔎 Analysoidaan: {coin.capitalize()} ({days} päivän data)\n{'-'*50}")
        data = hae_historia_coinilla(coin, days)
        if data.empty or len(data) < 15:
            print("⚠️ Ei riittävästi dataa analyysiin.\n")
            continue

        analysoitu = analysoi_data(data)
        vinkit = anna_vinkki(analysoitu)
        for v in vinkit:
            print(v)

        piirra_kuvaajat(analysoitu, coin)

# 🔹 Pääohjelma
if __name__ == "__main__":
    kryptot = ['bitcoin', 'ethereum', 'solana', 'ripple']
    analysoi_kryptot(kryptot, days=30)
