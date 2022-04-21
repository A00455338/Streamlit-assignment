

import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import requests as req
from datetime import datetime

st.header("Bitcoin Prices")

Days_value=st.slider("No of days",1,365,90)
status = st.radio("Currency: ", ('cad', 'usd','inr'))

payload = {'vs_currency': status, 'days': Days_value, 'interval': 'daily'}

api_url ='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
res=req.get(api_url, params=payload)
   
df = None
if res.status_code == 200:
    
    json_data = res.json()
    data=json_data['prices']
    df=pd.DataFrame(data,columns=['date','prices'])
else:
    print(req.status_code)

df['date']=pd.to_datetime(df['date'],unit='ms')

st.line_chart(df['prices'])

df3 = df['prices'].mean()
str1= f'Average price during this time was {df3} in {status}'
st.write(str1)