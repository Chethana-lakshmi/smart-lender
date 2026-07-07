# Loan Prediction System

## Project Overview

The Loan Prediction System is a Machine Learning application that predicts whether a loan application is likely to be approved based on applicant information such as income, education, credit history, and property area.

This project helps financial institutions make faster and more consistent loan approval decisions.

---

## Objectives

- Predict loan approval status.
- Analyze applicant information.
- Compare Random Forest and XGBoost models.
- Deploy the model using Streamlit.

---

## Dataset

The dataset contains 614 loan application records with 13 attributes.

### Features

- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

### Target

- Loan_Status

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Missing Value Handling
4. Label Encoding
5. Exploratory Data Analysis
6. Train-Test Split
7. Random Forest Training
8. XGBoost Training
9. Model Evaluation
10. Deployment

---

## Algorithms Used

### Random Forest

A supervised ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy.

### XGBoost

A gradient boosting algorithm that builds trees sequentially to improve predictive performance.

---

## Model Performance

Random Forest Accuracy: **75.61%**

XGBoost Accuracy: **75.61%**

---

## Project Structure

Loan_Prediction_Project/

├── dataset/

│ └── loan_prediction.csv

├── loan_prediction.ipynb

├── loan_prediction_model.pkl

├── app.py

├── requirements.txt

└── README.md

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

- Hyperparameter tuning
- Better feature engineering
- User authentication
- Database integration
- Cloud deployment

---

## Author

Name: Your Name

College: Vignan's Lara Institute of Technology and Science

Project: SmartBridge Internship Project