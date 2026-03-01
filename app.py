import joblib
from flask import Flask,request,app,jsonify,url_for,render_template,redirect,flash,session
import numpy as np
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

if __name__=='__main__':
    app.run(debug=True)
