#Import appropriate libraries
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
from scipy import stats as sta
import numpy as np
import matplotlib.pyplot as plt
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
    st.dataframe(df.loc[df['price'] < 10000])
else:
    st.dataframe(df)



st.subheader("Vehicle Types Compared to Days Listed")

#Create Histogram

fig = px.histogram(
    df,
    x='days_listed',
    color='type',
    labels={'days_listed': 'Days Listed', 'type': 'Vehicle Type'},
    color_discrete_sequence=px.colors.qualitative.Set1 
)

st.plotly_chart(fig)


st.subheader("Price vs. Odometer Reading")

#Create Scatterplot
scatdf1 = df.loc[df['price'] < 100000]
scatdf = scatdf1.loc[scatdf1['odometer'] < 600000]

scat = px.scatter(scatdf, x='price', y='odometer', opacity=0.5)

event = st.plotly_chart(scat, on_select="rerun")


model_list = df['model'].value_counts().sort_index()
model_list.columns=['model','sales']
#print(model_list)



modelbar = px.bar(
                df,
                title= 'Distribution of Models Sold',
                x = 'model', 
                labels={'model': 'Vehicle Model'},
                color_discrete_sequence=px.colors.qualitative.Set1,
                width=1600,
                height=1000)

st.plotly_chart(modelbar)


st.subheader('Vehicle Types by Class')

lux_hist = px.histogram(df,x='luxury_class',color='type')
st.write(lux_hist)


st.subheader('Condition vs. Model Year')

cond_year_hist = px.histogram(df,x='model_year',color='condition')
st.write(cond_year_hist)




# get user's inputs from a dropdown menu
manufac_list = sorted(df['manufacturer'].unique())
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('hyundai')
                              )
# filter the dataframe 
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
filtered_hist = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')

st.write(filtered_hist)