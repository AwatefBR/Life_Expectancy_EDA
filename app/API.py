from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('path/to/your/model.pkl')

# Render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Prediction API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = extract_features(data)  # Implement a function to extract features from input data
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)