# 🚗 Car Price Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Machine_Learning-Linear_Regression-green?style=for-the-badge" alt="ML">
  <img src="https://img.shields.io/badge/Deployed_On-Render-brightgreen?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</p>

---

### 🌐 Live Web App
Aap is web application ko live yahan check kar sakte hain:  
🔗 **[https://car-price-predictor-p8hf.onrender.com/](https://car-price-predictor-p8hf.onrender.com/)**

---

## 📌 Project Overview
Yeh project ek complete **End-to-End Machine Learning** web application hai. Isme raw dataset ko clean karke ek `LinearRegression` model train kiya gya hai. Frontend ko ek premium aur responsive design diya gaya hai aur backend ko Flask framework ka use karke Render cloud server par safely deploy kiya gaya hai.

## ⚡ Features & Functionalities
* 🔄 **Dynamic Dropdowns:** Kaun si company select hui hai, uske hisab se car ke models automatic update hote hain.
* 🛠️ **Robust Input Pipeline:** User jo bhi data form me bharta hai, backend use automatic DataFrame me badal kar model tak bhejta hai.
* 📱 **Responsive UI:** Minimalistic aur premium design jo desktop aur mobile dono par mast chalta hai.
* 🛡️ **Error Tolerant:** Backend me safeguards lage hain taaki galat input se server crash na ho.

---

## 🛠️ Tech Stack Used

| Technology | Role / Usage | Icon |
| :--- | :--- | :---: |
| **Python** | Core Language | <img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white" height="20"> |
| **Flask** | Backend Web Framework | <img src="https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask&logoColor=white" height="20"> |
| **Pandas** | Data Cleaning & Manipulation | <img src="https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white" height="20"> |
| **Scikit-Learn** | ML Model Training & Pipeline | <img src="https://img.shields.io/badge/-Scikit_Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" height="20"> |
| **Render** | Cloud Hosting & Deployment | <img src="https://img.shields.io/badge/-Render-46E3B7?style=flat&logo=render&logoColor=white" height="20"> |

---

## 📊 Dataset Features
Model predictions ke liye in main features ka use kiya jata hai:

* 🚘 **name:** Car model ka full name (e.g., Maruti Suzuki Swift)
* 🏢 **company:** Car manufacturing brand/company name (e.g., Maruti)
* 📅 **year:** Car ka manufacturing/purchase year
* 🛣️ **kms_driven:** Total kilometers the car has traveled
* ⛽ **fuel_type:** Engine ka fuel type (Petrol / Diesel / LPG)

---

## 🏗️ Project Structure
```bash
car-price-predictor/
│
├── 📂 templates/
│   └── 📄 index.html               # Frontend User Interface (UI Design)
│
├── 🐍 app.py                       # Main Flask Backend Router & Prediction Logic
├── 📊 cleaned_car.csv              # Fully Cleaned Dataset used for baseline validation
├── 📦 LinearRegressionModel.pkl    # Serialized Trained Machine Learning Model Weights
├── ⚙️ Procfile                     # Production WSGI process manager command for Render
└── 📄 requirements.txt             # Python Package Dependencies List
