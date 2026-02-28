Used Cars Price Prediction

📌 Project Overview -
This project predicts the selling price of used cars using Machine Learning.
The model is trained on real car dataset and deployed using Streamlit as a web application.
The goal is to estimate car price based on features like brand, year, engine, mileage, fuel type, etc.


🧠 Problem Statement - 
Used car prices vary depending on multiple factors.
This project builds a regression model to predict car prices accurately based on historical data.


⚙️ Technologies Used - 
Python
Pandas
NumPy
Scikit-learn
Streamlit
Pickle

🔍 Data Preprocessing - 
Removed missing values
Removed duplicates
Handled outliers
Log transformation applied to target variable
OneHotEncoding for categorical features
LabelEncoding for owner feature
Feature scaling using StandardScaler


📊 Model Used - 
Linear Regression. 
Model Performance - 
R² Score (Train): ~0.83
R² Score (Test): ~0.82
MAE: ~77,695
RMSE: ~106,605
The model shows good generalization with minimal overfitting.


🌐 Deployment - 
The model is deployed using Streamlit.
Users can input: 
Year, 
KM Driven,
Mileage,
Engine Capacity,
Seats,
Owner Type,
Brand,
Fuel Type,
Transmission,
Seller Type

AND GET PREDICTED CAR PRICE INSTANTLY..

To see The Working Demo: https://used-cars-price-prediction-afbdtk8x6ntnigcpvha5la.streamlit.app/
