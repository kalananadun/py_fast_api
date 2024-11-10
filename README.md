# Price Prediction API Documentation

Welcome to the official documentation for the **Price Prediction API**. This API predicts the price of a house based on various input features such as location, income, and room count.

---

## Base URL

The base URL for the API is: https://price-80802959201.asia-south1.run.app


---

## Authentication

No authentication is required to use this API. You can start making requests without the need for API keys or login credentials.

---

## Request Format

### Request Body

The API expects a `POST` request with the following JSON format:

| Parameter              | Type    | Description                                  |
|------------------------|---------|----------------------------------------------|
| `Median_Income`         | float   | Median income of the area                   |
| `Median_Age`            | int     | Median age of residents in the area         |
| `Tot_Rooms`             | int     | Total number of rooms in the house          |
| `Latitude`              | float   | Latitude coordinate of the house            |
| `Longitude`             | float   | Longitude coordinate of the house           |
| `Distance_to_coast`     | float   | Distance from the house to the coast (in miles) |
| `Distance_to_LA`        | float   | Distance from the house to Los Angeles (in miles) |
| `Distance_to_SanJose`   | float   | Distance from the house to San Jose (in miles) |

---

## Example Request

You can use the following Python script to interact with the API:

```python
import requests
from pydantic import BaseModel

# Define the data model
class ScoringItem(BaseModel): 
    Median_Income: float
    Median_Age: int
    Tot_Rooms: int
    Latitude: float
    Longitude: float
    Distance_to_coast: float
    Distance_to_LA: float
    Distance_to_SanJose: float

# Instantiate the data model with example values
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

# Convert the object to JSON
json_data = item.json()

# Send the POST request to the API
response = requests.post("https://price-80802959201.asia-south1.run.app", json=json_data)

# Print the response
print(response.json())


curl -X POST "https://price-80802959201.asia-south1.run.app" \
-H "Content-Type: application/json" \
-d '{
    "Median_Income": 60000.0,
    "Median_Age": 35,
    "Tot_Rooms": 5,
    "Latitude": 34.0522,
    "Longitude": -118.2437,
    "Distance_to_coast": 10.5,
    "Distance_to_LA": 0.0,
    "Distance_to_SanJose": 300.0
}'


```python
---
## Response of the api
{
    "predicted_price": 450000.0
}




