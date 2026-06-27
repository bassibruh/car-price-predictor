# 🚗 Car Price Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Machine_Learning-Linear_Regression-green?style=for-the-badge" alt="ML">
  <img src="https://img.shields.io/badge/R²_Score-0.899-success?style=for-the-badge" alt="R2">
  <img src="https://img.shields.io/badge/Deployed_On-Render-brightgreen?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</p>

---

### 🌐 Live Web Application
You can access the live, fully-functional web application here:  
🔗 **[https://car-price-predictor-p8hf.onrender.com/](https://car-price-predictor-p8hf.onrender.com/)**

---

## 📌 Project Overview
The **Car Price Predictor** is a complete end-to-end Machine Learning web application designed to estimate the resale value of used cars. The core machine learning engine utilizes a `LinearRegression` algorithm combined with a `OneHotEncoder` preprocessing pipeline to seamlessly handle categorical data. The backend is powered by Flask, and the entire application is securely hosted and running in production on the Render cloud platform.

---

## ⚡ Features & Functionalities
* 🔄 **Dynamic Dependent Dropdowns:** The frontend intelligently syncs inputs; selecting a specific car company automatically updates and filters the corresponding car models in real-time.
* 🛠️ **Robust Input Pipeline:** Safely captures dynamic form inputs from the user, restructuring them into a structured Pandas DataFrame mapped perfectly to the pre-trained model's layout.
* 📱 **Responsive UI/UX:** Built with a clean, modern, and fully interactive interface optimized beautifully for both mobile browsers and desktop monitors.
* 🛡️ **Fault Tolerant Architecture:** Embedded with backend exceptions and fallback routines to ensure the production server never crashes on missing payloads or uneven model configurations.

---

## 🧠 How It Works

```
Raw Input (User Form)
        │
        ▼
┌───────────────────┐
│  OneHotEncoder    │  ← Encodes: name, company, fuel_type
└───────────────────┘
        │
        ▼
┌───────────────────┐
│ LinearRegression  │  ← Trained on 90% of cleaned Quikr dataset
└───────────────────┘
        │
        ▼
 Predicted Car Price (₹)
```

1. **Data Cleaning** — Removed non-numeric years, prices tagged "Ask For Price", and null fuel types. Standardized `kms_driven` and trimmed car names to first 3 words.
2. **Preprocessing** — `OneHotEncoder` handles categorical columns (`name`, `company`, `fuel_type`); numerical features passed through directly.
3. **Model Training** — `LinearRegression` pipeline trained over **1000 random train-test splits** to find the optimal split (best `random_state`), ensuring the most generalizable weights.
4. **Serialization** — Final pipeline pickled via `pickle` and served live through Flask on Render.

---

## 📈 Model Performance

| Metric | Value |
| :--- | :--- |
| **Algorithm** | Linear Regression |
| **R² Score (Best Split)** | **0.899** (~90% accuracy) |
| **Training Strategy** | Best of 1000 random train-test splits |
| **Test Size** | 10% of cleaned dataset |
| **Encoding** | OneHotEncoder (name, company, fuel_type) |

> The model was trained across **1000 random states** and the split yielding the highest R² score (`0.8991`) was selected — ensuring robust and generalizable predictions.

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

## 📊 Dataset

| Property | Details |
| :--- | :--- |
| **Source** | [Quikr Used Cars Dataset — Kaggle]([https://www.kaggle.com/datasets/manishkr1754/quikr-used-car-dat](https://github.com/bassibruh/car-price-predictor/blob/main/quikr_car.csv)) |
| **Raw Records** | ~825 entries |
| **After Cleaning** | ~816 usable records |
| **Target Variable** | `Price` (INR) |

**Features used for prediction:**

| Feature | Description |
|:---|:---|
| `name` | Full model name of the car (e.g., Maruti Suzuki Swift) |
| `company` | Manufacturing brand (e.g., Maruti, Hyundai) |
| `year` | Year of purchase/manufacture |
| `kms_driven` | Total kilometers driven |
| `fuel_type` | Petrol / Diesel / LPG |

---

## 🏗️ Project Structure

```bash
car-price-predictor/
│
├── 📂 templates/
│   └── 📄 index.html               # Frontend UI layout & dynamic dropdown scripting
│
├── 🐍 app.py                       # Core Flask router & prediction pipeline
├── 📓 quickr_car_price_predictor.ipynb  # Data cleaning, EDA & model training notebook
├── 📊 cleaned_car.csv              # Post-processed dataset
├── 📦 LinearRegressionModel.pkl    # Serialized trained Scikit-Learn pipeline
├── ⚙️ Procfile                     # WSGI process config for Render deployment
└── 📄 requirements.txt             # Python package dependencies
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the Flask server
python app.py
```

Then open your browser and go to: `http://localhost:5000`

---

## 🔮 Future Improvements

- [ ] Upgrade to **Random Forest / XGBoost** for better non-linear predictions
- [ ] Add **more features** — transmission type, number of owners, car color
- [ ] Implement **confidence intervals** alongside price prediction
- [ ] Add **EDA dashboard** to visualize price trends by brand and year

---

## 👨‍💻 Author

**Aditya**  
BCA Final Year | IIMT University, Meerut  
📊 Aspiring Data Analyst | SQL • Python • Power BI • Excel

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/aditya-singh-8a0a2a35b)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/bassibruh)

---


