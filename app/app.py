from flask import render_template, request, jsonify
from sklearn.externals import joblib
from app import app

# Load your trained model
model = joblib.load('model/your_model.pkl')

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