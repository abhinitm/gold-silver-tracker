import yfinance as yf

TICKERS = {
       "GOLDBEES.NS": "Gold ETF (INR)",
       "SILVERBEES.NS": "Silver ETF (INR)",
       "GC=F": "Gold futures (USD/oz)",
       "SI=F": "Silver futures (USD/oz)",
       "INR=X": "USD/INR rate",
   }

for ticker, label in TICKERS.items():
       df = yf.download(ticker, period="1mo", interval="1d",
                        auto_adjust=False, progress=False)
       print(f"\n===== {ticker} | {label} =====")
       print("Rows:", len(df))
       print("First date:", df.index.min().date(), "| Last date:", df.index.max().date())
       print(df[["Close", "Volume"]].tail(3))