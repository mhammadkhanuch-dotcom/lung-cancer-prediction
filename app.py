
import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Page Title
st.set_page_config(page_title="Lung Cancer Prediction", page_icon="🫁")

st.title("🫁 Lung Cancer Prediction System")
st.write("Enter the patient details below.")

# Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
gender = 1 if gender == "Male" else 0

age = st.number_input("Age", min_value=1, max_value=120, value=40)

smoking = st.selectbox("Smoking", [1, 2])
yellow_fingers = st.selectbox("Yellow Fingers", [1, 2])
anxiety = st.selectbox("Anxiety", [1, 2])
peer_pressure = st.selectbox("Peer Pressure", [1, 2])
chronic_disease = st.selectbox("Chronic Disease", [1, 2])
fatigue = st.selectbox("Fatigue", [1, 2])
allergy = st.selectbox("Allergy", [1, 2])
wheezing = st.selectbox("Wheezing", [1, 2])
alcohol = st.selectbox("Alcohol Consuming", [1, 2])
coughing = st.selectbox("Coughing", [1, 2])
shortness_breath = st.selectbox("Shortness of Breath", [1, 2])
swallowing = st.selectbox("Swallowing Difficulty", [1, 2])
chest_pain = st.selectbox("Chest Pain", [1, 2])

# Prediction
if st.button("Predict"):

    features = np.array([[gender, age, smoking, yellow_fingers,
                          anxiety, peer_pressure, chronic_disease,
                          fatigue, allergy, wheezing, alcohol,
                          coughing, shortness_breath,
                          swallowing, chest_pain]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Lung Cancer")
    else:
        st.success("✅ Low Risk of Lung Cancer")
