from fastapi import FastAPI , HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,field_validator

import joblib,pickle
import pandas as pd 


ss =  joblib.load("models/std_scaler.bin")
model=  pickle.load(open("models/model.pkl","rb"))
app =  FastAPI()

class HouseModel(BaseModel):
    
    
    bedrooms: float = Field(..., gt=1, lt=10)
    bathrooms: float = Field(..., gt=1, lt=10)
    sqft_living: float = Field(..., gt=0, lt=10000)
    floors: float = Field(..., gt=0, lt=10000)
    view: float = Field(..., gt=0, lt=10000)
    condition: float = Field(..., gt=0, lt=10000)
    sqft_basement: float = Field(..., gt=0, lt=10000)
    
    
    @field_validator("sqft_living")
    @classmethod
    def normalize_sqft_living(cls,data):
        
        
        return ss.transform([[data]])
    
    
    

    
@app.post("/predict")
def predict(obj: HouseModel):
    
    data = pd.DataFrame({
        "bedrooms": [obj.bedrooms],
        "bathrooms": [obj.bathrooms],
        "sqft_living": [obj.sqft_living],
        "floors": [obj.floors],
        "view": [obj.view],
        "condition": [obj.condition],
        "sqft_basement": [obj.sqft_basement]
    })
    
    print(data)
    
    # Run prediction using your loaded ML model
    prediction = model.predict(data)[0]
    
    return JSONResponse(status_code=200,content={"predicted_price": float(prediction)})
    
    
    
    
