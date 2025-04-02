import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model = joblib.load('loan.joblib')
Gender = st.number_input('Enter Gender Male:0 Female:1')
Married = st.number_input('Enter Martial status Married:1 Unmarried:0')
Income = st.number_input('Enter applicant income in thounsands')
LA = st.number_input('Enter Loan Amount in thounsands')
if st.button('Predict Approval'):
    Prediction = model.predict([[Gender,Married,Income,LA]])
    if Prediction == 'Y':
        st.text('Loan Approved')
    else:
        st.text('Loan Rejected')
