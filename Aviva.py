


# Needed libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import streamlit as st
import pickle as pk



# Load the trained pipeline
model = pk.load(open('gbr_pipeline.pkl','rb'))

# App Title
st.title("Aviva Insurance Charges Prediction App")
st.write("This app predicts insurance charges based on user inputs using a trained Gradient Boosting Regressor pipeline.")

# User Inputs
st.header("Enter Customer Details")

# Numerical Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=100.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=0)

# Categorical Inputs
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Convert user inputs to a DataFrame
user_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

# Predict Charges
if st.button("Predict Insurance Charges"):
    try:
        prediction = model.predict(user_data)[0]
        st.success(f"Predicted Insurance Charges: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")