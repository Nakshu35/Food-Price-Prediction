from flask import Flask,request,jsonify,render_template
import pandas as pd 
import numpy as np 
import xgboost as xgb
import pickle
import traceback

app = Flask(__name__)

XGB_model = pickle.load(open('Models/xgb_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'POST':
            state = float(request.form.get('statet'))
            district = float(request.form.get('districtt'))
            market = float(request.form.get('markett'))
            category = float(request.form.get('categoryt'))
            commodity = float(request.form.get('commodityt'))
            unit = float(request.form.get('unitt'))
            pricetype = float(request.form.get('pricetypet'))
            Year = float(request.form.get('year'))
            Month = float(request.form.get('month'))
            Day = float(request.form.get('day'))

            new_data_points = np.array([[state, district, market, category, commodity, unit, pricetype, Year, Month, Day]])
            result = XGB_model.predict(new_data_points)
            result[0] = round(result[0], 2)

            return str(result[0])
        else:
            return render_template('index.html')
    
    except Exception as e:
        print("ERROR:", str(e))
        print(traceback.format_exc())  # Print full error traceback
        return "Internal Server Error: " + str(e), 500
            
        


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0")
