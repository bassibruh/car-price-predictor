# 🚗 Car Price Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Machine_Learning-Linear_Regression-green?style=for-the-badge" alt="ML">
  <img src="https://img.shields.io/badge/Deployed_On-Render-brightgreen?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</p>

---

### 🌐 Live Web Application
You can access the live, fully-functional web application here:  
🔗 **[https://car-price-predictor-p8hf.onrender.com/](https://car-price-predictor-p8hf.onrender.com/)**

---

## 📌 Project Overview
The **Car Price Predictor** is a complete end-to-end Machine Learning web application designed to estimate the resale value of used cars. The core machine learning engine utilizes a `LinearRegression` algorithm combined with a `OneHotEncoder` preprocessing pipeline to seamlessly handle categorical data. The backend is powered by Flask, and the entire application is securely hosted and running in production on the Render cloud platform.

## ⚡ Features & Functionalities
* 🔄 **Dynamic Dependent Dropdowns:** The frontend intelligently syncs inputs; selecting a specific car company automatically updates and filters the corresponding car models in real-time.
* 🛠️ **Robust Input Pipeline:** Safely captures dynamic form inputs from the user, restructuring them into a structured Pandas DataFrame mapped perfectly to the pre-trained model's layout.
* 📱 **Responsive UI/UX:** Built with a clean, modern, and fully interactive interface optimized beautifully for both mobile browsers and desktop monitors.
* 🛡️ **Fault Tolerant Architecture:** Embedded with backend exceptions and fallback routines to ensure the production server never crashes on missing payloads or uneven model configurations.

---

## 🛠️ Tech Stack Used

| Technology / Tool | Role / Core Usage | Badge |
| :--- | :--- | :---: |
| **Python** | Core Programming Language | <img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white" height="20"> |
| **Flask** | Backend Web Routing Framework | <img src="https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask&logoColor=white" height="20"> |
| **Pandas** | Data Cleaning, Wrangling & Engineering | <img src="https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white" height="20"> |
| **Scikit-Learn** | ML Pipeline Construction & Model Weights | <img src="https://img.shields.io/badge/-Scikit_Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" height="20"> |
| **Render** | Cloud Production Hosting Server | <img src="https://img.shields.io/badge/-Render-46E3B7?style=flat&logo=render&logoColor=white" height="20"> |

---

## 📊 Dataset Features
The model actively evaluates predictions based on the following key engineering parameters:

* 🚘 **name:** Complete structural name of the car model (e.g., Maruti Suzuki Swift)
* 🏢 **company:** The manufacturing automotive brand (e.g., Maruti, Hyundai, Toyota)
* 📅 **year:** The release/purchase year of the automobile
* 🛣️ **kms_driven:** Total historical odometer distance covered by the vehicle in kilometers
* ⛽ **fuel_type:** The mechanical engine fuel configuration (Petrol / Diesel / LPG)

---

## 🏗️ Project Structure
```bash
car-price-predictor/
│
├── 📂 templates/
│   └── 📄 index.html               # Frontend User Interface layout & dynamic scripting
│
├── 🐍 app.py                       # Core Flask Application router & prediction pipeline
├── 📊 cleaned_car.csv              # Post-processed dataset utilized for baseline checks
├── 📦 LinearRegressionModel.pkl    # Serialized trained Scikit-Learn machine learning weights
├── ⚙️ Procfile                     # WSGI process manager instruction layout for Render
└── 📄 requirements.txt             # Mandatory environment package dependency list
