from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# Load model — go one folder up to find the ml/ folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'ml', 'price_model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

class RideInput(BaseModel):
    distance: float
    available_seats: int
    time_before_departure: float

@app.get("/")
def root():
    return {"message": "Carpooling Price Prediction API 🇲🇦"}

@app.post("/predict")
def predict(ride: RideInput):
    features = np.array([[
        ride.distance,
        ride.available_seats,
        ride.time_before_departure
    ]])
    predicted_price = model.predict(features)[0]

    if predicted_price < 5:
        predicted_price = 5

    return {
        "price": round(float(predicted_price), 2),
        "currency": "MAD"
    }