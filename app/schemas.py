from pydantic import BaseModel

# Define request schema
class EnergyInput(BaseModel):
    Temperature: float
    Humidity: float
    SquareFootage: float
    Occupancy: int
    HVACUsage: int
    LightingUsage: int
    RenewableEnergy: float
    DayOfWeek: int
    Holiday: int