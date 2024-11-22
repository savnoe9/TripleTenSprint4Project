#Import appropriate libraries
import pandas as pd
import streamlit as st
from scipy import stats as sta
import numpy as np
#import matplotlib.pyplot as plt
#import plotly_express as px

#Import dataset
df = pd.read_csv('vehicles_us.csv')
#df.info()

#Drop rows where model year or odometer reading is missing
df=df.dropna(subset=['model_year'])
df=df.dropna(subset=['odometer'])

#Convert columns to appropriate data types
df['date_posted'] = pd.to_datetime(df['date_posted'])
df['is_4wd'] = df['is_4wd'].fillna(value=0)
df['is_4wd'] = df['is_4wd'].astype('int')
df['cylinders'] = df['cylinders'].fillna(value=0)
df['cylinders'] = df['cylinders'].astype('int')
df['model_year'] = df['model_year'].astype('int')
df['odometer'] = df['odometer'].astype('int')

#Add new column - manufacturer
df['manufacturer'] = df['model'].apply(lambda x:x.split()[0])

#Add new column - luxury vs standard
luxury_brands = ['bmw','mercedes-benz','acura','cadillac']
luxury_class = []
for value in df['manufacturer']:
    if value in luxury_brands:
        luxury_class.append('luxury')
    else:
        luxury_class.append('normal')
df['luxury_class'] = luxury_class



st.write("""
         ##View Vehicle Advertisement Dataset
          """)
TenK = st.checkbox("Show vehicles under $10,000")

if TenK:
    st.write(print(df.loc[df['price'] < 10000]))
else:
    print(df)

st.write("""
         ##Price vs. Odometer'
          """)


#price_vs_odometer = st.scatter_chart(
#    df,
#    x='odometer',
#    y='price'
#    #use_container_width=True
#)


#st.write(price_vs_odometer)