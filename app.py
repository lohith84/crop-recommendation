from flask import Flask, request, render_template
import numpy as np
import pickle
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

operate_folder = os.path.join(script_dir, 'operate')
os.chdir(operate_folder)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('standscaler.pkl', 'rb'))
minmax_scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def recommendation():
    if request.method == 'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['T'])
        humidity = float(request.form['H'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rain'])

        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        transformed_features = minmax_scaler.transform(features)
        transformed_features = scaler.transform(transformed_features)
        transformed_features = transformed_features.reshape(1, -1)

        prediction = model.predict(transformed_features)

        crop_ref = {
            1: 'rice', 2: 'maize', 3: 'chickpea', 4: 'kidneybeans', 5: 'pigeonpeas',
            6: 'mothbeans', 7: 'mungbean', 8: 'blackgram', 9: 'lentil', 10: 'pomegranate',
            11: 'banana', 12: 'mango', 13: 'grapes', 14: 'watermelon', 15: 'muskmelon',
            16: 'apple', 17: 'orange', 18: 'papaya', 19: 'coconut', 20: 'cotton',
            21: 'jute', 22: 'coffee'
        }

        prediction = max(1, min(prediction[0], 22))

        if prediction in crop_ref:
            recommended_crop = crop_ref[prediction]
            result = f"{recommended_crop}"
        else:
            result = "Sorry, we are not able to recommend a proper crop for this environment."

        return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
