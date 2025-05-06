import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('save_model/heart_disease_model.joblib')

st.title("❤ Heart Disease Prediction App")
st.write("Please enter the patient data below:")

# Collect user input
age = st.number_input('Age', min_value=1, max_value=120, value=30)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=250, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
restecg = st.selectbox('Resting ECG results', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', [0, 1])
oldpeak = st.number_input('ST depression', min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox('Slope of the peak exercise ST segment', [0, 1, 2])
ca = st.selectbox('Number of major vessels (0-3)', [0, 1, 2, 3])
thal = st.selectbox('Thalassemia', [1, 2, 3])

# Map input
sex = 1 if sex == 'Male' else 0

# Predict
if st.button('Predict'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('The patient is likely to have heart disease. 🚨')
    else:
        st.success('The patient is unlikely to have heart disease. ✅')