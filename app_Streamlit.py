# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import sklearn
from PIL import Image
from sklearn.preprocessing import MinMaxScaler

with open('model.pkl', 'rb') as pickle_in:
     regressor = pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_stock(Sentiment_score):
    
    ss = float(Sentiment_score)
    #ov = float(Open_Value)

    prediction = regressor.predict([[ss]])
    change_value_of_share = -36.56+(prediction-0)*(24.36+36.56)/10
    return change_value_of_share



def main():
    st.title("Stock Price Sentiment Analyzer")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Stock Prediction by Sentiments </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Sentiment_score = st.text_input("Sentiment score","Type Here any value from 0 to 10")
    Open_Value = st.text_input("Enter previous day Opening value of Stock","Type value of previous day opening price")
    
    
    result=0.000
    Org_sp=""
    Pred_Open_Value=""
    sentiment_score=""
    pred=""
    if st.button("Predict"):
        ss = float(Sentiment_score)
        ov = float(Open_Value)
        result = predict_stock(Sentiment_score)
        pred = str(result)
        sentiment_score = str(-0.9022+(ss-0)*(0.9231+0.9022)/10)
        Pred_Open_Value = str((predict_stock(Sentiment_score)/100+1)*ov)
    st.success('The predicted value of upcoming stock-price is Rs.{} : opening price: Rs.{} & sentiment_score: {} & % change in opening:{} '.format(Pred_Open_Value,Org_sp,sentiment_score,pred))
    

if __name__=='__main__':
    main()
    
