#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA
import numpy as np 
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import pyplot




data = pd.read_excel("CO2 dataset.xlsx")
data2 = pd.read_csv("CO2_forecast_data_100years.csv",header=0, index_col=0,parse_dates=True )


final_arima = ARIMA(data2['CO2'],order = (5,1,3))
final_arima = final_arima.fit()



st.title("Forecasting CO2 Emission")
nav = st.sidebar.radio("CO2 Emission",["Forecast"])
if nav == "Forecast":
    
    year = st.slider("Select number of Year from 2015",1,100,step = 1)

    st.subheader("Forecasting the data for next few years")
    
    
    pred = final_arima.forecast(year)

   
    if st.button("Predict"):
       st.subheader(f"Your predicted CO2 emission from year 2015" )
       pred

       st.subheader("Line plot of the Forecasted data")
       st.line_chart(pred)

       
       fig= plt.figure(figsize=(20,8))


# In[ ]:




