from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import pandas as pd
import os
app = FastAPI()


class ScoringItem(BaseModel): 
    Median_Income:float
    Median_Age:int
    Tot_Rooms:int
    Latitude:float
    Longitude:float
    Distance_to_coast:float
    Distance_to_LA:float
    Distance_to_SanJose:float

#model_path = os.path.join(os.path.dirname(__file__), "lr_modelv4.pkl")
with open("./app/lr_modelv4.pkl", 'rb') as f: 
    model = pickle.load(f)

#print(model_path)
@app.post('/')
async def price(item:ScoringItem): 
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    yhat = model.predict(df)
    return {"prediction":float(yhat)}