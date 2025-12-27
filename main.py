import streamlit as st
from prediction_helper import predict

st.title("Lauki Finance: Credit Risk Modelling")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with row1[1]:
    income = st.number_input("Income", min_value=1000, max_value=10000000, step=1000)
with row1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=1000, max_value=10000000, step=1000)

with row2[0]:
    loan_tenure = st.number_input("Loan Tenure (months)", min_value=6, max_value=360, step=1)
with row2[1]:
    avg_dpd = st.number_input("Average DPD (Days Past Due)", min_value=0, max_value=1000, step=1)
with row2[2]:
    delinquency_ratio = st.number_input("Delinquency Ratio", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")

with row3[0]:
    credit_utilization = st.number_input("Credit Utilization Ratio", min_value=0.0, max_value=1.0, step=0.01,
                                         format="%.2f")
with row3[1]:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, step=1)
with row3[2]:
    num_credit_inquiries = st.number_input("Number of Credit Inquiries", min_value=0, max_value=100, step=1)

with row4[0]:
    employment_years = st.number_input("Years of Employment", min_value=0, max_value=50, step=1)

if st.button("Predict Credit Risk"):
    result = predict(age, income, loan_amount, loan_tenure, avg_dpd, delinquency_ratio,
                     credit_utilization, credit_score, num_credit_inquiries, employment_years)

    st.success(f"Credit Risk Prediction: {result}")
