from pydantic import BaseModel, Field
from enum import Enum

class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    electric = "Electric"
    cng = "CNG"

class SellerType(str, Enum):
    dealer = "Dealer"
    individual = "Individual"
    trustmark_dealer = "Trustmark Dealer"

class Transmission(str, Enum):
    manual = "Manual"
    automatic = "Automatic"

class CarFeatures(BaseModel):
    Car_Name: str = Field(..., example="swift")
    Year: int = Field(..., example='2011')
    Present_Price: float = Field(..., example='6.87')
    Kms_Driven: int = Field(..., example='33429')
    Fuel_Type: FuelType
    Seller_Type: SellerType
    Transmission: Transmission
    Owner: int = Field(..., ge=0, le=3, example=0, description="number of previous owners")

class PredictionResponse(BaseModel):
    predictionPrice: float