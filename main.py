tickers=["FXGD","FXUS","FXIT","SBSP","FXRL","FXRB","FXRU","SBCB","SBGB","SBRB"]
import requests
import apimoex
import pandas as pd
df=pd.DataFrame()
for ticker in tickers:
    with requests.Session() as session:
        data = apimoex.get_board_history(session, ticker,board="TQTF")
        df1 = pd.DataFrame(data)
        df1.set_index('TRADEDATE', inplace=True)
        df.info()
        df[ticker]=df1["CLOSE"]
df.to_csv("your_table.csv",sep=";")