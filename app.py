import sys
sys.setrecursionlimit(1500)

#Import appropriate libraries
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
from scipy import stats as sta
import numpy as np
import plotly_express as px


#Import dataset
df = pd.read_csv('vehicles_us.csv')
#df.info()

#Drop rows where model year or odometer reading is missing
#df=df.dropna(subset=['model_year'])
#df=df.dropna(subset=['odometer'])

#Convert columns to appropriate data types
df['date_posted'] = pd.to_datetime(df['date_posted'])
df['is_4wd'] = df['is_4wd'].fillna(value=0)
df['is_4wd'] = df['is_4wd'].astype('int')
df['cylinders'] = df['cylinders'].fillna(value=0)
df['cylinders'] = df['cylinders'].astype('int')
df['model_year'] = df['model_year'].fillna(value=0)
df['model_year'] = df['model_year'].astype('int')
df['odometer'] = df['odometer'].fillna(value=0)
df['odometer'] = df['odometer'].astype('int')
df['paint_color'] = df['paint_color'].fillna(value='Unknown')


# Calculate the median cylinders for each model_year, fill in missing values
median_cylinders = df.groupby(['model_year', 'model'])['cylinders'].transform('median')
df['cylinders'] = df['cylinders'].fillna(median_cylinders)
df['cylinders'] = df['cylinders'].fillna(value=0)
df['cylinders'] = df['cylinders'].astype('int')

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

st.subheader("View Vehicle Advertisement Dataset")
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

#We can see here that most vehicles are listed within a range of 8-50 days for all types of vehicles.

st.subheader("Price vs. Odometer Reading")

#Create Scatterplot
scatdf1 = df.loc[df['price'] < 100000]
scatdf = scatdf1.loc[scatdf1['odometer'] < 600000]

scat = px.scatter(scatdf, x='price', y='odometer', opacity=0.5, color ='manufacturer')

event = st.plotly_chart(scat, on_select="rerun")

#We can see that there are some outliers in both price and odometer reading based on this scatterplot. However, it is clear that most vehicles sell for under $50,000 with less than 200,000 miles on them.


st.subheader('Distribution of Sold Vehicles by Manufacturer')
manubar = px.bar(
                df,
                x = 'manufacturer', 
                labels={'manufacturer': 'Vehicle Manufacturer'},
                width=1600,
                height=1000)

st.plotly_chart(manubar)

st.subheader('Distribution of Models Sold')
modelbar = px.bar(
                df,
                x = 'model', 
                labels={'model': 'Vehicle Model'},
                width=1600,
                height=1000)

st.plotly_chart(modelbar)


st.subheader('Vehicle Manufactureres and Models')

manu_hist = px.histogram(df,x='manufacturer',color='model', color_discrete_sequence=px.colors.qualitative.Set1 )
st.write(manu_hist)


st.subheader('Vehicle Types by Class')

lux_hist = px.histogram(df,x='luxury_class',color='type')
st.write(lux_hist)



st.subheader('Condition vs. Model Year')

conddf = df.loc[df['model_year'] > 0]

cond_year_hist = px.histogram(conddf,x='model_year',color='condition')
st.write(cond_year_hist)




# st.subheader("Vehicle Manufacturer Price Comparison")
# manufac_list = sorted(df['manufacturer'].unique())
# manufacturer_1 = st.selectbox(
#                               label='Select manufacturer 1', 
#                               options=manufac_list, 
#                               index=manufac_list.index('ford')
#                               )

# manufacturer_2 = st.selectbox(
#                               label='Select manufacturer 2',
#                               options=manufac_list, 
#                               index=manufac_list.index('toyota')
#                               )

# mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
# df_filtered = df[mask_filter]

# normalize = st.checkbox('Normalize histogram', value=True)
# if normalize:
#     histnorm = 'percent'
# else:
#     histnorm = None

# filtered_hist = px.histogram(df_filtered,
#                       x='price',
#                       nbins=30,
#                       color='manufacturer',
#                       histnorm=histnorm,
#                       barmode='overlay')

# st.write(filtered_hist)