# 🏡 Real Estate Price Prediction

Welcome to the **Real Estate Price Prediction** project!  
This project uses a **Linear Regression** model trained on the Bengaluru property dataset to predict property prices based on various features.

---

## 📌 Project Description

This machine learning model predicts property prices using the following input parameters:

- 📏 **Total Area (in sqft)**
- 📍 **Location**
- 🛁 **Number of Bathrooms**
- 🛏️ **Number of Bedrooms (BHK)**

The trained model is integrated with a **Flask** server to expose APIs for prediction. It enables you to make real-time price predictions via HTTP requests.

## 📁 Project Structure

```bash
real-estate-price-prediction/
├── model_details
│        ├── Bengaluru_House_Data.csv
│        ├── common.py
│        ├── data_cleaning.py
│        └── model.py
├── README.md
├── requirements.txt
└── server
    ├── artifacts
    │   ├── banglore_home_prices_model.pickle
    │   └── columns.json
    ├── server.py
    └── util.py

```
---

## ⚙️ Requirements

- Python **3.10+**

---

## 🚀 Installation

Follow these steps to get started:

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <repo-directory>
   * Setup virtual venv
   * Activate virtual venv 
   pip install -r requirements.txt



## Model Pipeline
Navigate to the model_details directory and run:
```bash
   python model.py
```
This will generate a bangalore_home_prices_model.pickle file and save it to the server directory.

🌐 Running the Flask Server
Move to the server directory and run:

```bash
   python server.py
```
This will start the Flask server locally at http://127.0.0.1:5000/.


## 📡 API Endpoints

| Endpoint                        | Method      | Description                        |
|--------------------------------|-------------|------------------------------------|
| `/get_location_names`          | `GET`       | Returns a list of available locations |
| `/predict_home_price`          | `POST`/`GET`| Predicts property price using input features |

**Parameters for `/predict_home_price`**:

| Parameter    | Type   | Description                      |
|--------------|--------|----------------------------------|
| `total_sqft` | `int`  | Area of the property in sqft     |
| `location`   | `str`  | Location of the property         |
| `bhk`        | `int`  | Number of bedrooms (BHK)         |
| `bath`       | `int`  | Number of bathrooms              |


## 🧪 Example cURL Request

```bash
curl -X POST http://127.0.0.1:5000/predict_home_price \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "total_sqft=1200&location=Indira Nagar&bhk=2&bath=2"

```

## Reference
https://www.youtube.com/playlist?list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg

https://github.com/codebasics/py/tree/master/DataScience/BangloreHomePrices
