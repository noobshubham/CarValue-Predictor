from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.schema import CarFeatures, PredictionResponse
from ml.model import predict_price, load_artifacts

app = FastAPI(title="Car Price Prediction API", version="1.0.0")

@app.on_event("startup")
def startup_event():
    load_artifacts()

@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={"success": True,
            "message": "Welcome to the Car Price Prediction API! API is up and running!"}
    )

@app.post("/predict", response_model=PredictionResponse)
def predict(features: CarFeatures):
    price = predict_price(features.model_dump())
    return PredictionResponse(predictionPrice=price)
