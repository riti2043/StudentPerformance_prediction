import joblib
from flask import Flask,request,app,jsonify,url_for,render_template,redirect,flash,session
import numpy as np
import matplotlib.pyplot as plt
import os
from markupsafe import escape
import pandas as pd

app=Flask(__name__)
# LOad the model
regmodel=joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data= np.array(list(data.values())).reshape(1,-1)
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=np.array(data).reshape(1,-1)
    prediction=regmodel.predict(final_input)[0]
    # Clamp prediction within dataset bounds
    prediction = max(10, min(100, prediction))

    previous_score = data[1]


    return render_template(
        'home.html',
        prediction_text=f"The predicted performance in the exam is {prediction:.2f}",
        graph_url='prediction.png'
    )
if __name__=='__main__':
    app.run()


