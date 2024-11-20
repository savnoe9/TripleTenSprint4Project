#Import appropriate libraries
import pandas as pd
import streamlit as st
from scipy import stats as sta
import numpy as np
#import matplotlib.pyplot as plt
import plotly_express as px

#Import dataset
df = pd.read_csv('vehicles_us.csv')
#df.info()

st.write("""
         ##Vehicles by Make
          """)

#st.scatter_chart()