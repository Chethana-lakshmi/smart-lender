import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("loan_prediction_model.pkl")

st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide"
)

# Sidebar
st.sidebar.title("🏦 Loan Prediction System")
st.sidebar.markdown("""
### Project Details

**Algorithm Used**
- Random Forest

**Dataset**
- Loan Prediction Dataset

**Developed Using**
- Python
- Streamlit
- Scikit-learn
- XGBoost

---

Enter applicant details and click **Predict Loan Status**.
""")

# Title
st.title("🏦 Loan Prediction System")
st.write("Predict whether a loan application is likely to be approved.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    married = st.selectbox("Married", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    applicant_income = st.number_input("Applicant Income", 0, value=5000)

with col2:
    coapplicant_income = st.number_input("Coapplicant Income", 0, value=0)
    loan_amount = st.number_input("Loan Amount", 0, value=120)
    loan_term = st.number_input("Loan Amount Term", 0, value=360)
    credit_history = st.selectbox("Credit History", [1, 0])
    property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Encoding
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0

dependents = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}[dependents]

education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0

property_area = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}[property_area]

st.divider()

if st.button("Predict Loan Status", use_container_width=True):

    input_data = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    confidence = np.max(probability) * 100

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.metric("Prediction Confidence", f"{confidence:.2f}%")