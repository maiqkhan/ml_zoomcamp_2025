import pickle 

from fastapi import FastAPI 
import uvicorn
from typing import Literal, Dict, Any
from pydantic import BaseModel, Field ,ConfigDict

class Lead_Input(BaseModel):
    model_config = ConfigDict(extra='forbid')

    lead_source: Literal['paid_ads', 'social_media', 'events', 'referral', 'organic_search']
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0.0)
    
class sub_proba_output(BaseModel):
    lead_proba: float

with open('pipeline_v2.bin', 'rb') as f_in:
    model = pickle.load(f_in) 

app = FastAPI(title="subscription-predictor")

@app.post("/predict")
def predict_sub(lead: Lead_Input) -> sub_proba_output:
    proba = model.predict_proba(lead.model_dump())[0, 1]

    return sub_proba_output(lead_proba=proba)


if __name__ == "__main__":
    uvicorn.run('predict:app', host="0.0.0.0", port=9696, reload=True)