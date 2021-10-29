import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open("Home_Loan.pkl","rb"))

def main():
    st.title("Home Price Prediction")
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://st2.depositphotos.com/1074452/7351/i/600/depositphotos_73511887-stock-photo-house-prices-increase-means-return.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://st2.depositphotos.com/1074452/7351/i/600/depositphotos_73511887-stock-photo-house-prices-increase-means-return.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    html_temp = """
    <div style="background-color:Black;padding:5px">
    <h2 style="color:white;text-align:center;">Enter the following details to check price of the house </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    bathrooms = st.text_input("bathrooms","Enter no of bathrooms(0.0-8.0)")
    sqft_living = st.text_input("sqft_living","Enter sqft_living(290-12050)")
    floors = st.text_input("floors","Enter no of floors(1.0-3.5)")
    view = st.text_input("view","Enter view(0-4)")
    sqft_above = st.text_input("sqft_above","Enter sqft_above(290-8860)")
    condition = st.text_input("condition","Enter House condition in(1-5) rating")
    grade = st.text_input("	grade","Enter Grade(1-13)")
    year_built = st.text_input("yr_built","Enter the year the house was bulit(1900-2015)")
    year_renovated = st.text_input("yr_renovated","Enter how many years back house has been renovated 0 if never or else enter year(0,1990-2015)")
    sqft_basement = st.text_input("sqft_basement","Enter sqft_basement(0-3480)")
    
    
    inputs = [[bathrooms,sqft_living,floors,view,sqft_above,condition,grade,year_built,year_renovated,sqft_basement]] #our inputs
    result=""
    if st.button("Predict"): #making and printing our prediction
        result = model.predict(inputs)
        st.success('The Price Offered for your house is {}'.format(result))
        
        
if __name__=="__main__":
    main()