# ❤️ Heart Disease Prediction System using Machine Learning

An end-to-end Machine Learning-based Heart Disease Prediction system developed as a Final Year Project for the degree of BS Mathematics at COMSATS University Islamabad.

This project uses real-world clinical data to predict the presence of heart disease using advanced machine learning techniques and provides real-time predictions through a Flask-based web application.

---

## 📌 Project Overview

Heart disease remains one of the leading causes of mortality worldwide. Early detection plays a critical role in reducing health risks and improving treatment outcomes.

The primary objective of this project is to develop a complete machine learning pipeline that:

- Performs data preprocessing and exploratory data analysis (EDA)
- Trains and evaluates multiple machine learning models
- Selects the best-performing model based on performance metrics
- Deploys the trained model through a Flask-based web application
- Provides real-time predictions based on clinical input features

This project demonstrates both analytical modeling and practical deployment skills.

---

## 📊 Dataset Information

- Publicly available Heart Disease dataset
- 1025 patient records
- 13 clinical input attributes
- Binary classification problem:
  - `1` → Heart Disease Present
  - `0` → No Heart Disease

### 🧾 Input Features Used

| Feature | Description |
|---------|-------------|
| age | Age of patient (years) |
| sex | Gender (0 = Female, 1 = Male) |
| cp | Chest Pain Type |
| trestbps | Resting Blood Pressure (mm Hg) |
| chol | Serum Cholesterol (mg/dl) |
| fbs | Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No) |
| restecg | Resting ECG Results |
| thalach | Maximum Heart Rate Achieved |
| exang | Exercise Induced Angina (1 = Yes, 0 = No) |
| oldpeak | ST Depression induced by exercise |
| slope | Slope of Peak Exercise ST Segment |
| ca | Number of Major Vessels (0–3) |
| thal | Thalassemia Type |

---

## 🧠 Machine Learning Models Implemented

The following classification models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Neural Network (MLP)
- **XGBoost (Selected Final Model)**

---

## 🏆 Final Model Selection: XGBoost

XGBoost (Extreme Gradient Boosting) was selected as the final model because:

- It achieved the highest test accuracy
- It maintained a strong balance between precision and recall
- It handled feature interactions effectively
- It provided better generalization compared to other models

The trained model was saved using Joblib and integrated into the Flask application.

---

## 📈 Model Evaluation Metrics

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics ensure reliable and interpretable performance evaluation.

---

## ⚙️ Technologies & Tools Used

- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Matplotlib & Seaborn
- Flask
- Joblib
- Google Colab (Model Training)
- Visual Studio Code (Deployment)
---

## 🌐 Web Application (Flask Deployment)

The trained XGBoost model is deployed through a Flask web application that:

- Accepts 13 medical input features from the user
- Converts form data into structured format
- Passes input into the trained ML model
- Generates real-time prediction
- Displays user-friendly risk result

This demonstrates full-stack integration of machine learning with web technologies.

---

## 📂 Project Structure
