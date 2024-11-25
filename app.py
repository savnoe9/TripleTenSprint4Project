#Import appropriate libraries
import pandas as pd
import streamlit as st
#from scipy import stats as sta
#import numpy as np
#import matplotlib.pyplot as plt
import plotly_express as px

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


st.header("Vehicle Advertisement Date Analysis")

st.write("View Vehicle Advertisement Dataset")
TenK = st.checkbox("Show vehicles under $10,000")

if TenK:
    st.dataframe(print(df.loc[df['price'] < 10000]))
else:
    st.dataframe(df)

st.subheader("Price vs. Odometer")


#price_vs_odometer = st.scatter_chart(
#    df,
#    x='odometer',
#    y='price'
#    #use_container_width=True
#)


#st.write(price_vs_odometer)

import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)