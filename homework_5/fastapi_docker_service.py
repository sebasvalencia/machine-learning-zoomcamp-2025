from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn

print("Loading pipeline from base image...")
with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)
print("Pipeline loaded successfully!")

app = FastAPI(title="Lead Scoring API - Docker", version="1.0.0")

class LeadData(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

class PredictionResponse(BaseModel):
    probability: float
    lead_data: dict

@app.get("/")
def read_root():
    return {"message": "Lead Scoring API (Docker) is running!", "version": "1.0.0", "model": "pipeline_v1.bin"}

@app.post("/predict", response_model=PredictionResponse)
def predict_lead_conversion(lead_data: LeadData):
    lead_dict = {
        "lead_source": lead_data.lead_source,
        "number_of_courses_viewed": lead_data.number_of_courses_viewed,
        "annual_income": lead_data.annual_income
    }
    
    records = [lead_dict]
    probabilities = pipeline.predict_proba(records)
    probability = probabilities[0][1]
    
    return PredictionResponse(
        probability=round(probability, 6),
        lead_data=lead_dict
    )

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True, "model": "pipeline_v2.bin"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)