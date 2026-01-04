![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)

# CarValue Predictor 🚗💰  
### End-to-End Car Price Prediction System

CarValue Predictor is an **end-to-end machine learning application** that predicts used car prices based on vehicle features.  
It combines a **FastAPI backend** for ML inference with an **interactive Streamlit UI** for real-time predictions.

---

## 🚀 Features

- Machine learning–based car price prediction
- REST API built with **FastAPI**
- Interactive frontend built with **Streamlit**
- Strong request validation using **Pydantic**
- Enum-based categorical feature handling
- Model artifacts loaded at application startup
- Clean separation of API, ML, and UI layers
- Ready for local and cloud deployment

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Regressor  
- **Dataset**: Used car dataset (CarDekho-style)
- **Target**: Selling Price (in lakhs)

### Input Features
- Car Name
- Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Number of Previous Owners

---

## 🧱 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Streamlit**
- **Pydantic**
- **Scikit-learn**
- **Uvicorn**

---

## 📂 Project Structure

```
carvalue-predictor/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schema.py
├── ml/
│   ├── __init__.py
│   └── model.py
├── ui/
│   └── streamlit_app.py
├── artifacts/
│   ├── random_forest_model.pkl
│   └── feature_columns.pkl
├── data/
│   └── cardekho_data.csv
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ⚙️ Setup & Run

### Clone the repository
```bash
git clone https://github.com/your-username/carvalue-predictor.git
cd carvalue-predictor
```

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs

---

## ▶️ Run Streamlit UI

```bash
streamlit run ui/streamlit_app.py
```

UI: http://localhost:8501

---

## 🔌 API Usage

### POST /predict

```json
{
  "Car_Name": "swift",
  "Year": 2014,
  "Present_Price": 5.59,
  "Kms_Driven": 40000,
  "Fuel_Type": "Petrol",
  "Seller_Type": "Dealer",
  "Transmission": "Manual",
  "Owner": 0
}
```

### Response
```json
{
  "predictionPrice": 4.52
}
```

---

## 👨‍💻 Author

**Shubham Yadav**  
Backend & Machine Learning Engineer

---

## 📄 License

MIT License
