# AgriPredict: Indian Rainfall Analysis & Prediction System

### 🏆 SmartBridge Internship Project
**Team ID:** LTVIP2026TMIDS88309 <br>
**Team Lead:** [Thilak Nalla]  
**Team Members:**  Thilak Nalla, P Sai Govind, Khandavilli Jagadeesh Sai Kalyan, Krishna Manohar Mahalakshmi Varma Sangani, Yogi Venkata Naga Balaji Ankala.

---

## 🚀 Project Overview
**AgriPredict** is an AI-driven decision-support system designed to help Indian farmers mitigate weather-related risks. By performing **Exploratory Data Analysis (EDA)** on historical Indian rainfall data and utilizing **Machine Learning**, the system provides real-time rain forecasts and actionable agricultural suggestions.

The goal is to bridge the gap between complex meteorological data and practical farming needs through a simple, farmer-friendly dashboard.

## ✨ Key Features
*   **One-Click Prediction:** Enter a city name to fetch live weather via [OpenWeather API](https://openweathermap.org).
*   **Manual Input:** Option to manually enter weather parameters (Humidity, Temperature, etc.).
*   **Machine Learning Core:** Powered by a **Random Forest Classifier** for high-accuracy binary classification.
*   **Visual Analytics:** Dynamic gauge charts and temperature trend graphs.
*   **Farmer Guidelines:** Targeted advice (e.g., "Protect harvested crops") based on prediction results.

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Web Framework:** [Flask](https://flask.palletsprojects.com)
*   **Machine Learning:** [Scikit-learn](https://scikit-learn.org), [Pandas](https://pandas.pydata.org), [NumPy](https://numpy.org)
*   **Visualization:** [Matplotlib](https://matplotlib.org)
*   **Frontend:** HTML5, CSS3
*   **Data Source:** [OpenWeatherMap API](https://openweathermap.org)

## 🏗️ How It Works

### 1. Model Training (`train_model.py`)
*   Loads and cleans historical rainfall datasets.
*   Converts rainfall data into binary outcomes ($1$ = Rain, $0$ = No Rain).
*   Trains the **Random Forest** model and saves it as `model.pkl`.

### 2. Data Analysis (`data_analysis.py`)
*   Performs EDA to identify seasonal rainfall patterns in India.
*   Generates charts and trend graphs used in the dashboard.

### 3. Web Application (`app.py`)
*   The core engine that loads the ML model.
*   Fetches live API data or processes manual user input.
*   Renders dynamic results on `rain.html` (with a progress gauge) or `no_rain.html`.

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd AgriPredict


2. **Install dependencies:**
   ```
    pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
    python app.py

   ```
The app will be live at http://127.0.0.1

## 📁 Project Structure

```text
├── app.py              # Flask Backend Logic
├── train_model.py      # ML Model Training & Preprocessing
├── data_analysis.py    # EDA & Chart Generation
├── model.pkl           # Serialized ML Model
├── templates/          # HTML Pages (Index, Rain, No Rain)
├── static/             # CSS Stylesheets & Image Assets
├── css/             # CSS Stylesheets & Image Assets  
```
## 🎯 Impact & Value
AgriPredict demonstrates the power of combining **Machine Learning** with **Real-time APIs** to solve critical agricultural challenges. By delivering localized rainfall insights, the system:
* **Reduces Risk:** Helps farmers protect crops before heavy rain.
* **Data-Driven Decisions:** Moves farming away from guesswork to predictive science.
* **Scalability:** Highlights how AI can be made accessible to rural communities despite climate uncertainty.

<p align="center">
  <b>Developed with ❤️ by Thilak Nalla during the SmartBridge External Internship.</b>
</p>
