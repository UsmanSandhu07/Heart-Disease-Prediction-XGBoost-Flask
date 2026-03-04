from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model from current directory
MODEL_PATH = os.path.join(os.path.dirname(__file__), "xgb_boost.joblib")
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    result_text = None

    if request.method == "POST":
        try:
            # Collect input data from form
            data = {
                "age": float(request.form["age"]),
                "sex": float(request.form["sex"]),
                "cp": float(request.form["cp"]),
                "trestbps": float(request.form["trestbps"]),
                "chol": float(request.form["chol"]),
                "fbs": float(request.form["fbs"]),
                "restecg": float(request.form["restecg"]),
                "thalach": float(request.form["thalach"]),
                "exang": float(request.form["exang"]),
                "oldpeak": float(request.form["oldpeak"]),
                "slope": float(request.form["slope"]),
                "ca": float(request.form["ca"]),
                "thal": float(request.form["thal"])
            }

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # Make prediction
            prediction = int(model.predict(df)[0])

            # Convert prediction to readable text
            if prediction == 1:
                result_text = "Heart Disease Detected"
            else:
                result_text = "No Heart Disease Detected"

        except Exception as e:
            result_text = f"Error: {str(e)}"

    return render_template("index.html", prediction=result_text)


if __name__ == "__main__":
    app.run(debug=True)
