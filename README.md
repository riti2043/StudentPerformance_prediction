## Student Performance Prediction
End-to-End Simple Machine Learning Web Application


## Software And Tools Requirements

- [Github Account]()
- [VS Code IDE]
- [RenderAccount]()
- [GitCLI]()

## Tech Stack

Python,Flask,scikit-learn,NumPy,Pandas,Pickle
,HTML / CSS,Gunicorn,Render

## Project Overview

This project implements an end-to-end machine learning pipeline to predict student academic performance using multivariate linear regression.

The primary objective of this project was to move a trained model from the notebook stage to a fully deployed web application. It was developed as a hands-on exercise to understand the complete lifecycle of a machine learning system — from data preparation and model training to serialization, backend integration, and cloud deployment.

The application enables real-time prediction of a student’s performance index based on key study-related inputs.

## Problem Statement

Academic performance can be influenced by measurable behavioral and academic factors. 

### The goal was to:

* Train a regression model on structured student data
* Evaluate its predictive performance
* Serialize the trained model
* Integrate it into a web application
* Deploy the application to a cloud platform

## Dataset Description

The dataset consists of 10,000 synthetic student records designed to simulate academic behavior patterns.

### Predictor Variables

* Hours Studied
* Previous Scores (percentage)
* Sleep Hours
* Sample Question Papers Practiced

### Target Variable

Performance Index (continuous variable ranging from 10 to 100)

The dataset is synthetic and created for illustrative and learning purposes.

## Machine Learning Pipeline

The model development process followed these stages (as implemented in the training notebook 
Stud_prediction.ipynb - Colab):

1.**Data Loading and Inspection** :The dataset was loaded using pandas and examined for structure, data types, and missing values. All selected numerical features were complete and required no imputation.

2.**Feature Selection**:
Four numerical predictors were selected-Hours Studied,Previous Scores,Sleep Hours
,Sample Question Papers Practiced
The target variable was defined as the Performance Index.

3.**Train-Test Split**:The dataset was split into training and testing sets using an 80–20 ratio with a fixed random state to ensure reproducibility.

4.**Model Training**:A multivariate Linear Regression model from scikit-learn was trained on the training dataset to learn the linear relationship between the selected predictors and the performance index.

5.**Model Evaluation**:Model performance was evaluated on the test dataset using regression metrics:
* Mean Absolute Error (MAE): 1.6297
* Mean Squared Error (MSE): 4.1823
* R-squared (R²): 0.9887
The high R² score indicates a strong linear relationship within this synthetic dataset.

6.**Model Serialization**: The trained model was serialized using pickle and saved as model.pkl, allowing it to be reused for inference within the Flask application.

## Backend Integration

The Flask application performs the following:
* Loads the serialized regression model at runtime
* Accepts user input through an HTML form
* Converts input values into a NumPy array
* Generates predictions using the trained model
* Returns the predicted performance score to the user interface
* Two routes are implemented:

/predict – Form-based prediction

/predict_api – JSON-based API endpoint

## Deployment

The application is deployed on Render and configured to run using Gunicorn as the production WSGI server.

