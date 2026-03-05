
import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('knn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit input interface
st.title("Heart Disease Risk Predictor")

glucose = st.number_input("Glucose", 0.0, 300.0, step=1.0)
insulin = st.number_input("Insulin", 0.0, 900.0, step=1.0)
bmi = st.number_input("BMI", 0.0, 60.0, step=0.1)
age = st.number_input("Age", 1, 120, step=1)

if st.button("Predict Risk Level"):
    input_data = np.array([[glucose, insulin, bmi, age]])
    scaled_input = scaler.transform(input_data)
    prob = model.predict_proba(scaled_input)[0][1]

    if prob < 0.33:
        risk = "Low Risk"
    elif prob < 0.66:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    st.write(f"Predicted Risk Level: **{risk}** (Probability: {prob:.2f})")
