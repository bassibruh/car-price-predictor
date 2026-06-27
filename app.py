from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# Current project folder path automatic detect karne ke liye
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load cleaned dataset
car = pd.read_csv(os.path.join(BASE_DIR, "cleaned_car.csv"))

# Load trained model
with open(os.path.join(BASE_DIR, "LinearRegressionModel.pkl"), "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    companies = sorted(car["company"].unique())
    car_models = sorted(car["name"].unique())
    years = sorted(car["year"].unique(), reverse=True)
    fuel_types = sorted(car["fuel_type"].dropna().unique())

    return render_template(
        "index.html",
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types,
    )


@app.route("/predict", methods=["POST"])
def predict():

    company = request.form.get("company")
    car_model = request.form.get("car_models")
    year = int(request.form.get("year"))
    fuel_type = request.form.get("fuel_type")
    kms_driven = int(request.form.get("kilo_driven"))

    data = pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=["name", "company", "year", "kms_driven", "fuel_type"],
    )

    prediction = model.predict(data)

    return str(round(prediction[0], 2))


if __name__ == "__main__":
    app.run(debug=True, port=8000)