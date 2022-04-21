

import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import requests as req
from datetime import datetime

st.header("Bitcoin Prices")
r=req.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interval=daily')
data=r.json()['prices']
df=pd.DataFrame(data,columns=['date','prices'])


df['date']=pd.to_datetime(df['date'],unit='ms')
df1=df['date'].dt.strftime("%d-%b")

Days_value=st.slider("No of days",1,365,90)
status = st.radio("Currency: ", ('cad', 'usd','inr'))
df2=df['prices']

if status=="usd":
    df['prices'] = df['prices'].apply(lambda x: x/1.2613)
elif status=="inr":
    df['prices'] = df['prices'].apply(lambda x: x*60)


df['date']=df['date'].apply(lambda x:(x-datetime(2022,1,1)).days)


fig, ax = plt.subplots()
plt.grid()
ax.plot(df1,df2)
ax.set_ylim(ymin=0)
ax.set_xlim(xmax=Days_value)
# Axis multiplier
multiplier = 12

# Set a tick on each integer multiple
locator = plt.MultipleLocator(multiplier)

# Set the locator of the major ticker
ax.xaxis.set_major_locator(locator)

st.pyplot(fig)

df3 = df['prices'].mean()
str1= "Average price during this time was ",df3,status
st.text(str1)