import requests
import json
from pydantic import BaseModel
class ScoringItem(BaseModel): 
    Median_Income:float
    Median_Age:int
    Tot_Rooms:int
    Latitude:float
    Longitude:float
    Distance_to_coast:float
    Distance_to_LA:float
    Distance_to_SanJose:float

item = ScoringItem(
    Median_Income=60000.0,
    Median_Age=35,
    Tot_Rooms=5,
    Latitude=34.0522,
    Longitude=-118.2437,
    Distance_to_coast=10.5,
    Distance_to_LA=0.0,
    Distance_to_SanJose=300.0
)
json_data = item.json()

r = requests.post("https://price-80802959201.asia-south1.run.app",json_data)
print(r.json())