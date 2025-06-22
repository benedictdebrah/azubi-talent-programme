from fastapi import FastAPI
from app.models import BankClient 
import joblib
import pandas as pd
from pathlib import Path
import os


app = FastAPI(title="Bank Marketing Model API")

# Use absolute path for model loading to avoid issues on Render
MODEL_PATH = Path(os.path.join(os.path.dirname(__file__), "app/src/artefacts/bank_marketing_workflow.pkl"))
print(f"Loading model from {MODEL_PATH}")
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
model = joblib.load(MODEL_PATH)


def predict_subscription(data: dict) -> dict:
    # Convert to DataFrame
    df = pd.DataFrame([data])
    # Predict
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return {
        "prediction": int(prediction),
        "subscription": "yes" if prediction == 1 else "no",
        "probability": round(probability, 4)
    }

@app.get("/")
async def root():
    return {"message": "Welcome to the Bank Marketing Model API"}

@app.post("/predict/")
async def predict(data: BankClient):
    result = predict_subscription(data.dict())
    return result

