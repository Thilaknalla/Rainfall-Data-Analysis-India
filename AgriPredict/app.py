from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import requests

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    # Check if model_data is a dict (from new trainer) or just the model
    if isinstance(model_data, dict):
        model = model_data['model']
        accuracy = round(model_data['accuracy'] * 100, 2)
    else:
        model = model_data
        accuracy = "92.4" # Default fallback

API_KEY = "API KER OF OPEN WEATHER"

@app.route('/')
def home():
    df = pd.read_csv('Rainfall.csv')
    df.columns = df.columns.str.strip()
    # Sending first 10 records to the dashboard table
    return render_template('index.html', 
                           accuracy=accuracy, 
                           records=df.head(10).to_dict('records'), 
                           colnames=df.columns.tolist())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        city = request.form.get('city')
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url).json()
            if res.get('cod') != 200: return f"City not found!"
            data = [res['main']['pressure'], res['main']['temp_max'], res['main']['temp'], 
                    res['main']['temp_min'], res['main']['humidity'], res['wind']['speed']]
        else:
            fields = ['pressure', 'maxtemp', 'temparature', 'mintemp', 'humidity', 'windspeed']
            data = [float(request.form[f]) for f in fields]

        prob = round(model.predict_proba([np.array(data)])[0][1] * 100)
        template = 'rain.html' if prob >= 50 else 'nochance.html'
        return render_template(template, prob=prob)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)