import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Page title
st.title("🚗 Used Car Price Prediction")

# User Inputs
year = st.number_input("Year", 2000, 2025, 2018)
km_driven = st.number_input("KM Driven", 0, 300000, 40000)
mileage = st.number_input("mileage(km/ltr/kg)")
engine = st.number_input("Engine (CC)",min_value=800,max_value=2000)
seats = st.number_input("Seats",min_value=5,max_value=14)
owner = st.selectbox('Owner Type',
                     ['First Owner',
                      'Second Owner',
                      'Third Owner',
                      'Fourth & Above Owner'])
#map to numeric values
owner_mapping = {'First Owner':0,
                 'Second Owner':1,
                 'Third Owner':2,
                 'Fourth & Above Owner':3}
owner = owner_mapping[owner]

brand = st.selectbox("Brand", [
    "BMW","Chevrolet","Ford","Honda","Hyundai",
    "Mahindra","Maruti","Mercedes-Benz","Nissan",
    "Renault","Skoda","Tata","Toyota","Other"
])

fuel = st.selectbox("Fuel", ["Diesel","Petrol","LPG"])
transmission = st.selectbox("Transmission", ["Manual","Automatic"])
seller_type = st.selectbox("Seller Type", ["Individual","Trustmark Dealer"])

# Prediction button
if st.button("Predict Price"):

    # Create empty dataframe with same columns
    input_df = pd.DataFrame(columns=model.feature_names_in_)
    input_df.loc[0] = 0

    # Fill numeric values
    input_df.at[0, 'year'] = year
    input_df.at[0, 'km_driven'] = km_driven
    input_df.at[0, 'mileage(km/ltr/kg)'] = mileage
    input_df.at[0, 'engine'] = engine
    input_df.at[0, 'seats'] = seats
    input_df.at[0, 'owner'] = owner

    # One-hot encoding
    brand_col = f"brand_{brand}"
    fuel_col = f"fuel_{fuel}"
    transmission_col = f"transmission_{transmission}"
    seller_col = f"seller_type_{seller_type}"

    if brand_col in input_df.columns:
        input_df.at[0, brand_col] = 1

    if fuel_col in input_df.columns:
        input_df.at[0, fuel_col] = 1

    if transmission_col in input_df.columns:
        input_df.at[0, transmission_col] = 1

    if seller_col in input_df.columns:
        input_df.at[0, seller_col] = 1

    # Scaling
    numeric_cols = ['year','km_driven','mileage(km/ltr/kg)','engine','seats']
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Prediction
    y_log = model.predict(input_df)
    y_actual = np.exp(y_log)

    st.success(f"💰 Predicted Price: ₹ {round(y_actual[0], 0)}")