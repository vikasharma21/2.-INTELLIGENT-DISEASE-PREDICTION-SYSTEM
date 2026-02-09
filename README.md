# Major-Project
HealthMate is a machine learning-based web application designed to predict the risk of Diabetes, Heart Disease, and Parkinson’s Disease using medical datasets and smart algorithms. Built with Streamlit, it offers real-time predictions and personalized diet &amp; workout plans based on user input 

# 🩺 HealthMate: Intelligent Disease Prediction and Diet Recommender

## 🔍 Project Overview

**HealthMate** is an intelligent Streamlit web application that allows users to predict their likelihood of having one of the following diseases:

- 🩸 Diabetes
- ❤️ Heart Disease
- 🧠 Parkinson’s Disease

Each prediction is backed by machine learning models trained on medical datasets, and the app also provides **customized diet and lifestyle recommendations** based on the result.

---

## 🧠 How It Works

This project has two main components:

### 1. 🧪 Model Development (Jupyter Notebooks)
Each disease has a dedicated notebook where the following steps are carried out:

#### ✅ Steps Followed:
1. **Importing Libraries**  
   Tools: `numpy`, `pandas`, `matplotlib`, `seaborn`, `sklearn`, etc.

2. **Loading the Dataset**  
   Using datasets like Pima Indians Diabetes, Heart Disease UCI, and Parkinson’s voice data.

3. **Exploratory Data Analysis (EDA)**  
   - Summary stats and data types  
   - Missing values  
   - Correlation heatmaps  
   - Visualizations

4. **Data Preprocessing**  
   - Replacing zeros/missing values  
   - Feature scaling (e.g., `StandardScaler`)  
   - Train-test split

5. **Model Training & Comparison**  
   - For **Diabetes**: Logistic Regression, KNN, SVM, Decision Tree, Random Forest  
   - For **Heart Disease**: Decision Tree, Random Forest (incl. Scratch & Improved), Gradient Boosting, XGBoost  
   - For **Parkinson’s**: MLP (Sklearn), Neural Network (Scratch + PyTorch)

6. **Evaluation Metrics**
   - Accuracy, Confusion Matrix, Classification Report

7. **Model Selection**
   - Best performing model saved for deployment using `pickle`.

---

### 2. 🌐 Streamlit Web App

The `app.py` script is a Streamlit dashboard with the following features:

#### 🎯 Functionalities:
- User-friendly input forms for health metrics.
- Real-time predictions using trained models.
- Instant diagnosis result (e.g., "The person is diabetic").
- 💡 **Personalized diet and workout plans** based on:
  - Disease
  - Gender
  - Vegetarian / Non-Vegetarian preference

#### 📦 Models are loaded from:




📊 Future Improvements:
- Add more diseases like liver disease, kidney disease, etc.
- Integrate visual analytics for feature importance.
- Add user login and history tracking.
- Deploy on cloud (e.g., Streamlit Cloud, Heroku, etc.)
