from flask import Flask, render_template, request
from numpy import loadtxt
from keras.models import model_from_json
import numpy as np

# Load the model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights("model.weights.h5")

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    input_data = [
        float(request.form['pregnancies']),
        float(request.form['glucose']),
        float(request.form['blood_pressure']),
        float(request.form['skin_thickness']),
        float(request.form['insulin']),
        float(request.form['bmi']),
        float(request.form['diabetes_pedigree']),
        float(request.form['age'])
    ]

    # Convert input data to numpy array and reshape for prediction
    input_array = np.array(input_data).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_array)
    predicted_class = (prediction > 0.5).astype(int)

    # Return the result
    return render_template('index.html', prediction=predicted_class[0][0])

if __name__ == '__main__':
    app.run(debug=True)