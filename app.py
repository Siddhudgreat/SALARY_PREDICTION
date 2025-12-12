import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("salary_model.pkl", "rb"))

st.title("💼 Salary Prediction using Linear Regression")
st.write("Enter your details to estimate annual salary:")

# Input fields
experience = st.number_input("Work Experience (Years)", 0, 40, 3)
skills = st.slider("Skills Rating (1–10)", 1, 10, 5)
qualification = st.selectbox("Qualification",
                             ["10th", "12th", "Graduate", "Post Graduate"])
age = st.number_input("Age", 18, 60, 25)
certifications = st.number_input("Number of Certifications", 0, 10, 1)
company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])

# Encode categorical inputs
qualification_map = {"10th": 1, "12th": 2, "Graduate": 3, "Post Graduate": 4}
company_map = {"Small": 1, "Medium": 2, "Large": 3}

q_val = qualification_map[qualification]
c_val = company_map[company_size]

# Prediction
if st.button("Predict Salary"):
    input_data = np.array([[experience, skills, q_val, age, certifications, c_val]])
    predicted_salary = model.predict(input_data)[0]

    st.subheader("📌 Estimated Salary:")
    st.success(f"₹ {int(predicted_salary):,} per year")
