import streamlit as st
import pandas as pd
import joblib



st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction System")
st.write("Enter patient details below.")



model = joblib.load("Disease_Prediction_RFC_model1.pkl")

st.divider()


age = st.number_input("Age", 18, 80, 30)

gender = st.selectbox("Gender", ["Male", "Female")

bmi = st.number_input("BMI", 10.0, 50.0, 25.0)

glucose = st.number_input("Glucose", 50.0, 300.0, 120.0)

blood_pressure = st.number_input("Blood Pressure", 80, 250, 120)

cholesterol = st.number_input("Cholesterol", 100, 350, 200)

insulin = st.number_input("Insulin", 0, 300, 100)

hba1c = st.number_input("HbA1c", 2.0, 15.0, 6.0)

smoking = st.selectbox(
    "Smoking Status",
    ["Current", "Never", "Former"]
)

activity = st.selectbox(
    "Physical Activity",
    ["Low", "Moderate", "High"]
)

family = st.selectbox(
    "Family History",
    ["No", "Yes"]
)



gender = {"Male": 1, "Female": 0}[gender]

smoking = {
    "Current": 0,
    "Never": 1,
    "Former": 2
}[smoking]

activity = {
    "Low": 0,
    "Moderate": 1,
    "High": 2
}[activity]

family = {
    "No": 0,
    "Yes": 1
}[family]


st.divider()

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age":[age],
        "Gender":[gender],
        "BMI":[bmi],
        "Glucose":[glucose],
        "Blood_Pressure":[blood_pressure],
        "Cholesterol":[cholesterol],
        "Insulin":[insulin],
        "HbA1c":[hba1c],
        "Smoking_Status":[smoking],
        "Physical_Activity":[activity],
        "Family_History":[family]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Diabetes")
        st.write(f"Probability : **{probability[1]*100:.2f}%**")
    else:
        st.success("✅ No Diabetes Detected")
        st.write(f"Probability : **{probability[0]*100:.2f}%**")
