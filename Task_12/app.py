from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler from model folder
with open("../Task_11/model/diabetes_classifier.pkl", "rb") as f:
    model = pickle.load(f)
with open("../Task_11/model/feature_normalizer.pkl", "rb") as f:
    scaler = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    features = [
        float(request.form["pregnancies"]),
        float(request.form["glucose"]),
        float(request.form["blood_pressure"]),
        float(request.form["skin_thickness"]),
        float(request.form["insulin"]),
        float(request.form["bmi"]),
        float(request.form["diabetes_pedigree"]),
        float(request.form["age"]),
    ]

    # Scale features
    features_scaled = scaler.transform([features])

    # Make prediction
    prediction = model.predict(features_scaled)[0]

    # Interpret result
    result = "High Risk" if prediction == 1 else "Low Risk"

    return render_template("index.html", prediction=result, features=features)


if __name__ == "__main__":
    app.run(debug=True)
