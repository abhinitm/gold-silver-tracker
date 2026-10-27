import yfinance as yf

df = yf.download("GOLDBEES.NS", period="1mo", interval="1d",
                    auto_adjust=False, progress=False)

print(df.tail())
print("Shape:", df.shape)
print("Columns:", list(df.columns))