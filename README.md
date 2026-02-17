# Rainfall-Data-Analysis-India
Exploratory Data Analysis of Indian rainfall data to understand seasonal patterns, trends, and their impact on agriculture using data visualization and statistical techniques.

AgriPredict is a simple decision-support system for farmers that predicts the chance of rainfall using Machine Learning.It uses a Random Forest Classifier trained on historical weather data. The system can also fetch live weather data using the OpenWeather API to give instant rain predictions for any city.The dashboard is designed to be simple and farmer-friendly. It includes:

-->One-click city-based prediction

-->Manual weather data input

-->Data visualization

-->Temperature trend graphs

-->Clear result pages with farming suggestions

How It Works

1.Train the Model (train_model.py)
--Load and clean rainfall data
--Convert rainfall into binary (1 = rain, 0 = no rain)
--Train Random Forest model
--Save model as model.pkl

2.Generate Charts (data_analysis.py)
--Create gauge charts and temperature trend graphs
--Save images for dashboard display

3.Run the Flask App (app.py)
--Loads trained model
--Accepts city input (OpenWeather API) or manual data
--Predicts rainfall probability
--Shows result page (Rain / No Rain)

-->Technologies Used
Python
Flask
Scikit-learn
Pandas
Matplotlib
HTML & CSS
OpenWeather API

-->Goal
~To help farmers make better agricultural decisions using AI-based rainfall prediction in a simple and easy-to-understand way.
~Results Pages: rain.html includes a dynamic progress circle gauge and farmer guidelines (e.g., "Protect harvested crops").
